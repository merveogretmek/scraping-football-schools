# Scraping Football Schools

## Libraries

import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

## Functions

def scrape_page(driver, page_number):

    url = f"https://schoolsfootball.co.uk/schools?filter=a&county=&currentPage={page_number}"

    try:
        driver.get(url)
    except Exception as e:
        print(f"Error loading page {page_number} (driver.get): {e}")
        return []
    
    try:
        table_body = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.TAG_NAME, "tbody"))
        )
    except TimeoutException as e:
        print(f"Timeout waiting for table on page {page_number}: {e}")
        return []
    except Exception as e:
        print(f"Error waiting for table on page {page_number}: {e}")
        return []
    
    rows = table_body.find_elements(By.TAG_NAME, "tr")
    if not rows:
        print(f"No rows found on page {page_number}.")
        return []
    
    page_results = []

    for row in rows:
        try:
            name_element = row.find_element(
                By.CSS_SELECTOR, "a.fs-5.text-gray-900.text-hover-primary.fw-bold"
            )
            school_name = name_element.text.strip()
        except Exception as e:
            school_name = ""
            print(f"Could not extract school name on page {page_number}: {e}")
        
        try:
            address_element = row.find_element(By.CSS_SELECTOR, "div.fs-6.fw-semibold.text-gray-500"
            )
            address_text = address_element.text.strip()
            parts = [p.strip() for p in address_text.split(",") if p.strip()]
            country = parts[-1] if parts else ""
            city = parts[1] if len(parts) > 1 else ""
        except Exception as e:
            address_text = ""
            country = ""
            city = ""
            print(f"Could not extract address info on page {page_number}: {e}")
        
        page_results.append({
            "school_name": school_name,
            "address": address_text,
            "city": city,
            "country": country
        })

    return page_results
        
def main():

    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")

    driver = webdriver.Chrome(options=options)
    driver.set_page_load_timeout(180)

    all_schools = []
    page_number = 1

    while True:
        print(f"Scraping page {page_number}...")
        
        try:
            results = scrape_page(driver, page_number)
        except TimeoutException as te:
            print(f"Timeout occured on page {page_number}: {te}")
            page_number += 1
            continue
        except Exception as e:
            print(f"An error occured on page {page_number}: {e}")
            page_number += 1
            continue

        if not results:
            print("No more data found - ending pagination.")
            break

        all_schools.extend(results)
        page_number += 1
        time.sleep(1)

    output_file = "schools_data.csv"
    fieldnames = ["school_name", "address", "city", "country" ]

    with open(output_file, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(all_schools)

    print(f"Scraping complete. {len(all_schools)} schools saved to {output_file}")

## Scraping

if __name__ == "__main__":
    main()