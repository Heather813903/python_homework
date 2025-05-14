#Task 6

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pandas as pd
import json
import time
import os

output_folder = "python_homeowrk/assignment9"
os.makedirs(output_folder, exist_ok=True)

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://owasp.org/www-project-top-ten/")
time.sleep


title = driver.title
print(title)

body = driver.find_element(By.CSS_SELECTOR, 'main')
if body:
    links = body.find_elements(By.CSS_SELECTOR, 'a')
    if len(links) > 0:
        print("href: ", links[0].get_attribute('href'))


elements = driver.find_elements(By.XPATH, "//a[strong]")


owasp_top_10 = []
for el in elements:
    title = el.text.strip()
    href = el.get_attribute("href")
    if "Top10" in href:
        owasp_top_10.append({"Title": title, "Link": href})

print ("Extracted OWASP Top 10")
for item in owasp_top_10:
    print(item)

csv_path = os.path.join(output_folder, "owasp_top_10.csv")
df = pd.DataFrame(owasp_top_10)
df.to_csv(csv_path, index=False)

print(f"\nData written to: {csv_path}")
driver.quit()


