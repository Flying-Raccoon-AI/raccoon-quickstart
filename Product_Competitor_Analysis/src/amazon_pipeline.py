import urllib.parse

from raccoon.extract import RaccoonExtract


class ProductCompetitorAmazonAnalysis:
    def __init__(self):
        self.raccoon_extract = RaccoonExtract()

    @staticmethod
    def parse_amazon_search_url(search_text: str):
        encoded_product_name = urllib.parse.quote(search_text)
        search_url = f"https://www.amazon.in/s?k={encoded_product_name}"
        return search_url

    def pipeline_amazon(self, product_details: dict) -> dict:
        search_text = product_details.get('title') + ', ' + product_details.get('color')
        search_url = self.parse_amazon_search_url(search_text)
        most_relevant_item_url = self.raccoon_extract.extract_most_relevant_from_url(search_url)
        most_relevant_item_details = self.raccoon_extract.extract_product_details(most_relevant_item_url)
        return {"item_url": most_relevant_item_url, **most_relevant_item_details}
