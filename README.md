# Scraping Football Schools

This repository contains a single Python script (`scraping_script.py`) that scrapes football school data from https://schoolsfootball.co.uk/. The script cycles through paginated search results, gathering school names, addresses, and location details. Finally, it writes the collected information to a CSV file, `schools_data.csv`.

## Overview

1. Headless Chrome
   The script automates a Chrome browser (headless by default) to load each 
   paginated results page.
2. School Info Extraction
   For each school, it retrieves:
   - School Name
   - Address
   - City
   - Country
3. Pagination
   Continues to the next page until no more results are found.
4. CSV Export
   Outputs all the scraped data into a CSV file named `schools_data.csv`.

## Requirements

- Python 3.7+
- Chrome Browser installed locally
- ChromeDriver (matching your installed Chrome version)
- selenium

## Setup Instructions

1. Clone the Repository

```bash
git clone https://github.com/merveogretmek/scraping-football-schools.git
cd scraping-football-schools
```

2. Install Required Dependencies

```bash
pip install selenium
```

3. Download ChromeDriver

- Ensure you download the version that matches your installed Chrome version.

4. Run the Script

```bash
python scraping_script.py
```

## How It Works

- Main Flow:
  1. Creates a headless Chrome browser via Selenium.
  2. Navigates through each page of results, scraping school details.
  3. Continues incrementing page numbers until no more data is returned.
  4. Saves all results to a CSV file named `schools_data.csv`.
- `scrape_page(driver, page_number):`
   - Constructs the target URL for the given page number.
   - Waits for the table to appear.
   - Retrieves each row, extracting the school name and address data.
  
