import os

import requests
from dotenv import load_dotenv

load_dotenv()

RACCOON_PASSCODE = os.getenv('RACCOON_PASSCODE')
RACCOON_SECRET_KEY = os.getenv('RACCOON_SECRET_KEY')
RACCOON_EXTRACT_BASE_URL = os.getenv('RACCOON_EXTRACT_BASE_URL')


class RaccoonExtract:
    def __init__(self):
        self.base_url = RACCOON_EXTRACT_BASE_URL
        self.headers = {
            'raccoon-passcode': RACCOON_PASSCODE,
            'secret-key': RACCOON_SECRET_KEY,
            'Content-Type': 'application/json',
        }

    def extract_product_details(self, product_url: str):

        json_data = {
            'query': 'Extract comprehensive product information including the title, brand, product type, price, detailed specifications (material, sleeve type), style (based on images), color, unique description, and product rating, image URL. Please extract information from given URL and do not navigate',
            'app_url': product_url,
            'schema': {
                'title': 'Make it short and concise',
                'brand': 'Brand or manufacturer name',
                'type': 'Category or type of product',
                'price': 'Listed price in INR or other relevant currency',
                'product_details': 'Material, sleeve type, and additional key details from the product specifications',
                'style': 'Style or design based on product images and description',
                'color': 'main color of the product',
                'description': 'Detailed and unique product description',
                'rating': 'Overall product rating (out of 5 stars) including number of reviews if available',
                'image_url': 'also fetch main image URL',
            },
            'render_js': True,
            'full_page': True,
            'single_page': False,
            'chat_history': [],
            'max_count': 1,
        }

        response = requests.post(self.base_url, headers=self.headers, json=json_data)

        if response.status_code == 200:
            response_json = response.json()
            if response_json[-1].get("status_code") == 200:
                return response_json[-1].get('data').get('data')[0]
            else:
                print(response_json[-1])
                return {}
        else:
            return {}

    def extract_most_relevant_from_url(self, search_url: str):

        payload = {
            "query": "Retrieve the URL of the top result from search results.",
            "app_url": search_url,
            "schema": {
                "url": "URL of the top-listed product"
            },
            "render_js": True,
            "full_page": True,
            "single_page": True,
            "chat_history": [],
            "max_count": 1
        }

        response = requests.post(self.base_url, headers=self.headers, json=payload)

        if response.status_code == 200:
            response_json = response.json()
            if response_json[-1].get("status_code") == 200:
                return response_json[-1].get('data').get('data')[0].get('url')
            else:
                print(response_json[-1])
                return {}
        else:
            return {}
