from selenium import webdriver
from chromedriver_autoinstaller import install
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time
import hashlib
import os
import pandas as pd

##################################################

# TASK 3

##################################################

URL = 'https://batdongsan.com.vn'
TTL = 3600 #If the cache is older than this, we will refresh it
TIMESTAMP_COLUMN_INDEX = 6
PROPERTIES_DIV_CLASS_NAME = "re__product-item"
PROPERTIES_NAME_CLASS_NAME = "js__card-title"
PROPERTIES_IMAGE_CLASS_NAME = "re__card-image"
PROPERTIES_PRICE_CLASS_NAME = "re__card-config-price"
PROPERTIES_AREA_CLASS_NAME = "re__card-config-area"
PROPERTIES_LOCATION_CLASS_NAME = "re__card-location"
PROPERTIES_POST_TIME_CLASS_NAME = "re__card-published-info-published-at"
SCRIPT_DIRECTORY = os.path.dirname(__file__)

install() # Install the latest version of ChromeDriver if not exists

def check_cache(cache_key):
    # Check if the cache directory exists; if not, create it
    cache_directory = os.path.join(SCRIPT_DIRECTORY, "cache")  
    if not(os.path.exists(cache_directory)):
        os.mkdir(cache_directory)
        return False
    
    # Check if the cache file exists
    file_name = f"{cache_key}.csv"
    file_path = os.path.join(cache_directory, file_name)
    if not(os.path.exists(file_path)):
        return False

    # Read the DataFrame from the cache file
    df = pd.read_csv(file_path)
    
    # Check if the timestamp of the last row + TTL is greater than the current time
    if df.iloc[-1][TIMESTAMP_COLUMN_INDEX] + TTL > time.time():
        # Update the timestamp in the DataFrame
        df['timestamp'] = time.time()
        return True
    return False

def get_properties_detail(url):
    # Generate a cache key using the URL
    cache_key = hashlib.md5(url.encode()).hexdigest()
    
    # Check if data is available in the cache
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
    
    # Set up Chrome options
    chrome_options = ChromeOptions()
    # Uncomment the next line if you want to run headlessly
    # chrome_options.add_argument('--headless')
    chrome_options.add_argument('--enable-javascript')
    
    # Initialize the Chrome WebDriver
    driver = webdriver.Chrome(options=chrome_options)
    
    # Navigate to the specified URL
    driver.get(url)
    
    # Click the "View More" button to load additional content
    expand_button = WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.CLASS_NAME, "re__product-view-more")))
    expand_button.click()
    
    # Wait for the properties to be present on the page
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, PROPERTIES_DIV_CLASS_NAME)))
    
    # Find all property elements
    properties_divs = driver.find_elements(By.CLASS_NAME, PROPERTIES_DIV_CLASS_NAME)
    
    # Initialize an empty DataFrame
    df = pd.DataFrame(columns=['Name', 'Image', 'Price', 'Area', 'Location', 'PostTime'])
    
    # Loop through each property element
    for properties_div in properties_divs:        
        try:
            name = properties_div.find_element(By.CLASS_NAME, PROPERTIES_NAME_CLASS_NAME).text
        except NoSuchElementException:
            name = ""
        try:
            # Extract the image source using a CSS selector
            image = properties_div.find_element(By.CSS_SELECTOR, f".{PROPERTIES_IMAGE_CLASS_NAME} img").get_attribute('src')
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

        # Create a new row for the DataFrame
        new_row = {'Name': name, 'Image': image, 'Price': price, 'Area': area, 'Location': location, 'PostTime': post_time}
        
        # Concatenate the new row to the DataFrame
        df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
    
    # Create the cache directory if it doesn't exist
    cache_directory = os.path.join(SCRIPT_DIRECTORY, "cache")
    if not os.path.exists(cache_directory):
        os.makedirs(cache_directory)
    
    # Add a timestamp column and write the DataFrame to a CSV file
    df['timestamp'] = time.time()
    df.to_csv(os.path.join(cache_directory, f"{cache_key}.csv"), index=False)
    
    print(df)
    
    # Close the WebDriver
    time.sleep(5)  # Adjust this if needed for proper visibility in a headless browser
    driver.close()

# Call the function with the specified URL
get_properties_detail(URL)
