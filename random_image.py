import re
import requests
import random
import time
from urllib.parse import quote
from bs4 import BeautifulSoup

def get_random_image(request_phrase):
    response = requests.get(f'https://www.google.com/search?tbm=isch&q={handle_cyrillic(request_phrase)}')
    html_text = response.text

    soup = BeautifulSoup(html_text, 'lxml')
    all_images = soup.find_all('img')

    while True:
        random_image = random.choice(all_images)

        if (isinstance(random_image, str)):
            return random_image

        try:

            image_response = requests.get(random_image.attrs['src'])
            with open(f'{round(time.time())}.png', 'wb') as retrieved_image:
                retrieved_image.write(image_response.content)
                return retrieved_image.name

        except:
            pass


def handle_cyrillic(text):
    if (re.search(r'p{IsCyrillic}', text)):
        return quote(text.encode('cp1251'))
    else:
        return text.replace(" ", "+")
