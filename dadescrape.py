# Process Flow

# 1) Read the Folio numbers in /home/kit/Downloads/Public-Certlist Paid_Unpd.xlsx

# 2) Loop each folio number and enter it on the website ('https://www8.miamidade.gov/Apps/PA/propertysearch/#/')

# 3) Use Selenium to access the website above and search each folio numbers and submit

# 4) Parse data using BS4

# 5) Save output to Csv using Pandas

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pandas as pd
from bs4 import BeautifulSoup


# Read Data from Excel Column Account Number
#df = pd.read_excel('/home/kit/Downloads/Public-CertlistPaid_Unpd.xlsx', sheet_name='Sheet1')
df = pd.read_excel('/home/kit/Documents/sample.xlsx', sheet_name='Sheet1')
url = 'https://www8.miamidade.gov/Apps/PA/propertysearch/#/'


# Selenium will access the website and enter the folio numbers to search page
for folio in df['Account Number']:
    driver = webdriver.Chrome()
    driver.get (url)
    driver.find_element_by_id('t-folio').click()
    search_bar = driver.find_element_by_id('search_box')
    search_bar.send_keys(folio) # Error Traceback
    search_bar.send_keys((Keys.RETURN))
    element = WebDriverWait(driver, 3).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="property_info"]')))

# Scrape all needed info
    scrape_page = driver.page_source
    soup = BeautifulSoup(scrape_page, 'lxml')



    driver.quit()