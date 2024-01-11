from selenium import webdriver
from chromedriver_autoinstaller import install
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time
import csv
import hashlib
import os
import pandas as pd

##################################################

# TASK 3

##################################################
URL = 'https://batdongsan.com.vn'
TTL = 3600
TIMESTAMP_COLUMN_INDEX = 6
PROPERTIES_DIV_CLASS_NAME = "re__product-item"
PROPERTIES_NAME_CLASS_NAME= "js__card-title"
PROPERTIES_IMAGE_CLASS_NAME = "Ảnh đại diện"
PROPERTIES_PRICE_CLASS_NAME = "re__card-config-price"
PROPERTIES_AREA_CLASS_NAME = "re__card-config-area"
PROPERTIES_LOCATION_CLASS_NAME = "re__card-location"
PROPERTIES_POST_TIME_CLASS_NAME = "re__card-published-info-published-at"
SCRIPT_DIRECTORY = os.path.dirname(__file__)
install()


def check_cache(cache_key):
    return False
    cache_directory = os.path.join(SCRIPT_DIRECTORY, "cache")  
    if not(os.path.exists(cache_directory)):
        os.mkdir(cache_directory)
        return False
    file_name = f"{cache_key}.csv"
    file_path = os.path.join(cache_directory, file_name)
    if not(os.path.exists(file_path)):
        return False
    df = pd.read_csv(file_path)
    if df.iloc[-1][6] + TTL > time.time():
        df['timestamp'] = time.time()
        return True
    return False

def get_properties_detail(url):
    cache_key = hashlib.md5(url.encode()).hexdigest()
    if check_cache(cache_key):
        print("Reading data from cache")
        script_directory = os.path.dirname(__file__)
        cache_directory = os.path.join(script_directory, "cache")  
        file_name = f"{cache_key}.csv"
        file_path = os.path.join(cache_directory, file_name)
        df = pd.read_csv(file_path)
        print(df)
        return 
    
    print("Reading data from website")
    chrome_options = ChromeOptions()
    # chrome_options.add_argument('--headless')
    chrome_options.add_argument('--enable-javascript')
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    # expand_button = WebDriverWait(driver,40).until(EC.element_to_be_clickable((By.CLASS_NAME, "re__product-view-more")))
    # expand_button.click()
    for _ in range(10):
        driver.execute_script("window.scrollBy(0, 350)")
        time.sleep(1)
    WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.CLASS_NAME, PROPERTIES_DIV_CLASS_NAME)))
    properties_divs = driver.find_elements(By.CLASS_NAME, PROPERTIES_DIV_CLASS_NAME)
    df = pd.DataFrame(columns=['Name', 'Image', 'Price', 'Area', 'Location', 'PostTime'])
    for properties_div in properties_divs:        
        try:
            name = properties_div.find_element(By.CLASS_NAME, PROPERTIES_NAME_CLASS_NAME).text
        except NoSuchElementException:
            name = ""
        try:
            image = properties_div.find_element(By.CLASS_NAME, PROPERTIES_IMAGE_CLASS_NAME).get_attribute("src")
        except NoSuchElementException:
            image = ""
        try:
            price = properties_div.find_element(By.CLASS_NAME, PROPERTIES_PRICE_CLASS_NAME).text
        except NoSuchElementException:
            price = ""
        try:
            area = properties_div.find_element(By.CLASS_NAME, PROPERTIES_AREA_CLASS_NAME).text
        except NoSuchElementException:
            area = ""
        try:
            location = properties_div.find_element(By.CLASS_NAME, PROPERTIES_LOCATION_CLASS_NAME).text
        except NoSuchElementException:
            location = ""
        try:
            post_time = properties_div.find_element(By.CLASS_NAME, PROPERTIES_POST_TIME_CLASS_NAME).text
        except NoSuchElementException:
            post_time = ""

        new_row = {'Name': name, 'Image': image, 'Price': price, 'Area': area, 'Location': location, 'PostTime': post_time}
        df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
    cache_directory = os.path.join(SCRIPT_DIRECTORY, "cache")
    if not os.path.exists(cache_directory):
        os.makedirs(cache_directory)
    df['timestamp'] = time.time()
    df.to_csv(os.path.join(cache_directory, f"{cache_key}.csv"), index=False)
    print(df)
    time.sleep(5)
    driver.close()


##

get_properties_detail(URL)