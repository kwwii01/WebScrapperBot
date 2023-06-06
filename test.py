import random
import time
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.headless = True

driver = webdriver.Chrome(executable_path='chromedriver.exe', options=options)
while True:
    driver.get('https://www.google.com/search?tbm=isch&q=kaneki+manga+art')
    all_images = driver.find_elements(By.CLASS_NAME, 'islir')

    image_to_download = random.choice(all_images)
    image_to_download.click()

    try:

        image_itself = driver.find_element(By.CLASS_NAME, 'n3VNCb')

        image_url = image_itself.get_attribute('src')

        image_response = requests.get(image_url)

        with open(f'{round(time.time())}.png', 'wb') as retrieved_image:
            retrieved_image.write(image_response.content)
            exit(0)
        
    except:
        pass
