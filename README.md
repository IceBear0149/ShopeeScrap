# Shopee API Scraper

This repository contains two scrapers for extracting product data from Shopee Taiwan (shopee.tw) by intercepting API responses.

## Overview

The project consists of two scraping tools:
1. `shopee_focused_scraper.py` - For scraping a single product URL at a time
2. `ShopeeApiScraper` - For batch scraping multiple product URLs

Both tools use browser automation with Selenium and undetected-chromedriver to navigate Shopee pages while monitoring network traffic to capture API responses containing detailed product information.

## Requirements

- Python 3.6+
- undetected-chromedriver
- Selenium
- Chrome browser

To install dependencies:
```bash
pip install selenium undetected-chromedriver
```

## Single Product Scraper (`shopee_focused_scraper.py`)

### Description

This script is designed to extract detailed information from a single Shopee product page by monitoring the network traffic and capturing the API response.

### Usage

1. Edit the URL in the `main()` function to target your desired product:
   ```python
   url = "https://shopee.tw/your-product-url-here"
   ```

2. Run the script:
   ```bash
   python shopee_focused_scraper.py
   ```

3. First-time setup:
   - If this is your first time running the script, you'll need to log in to Shopee manually
   - You may need to solve CAPTCHA challenges if prompted

4. Interacting with the page:
   - After the page loads, scroll down until the product description section is visible
   - The script monitors network traffic as you interact with the page
   - Press Enter in the terminal to check if data has been captured
   - Type 'done' and press Enter to exit the monitoring mode

5. Output:
   - When the API response is successfully captured, the script will save it to a JSON file
   - The file will be named `shopee_item_{item_id}.json`

## Batch Scraper (`ShopeeApiScraper`)

### Description

This more advanced scraper allows you to process multiple Shopee product URLs in batches. It opens multiple tabs and allows you to interact with each page while it monitors and captures API responses.

### Usage

1. Create a text file named `link_shopee.txt` containing one product URL per line

2. Run the script:
   ```bash
   python batch_shopee_scraper.py
   ```

3. Configure tabs:
   - You'll be prompted to enter the maximum number of concurrent tabs (3-10 recommended)

4. Tab management:
   - The script will open multiple tabs based on your configuration
   - You need to manually interact with each tab (scroll, click)
   - Enter a tab number to check if data has been captured from that tab
   - If data is found, the tab will be marked as processed and replaced with a new URL

5. Output:
   - All captured data is saved in `shopee_all_items.json`
   - Progress is automatically saved as you go

## Important Notes

- **Anti-scraping measures**: Shopee employs anti-scraping techniques. These scripts use undetected-chromedriver and a semi-manual approach to avoid detection.
- **Cookies**: Both scrapers save and load cookies to maintain session information between runs.
- **Captcha**: You may need to solve CAPTCHA challenges manually when prompted.
- **Browser profile**: A Chrome profile is created and stored in your home directory to maintain login state.

## Troubleshooting

If you encounter issues:

1. Make sure you're logged in to Shopee when prompted
2. Solve any CAPTCHA challenges that appear
3. Interact with the page (scroll down to the description) to trigger the API calls
4. Check that the target API URL pattern hasn't changed
5. Check console for error messages

## Legal Notice

This tool is for educational purposes only. Be sure to comply with Shopee's Terms of Service and avoid excessive scraping that could impact their servers.# Shopee API Scraper

This repository contains two scrapers for extracting product data from Shopee Taiwan (shopee.tw) by intercepting API responses.

## Overview

The project consists of two scraping tools:
1. `shopee_focused_scraper.py` - For scraping a single product URL at a time
2. `ShopeeApiScraper` - For batch scraping multiple product URLs

Both tools use browser automation with Selenium and undetected-chromedriver to navigate Shopee pages while monitoring network traffic to capture API responses containing detailed product information.

## Requirements

- Python 3.6+
- undetected-chromedriver
- Selenium
- Chrome browser

To install dependencies:
```bash
pip install selenium undetected-chromedriver
```

## Single Product Scraper (`shopee_focused_scraper.py`)

### Description

This script is designed to extract detailed information from a single Shopee product page by monitoring the network traffic and capturing the API response.

### Usage

1. Edit the URL in the `main()` function to target your desired product:
   ```python
   url = "https://shopee.tw/your-product-url-here"
   ```

2. Run the script:
   ```bash
   python shopee_focused_scraper.py
   ```

3. First-time setup:
   - If this is your first time running the script, you'll need to log in to Shopee manually
   - You may need to solve CAPTCHA challenges if prompted

4. Interacting with the page:
   - After the page loads, scroll down until the product description section is visible
   - The script monitors network traffic as you interact with the page
   - Press Enter in the terminal to check if data has been captured
   - Type 'done' and press Enter to exit the monitoring mode

5. Output:
   - When the API response is successfully captured, the script will save it to a JSON file
   - The file will be named `shopee_item_{item_id}.json`

## Batch Scraper (`ShopeeApiScraper`)

### Description

This more advanced scraper allows you to process multiple Shopee product URLs in batches. It opens multiple tabs and allows you to interact with each page while it monitors and captures API responses.

### Usage

1. Create a text file named `link_shopee.txt` containing one product URL per line

2. Run the script:
   ```bash
   python batch_shopee_scraper.py
   ```

3. Configure tabs:
   - You'll be prompted to enter the maximum number of concurrent tabs (3-10 recommended)

4. Tab management:
   - The script will open multiple tabs based on your configuration
   - You need to manually interact with each tab (scroll, click)
   - Enter a tab number to check if data has been captured from that tab
   - If data is found, the tab will be marked as processed and replaced with a new URL

5. Output:
   - All captured data is saved in `shopee_all_items.json`
   - Progress is automatically saved as you go

## Important Notes

- **Anti-scraping measures**: Shopee employs anti-scraping techniques. These scripts use undetected-chromedriver and a semi-manual approach to avoid detection.
- **Cookies**: Both scrapers save and load cookies to maintain session information between runs.
- **Captcha**: You may need to solve CAPTCHA challenges manually when prompted.
- **Browser profile**: A Chrome profile is created and stored in your home directory to maintain login state.

## Troubleshooting

If you encounter issues:

1. Make sure you're logged in to Shopee when prompted
2. Solve any CAPTCHA challenges that appear
3. Interact with the page (scroll down to the description) to trigger the API calls
4. Check that the target API URL pattern hasn't changed
5. Check console for error messages

## Legal Notice

This tool is for educational purposes only. Be sure to comply with Shopee's Terms of Service and avoid excessive scraping that could impact their servers.# Shopee API Scraper

This repository contains two scrapers for extracting product data from Shopee Taiwan (shopee.tw) by intercepting API responses.

## Overview

The project consists of two scraping tools:
1. `shopee_focused_scraper.py` - For scraping a single product URL at a time
2. `ShopeeApiScraper` - For batch scraping multiple product URLs

Both tools use browser automation with Selenium and undetected-chromedriver to navigate Shopee pages while monitoring network traffic to capture API responses containing detailed product information.

## Requirements

- Python 3.6+
- undetected-chromedriver
- Selenium
- Chrome browser

To install dependencies:
```bash
pip install selenium undetected-chromedriver
```

## Single Product Scraper (`shopee_focused_scraper.py`)

### Description

This script is designed to extract detailed information from a single Shopee product page by monitoring the network traffic and capturing the API response.

### Usage

1. Edit the URL in the `main()` function to target your desired product:
   ```python
   url = "https://shopee.tw/your-product-url-here"
   ```

2. Run the script:
   ```bash
   python shopee_focused_scraper.py
   ```

3. First-time setup:
   - If this is your first time running the script, you'll need to log in to Shopee manually
   - You may need to solve CAPTCHA challenges if prompted

4. Interacting with the page:
   - After the page loads, scroll down until the product description section is visible
   - The script monitors network traffic as you interact with the page
   - Press Enter in the terminal to check if data has been captured
   - Type 'done' and press Enter to exit the monitoring mode

5. Output:
   - When the API response is successfully captured, the script will save it to a JSON file
   - The file will be named `shopee_item_{item_id}.json`

## Batch Scraper (`ShopeeApiScraper`)

### Description

This more advanced scraper allows you to process multiple Shopee product URLs in batches. It opens multiple tabs and allows you to interact with each page while it monitors and captures API responses.

### Usage

1. Create a text file named `link_shopee.txt` containing one product URL per line

2. Run the script:
   ```bash
   python batch_shopee_scraper.py
   ```

3. Configure tabs:
   - You'll be prompted to enter the maximum number of concurrent tabs (3-10 recommended)

4. Tab management:
   - The script will open multiple tabs based on your configuration
   - You need to manually interact with each tab (scroll, click)
   - Enter a tab number to check if data has been captured from that tab
   - If data is found, the tab will be marked as processed and replaced with a new URL

5. Output:
   - All captured data is saved in `shopee_all_items.json`
   - Progress is automatically saved as you go

## Important Notes

- **Anti-scraping measures**: Shopee employs anti-scraping techniques. These scripts use undetected-chromedriver and a semi-manual approach to avoid detection.
- **Cookies**: Both scrapers save and load cookies to maintain session information between runs.
- **Captcha**: You may need to solve CAPTCHA challenges manually when prompted.
- **Browser profile**: A Chrome profile is created and stored in your home directory to maintain login state.

## Troubleshooting

If you encounter issues:

1. Make sure you're logged in to Shopee when prompted
2. Solve any CAPTCHA challenges that appear
3. Interact with the page (scroll down to the description) to trigger the API calls
4. Check that the target API URL pattern hasn't changed
5. Check console for error messages

## Legal Notice

This tool is for educational purposes only. Be sure to comply with Shopee's Terms of Service and avoid excessive scraping that could impact their servers.# Shopee API Scraper

This repository contains two scrapers for extracting product data from Shopee Taiwan (shopee.tw) by intercepting API responses.

## Overview

The project consists of two scraping tools:
1. `shopee_focused_scraper.py` - For scraping a single product URL at a time
2. `ShopeeApiScraper` - For batch scraping multiple product URLs

Both tools use browser automation with Selenium and undetected-chromedriver to navigate Shopee pages while monitoring network traffic to capture API responses containing detailed product information.

## Requirements

- Python 3.6+
- undetected-chromedriver
- Selenium
- Chrome browser

To install dependencies:
```bash
pip install selenium undetected-chromedriver
```

## Single Product Scraper (`shopee_focused_scraper.py`)

### Description

This script is designed to extract detailed information from a single Shopee product page by monitoring the network traffic and capturing the API response.

### Usage

1. Edit the URL in the `main()` function to target your desired product:
   ```python
   url = "https://shopee.tw/your-product-url-here"
   ```

2. Run the script:
   ```bash
   python shopee_focused_scraper.py
   ```

3. First-time setup:
   - If this is your first time running the script, you'll need to log in to Shopee manually
   - You may need to solve CAPTCHA challenges if prompted

4. Interacting with the page:
   - After the page loads, scroll down until the product description section is visible
   - The script monitors network traffic as you interact with the page
   - Press Enter in the terminal to check if data has been captured
   - Type 'done' and press Enter to exit the monitoring mode

5. Output:
   - When the API response is successfully captured, the script will save it to a JSON file
   - The file will be named `shopee_item_{item_id}.json`

## Batch Scraper (`ShopeeApiScraper`)

### Description

This more advanced scraper allows you to process multiple Shopee product URLs in batches. It opens multiple tabs and allows you to interact with each page while it monitors and captures API responses.

### Usage

1. Create a text file named `link_shopee.txt` containing one product URL per line

2. Run the script:
   ```bash
   python batch_shopee_scraper.py
   ```

3. Configure tabs:
   - You'll be prompted to enter the maximum number of concurrent tabs (3-10 recommended)

4. Tab management:
   - The script will open multiple tabs based on your configuration
   - You need to manually interact with each tab (scroll, click)
   - Enter a tab number to check if data has been captured from that tab
   - If data is found, the tab will be marked as processed and replaced with a new URL

5. Output:
   - All captured data is saved in `shopee_all_items.json`
   - Progress is automatically saved as you go

## Important Notes

- **Anti-scraping measures**: Shopee employs anti-scraping techniques. These scripts use undetected-chromedriver and a semi-manual approach to avoid detection.
- **Cookies**: Both scrapers save and load cookies to maintain session information between runs.
- **Captcha**: You may need to solve CAPTCHA challenges manually when prompted.
- **Browser profile**: A Chrome profile is created and stored in your home directory to maintain login state.

## Troubleshooting

If you encounter issues:

1. Make sure you're logged in to Shopee when prompted
2. Solve any CAPTCHA challenges that appear
3. Interact with the page (scroll down to the description) to trigger the API calls
4. Check that the target API URL pattern hasn't changed
5. Check console for error messages

## Legal Notice

This tool is for educational purposes only. Be sure to comply with Shopee's Terms of Service and avoid excessive scraping that could impact their servers.
