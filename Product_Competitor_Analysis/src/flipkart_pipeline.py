import urllib.parse

from raccoon.extract import RaccoonExtract


class ProductCompetitorFlipkartAnalysis:
    def __init__(self):
        self.raccoon_extract = RaccoonExtract()

    @staticmethod
    def parse_flipkart_search_url(search_text: str):
        encoded_product_name = urllib.parse.quote(search_text)
        search_url = f"https://www.flipkart.com/search?q={encoded_product_name}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
        return search_url

    def pipeline_flipkart(self, product_details: dict) -> dict:
        search_text = product_details.get('title') + ', ' + product_details.get('color')
        search_url = self.parse_flipkart_search_url(search_text)
        most_relevant_item_url = self.raccoon_extract.extract_most_relevant_from_url(search_url)
        most_relevant_item_details = self.raccoon_extract.extract_product_details(most_relevant_item_url)
        return {"item_url": most_relevant_item_url, **most_relevant_item_details}
