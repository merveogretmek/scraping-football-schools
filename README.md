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
