# Scraping Instrument Website

This repository contains a single Python script, scraping_script.py, that scrapes module data from an online instrument marketplace (ModularGrid). The script collects information about both currently available and discontinued modules, then outputs a combined CSV file (`product_df.csv`) with the collected data.

## Overview

The `scraping_script.py` file:

1. Uses Selenium to automate a headless Chrome browser.
2. Scrolls through all search results to load every module on the page.
3. Extracts key data for each module:
   - Name, manufacturer, and descriptions
   - Availability status
   - Physical dimensions & power requirements
   - Pricing in both Euro and Dollar
   - Image links (uploaded to Cloudinary)
4. Combines results for both "currently available" and "discontinued" modules into a single DataFrame.
5. Writes final data to `product_df.csv`. 

## Requirements

- Python 3.7+
- Chrome Browser
- ChromeDriver
- Libraries
   - requests
   - selenium
   - pandas
   - beautifulsoup4
   - cloudinary

You can install them via:

```bash
pip install selenium pandas beautifulsoup4 cloudinary
```

## Setup Instructions












