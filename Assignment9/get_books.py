from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pandas as pd
import json
import time
import os

output_folder = "assignment9"
os.makedirs(output_folder, exist_ok=True)

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

#Task 3.3
driver.get("https://durhamcounty.bibliocommons.com/v2/search?query=learning%20spanish&searchType=smart")
time.sleep


title = driver.title
print(title)

li_elements = driver.find_elements(By.TAG_NAME, 'li')
print(f"Found {len(li_elements)} <li> elements.")

#Task 3.4
results = []

#Task 3.5
for li in li_elements:
    try:  #book title
       title_elem = li.find_element(By.CLASS_NAME, "cp-title")
       title = title_elem.text.strip()
          #get author 
       author_elems = li.find_elements(By.CLASS_NAME, "author-link")  
       authors = "; ".join([author.text.strip() for author in author_elems])
          #get format and year
       format_year_elem = li.find_element(By.CLASS_NAME, "cp-format-info")
       span = format_year_elem.find_element(By.TAG_NAME, "span")
       format_year = span.text.strip()
          #store results
       results.append({
           "Title": title,
           "Author": authors,
           "Format-Year": format_year 
       }) 

    except Exception as e:
        print("Skipping one entry due to error:", e)

driver.quit()

    #Task 3.6
df = pd.DataFrame(results)
print(df)

# Task 4
# Save to csv
csv_path = os.path.join(output_folder, "get_books.csv") 
df.to_csv(csv_path, index=False)
print(f"Saved DataFrame to {csv_path}")

# Save to JSON
json_path = os.path.join(output_folder, "get_books.json")
with open(json_path, "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=4)
print(f"Saved results to {json_path}")


