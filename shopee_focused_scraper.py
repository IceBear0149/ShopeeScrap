import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
import time
import json
import os
import signal
import sys
import pickle

class ShopeeApiScraper:
    def __init__(self):
        self.driver = None
        self.user_data_dir = os.path.join(os.path.expanduser("~"), "shopee_chrome_profile")
        self.target_api_url = "https://shopee.tw/api/v4/pdp/get_pc?"
        
    def initialize_driver(self):
        options = uc.ChromeOptions()
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument(f"--user-data-dir={self.user_data_dir}")
        
        # Add DevTools Protocol logging
        options.set_capability("goog:loggingPrefs", {"performance": "ALL", "browser": "ALL"})
        
        print("Initializing undetected ChromeDriver...")
        self.driver = uc.Chrome(options=options)
        
        # Load cookies if they exist
        self.load_cookies()
    
    def save_cookies(self):
        if not os.path.exists("cookies"):
            os.makedirs("cookies")
        with open("cookies/shopee_cookies.pkl", "wb") as f:
            pickle.dump(self.driver.get_cookies(), f)
        print("Cookies saved successfully.")
    
    def load_cookies(self):
        try:
            # First navigate to a page on the domain
            self.driver.get("https://shopee.tw")
            time.sleep(2)
            
            # Then load cookies
            if os.path.exists("cookies/shopee_cookies.pkl"):
                with open("cookies/shopee_cookies.pkl", "rb") as f:
                    cookies = pickle.load(f)
                    for cookie in cookies:
                        self.driver.add_cookie(cookie)
                print("Cookies loaded successfully.")
                # Refresh to apply cookies
                self.driver.refresh()
                time.sleep(2)
            else:
                print("No saved cookies found.")
        except Exception as e:
            print(f"Error loading cookies: {e}")
    
    def extract_network_responses(self):
        """Extract network responses from Chrome DevTools Protocol logs"""
        logs = self.driver.get_log("performance")
        target_responses = []
        response_bodies = {}
        
        # First pass: collect all requests and responses
        for entry in logs:
            try:
                message = json.loads(entry["message"])["message"]
                
                # Capture response received events
                if message["method"] == "Network.responseReceived":
                    req_id = message["params"]["requestId"]
                    resp = message["params"]["response"]
                    url = resp["url"]
                    
                    # Check if this is our target API URL
                    if self.target_api_url in url:
                        target_responses.append({
                            "requestId": req_id,
                            "url": url,
                            "status": resp["status"],
                            "headers": resp["headers"]
                        })
                
                # Capture response body events
                elif message["method"] == "Network.responseReceived" or message["method"] == "Network.dataReceived":
                    if "params" in message and "requestId" in message["params"]:
                        req_id = message["params"]["requestId"]
                        
                        # We'll get the response body separately
                        for req in target_responses:
                            if req["requestId"] == req_id:
                                # Get response body
                                try:
                                    body = self.driver.execute_cdp_cmd("Network.getResponseBody", {"requestId": req_id})
                                    response_bodies[req_id] = body
                                except Exception as e:
                                    print(f"Error getting response body: {e}")
            except Exception as e:
                pass
        
        # Second pass: attach response bodies to their requests
        results = []
        for req in target_responses:
            req_id = req["requestId"]
            if req_id in response_bodies:
                req["response"] = response_bodies[req_id]
                results.append(req)
        
        return results
    
    def monitor_network_traffic(self, url):
        print(f"Accessing {url} and monitoring for target API calls...")
        
        # Enable network monitoring
        self.driver.execute_cdp_cmd("Network.enable", {})
        
        # Navigate to the target URL
        self.driver.get(url)
        
        print("Waiting for page to load and API calls to be made...")
        print("Interact with the page as needed to trigger the API calls.")
        print("Press Enter to continue monitoring or type 'done' to finish...")
        
        found_target = False
        
        while True:
            user_input = input()
            if user_input.lower() == 'done':
                break
            
            # Extract responses that match our target
            responses = self.extract_network_responses()
            
            if responses:
                for response in responses:
                    try:
                        if "response" in response and "body" in response["response"]:
                            body_text = response["response"]["body"]
                            
                            # Try to parse as JSON
                            try:
                                body_json = json.loads(body_text)
                                
                                # Check if it has the structure we're looking for
                                if "data" in body_json and "item" in body_json["data"]:
                                    item = body_json["data"]["item"]
                                    if "item_id" in item and "title" in item:
                                        print("\n" + "="*50)
                                        print(f"✅ FOUND TARGET RESPONSE!")
                                        print(f"Item ID: {item['item_id']}")
                                        print(f"Title: {item['title']}")
                                        print("="*50 + "\n")
                                        
                                        # Save to file
                                        output_file = f"shopee_item_{item['item_id']}.json"
                                        with open(output_file, "w", encoding="utf-8") as f:
                                            json.dump(body_json, f, indent=4, ensure_ascii=False)
                                        print(f"Saved response to {output_file}")
                                        
                                        found_target = True
                            except json.JSONDecodeError:
                                continue
                    except Exception as e:
                        print(f"Error processing response: {e}")
            
            if not found_target:
                print("No target responses found yet. Continue monitoring? (Press Enter or type 'done')")
    
    def cleanup(self):
        if self.driver:
            self.save_cookies()
            self.driver.quit()
        print("Cleanup complete")

def main():
    url = "https://shopee.tw/---i.2976113.26711692578" #ubah bagian ini saja
    
    scraper = ShopeeApiScraper()
    
    try:
        scraper.initialize_driver()
        scraper.monitor_network_traffic(url)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        scraper.cleanup()

if __name__ == "__main__":
    # Handle ctrl+c gracefully
    def signal_handler(sig, frame):
        print('Ctrl+C detected. Cleaning up...')
        sys.exit(0)
    
    signal.signal(signal.SIGINT, signal_handler)
    main()