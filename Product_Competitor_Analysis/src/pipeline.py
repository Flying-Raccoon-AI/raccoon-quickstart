import concurrent.futures
from concurrent.futures import ThreadPoolExecutor
from typing import List, Dict

from raccoon.extract import RaccoonExtract
from src.ajio_pipeline import ProductCompetitorAjioAnalysis
from src.amazon_pipeline import ProductCompetitorAmazonAnalysis
from src.flipkart_pipeline import ProductCompetitorFlipkartAnalysis


class ProductCompetitorAnalysis:
    def __init__(self, max_workers: int = 3):
        self.raccoon_extract = RaccoonExtract()
        self.max_workers = max_workers

    def extract_product_details(self, item_url: str):
        product_details = self.raccoon_extract.extract_product_details(item_url)
        return product_details

    def handle(self, product_details: dict, platform: str):
        if platform == "Amazon":
            product_competitor_amazon_analysis = ProductCompetitorAmazonAnalysis()
            comparison_data = product_competitor_amazon_analysis.pipeline_amazon(product_details=product_details)
        elif platform == "Flipkart":
            product_competitor_flipkart_analysis = ProductCompetitorFlipkartAnalysis()
            comparison_data = product_competitor_flipkart_analysis.pipeline_flipkart(product_details=product_details)
        else:
            product_competitor_ajio_analysis = ProductCompetitorAjioAnalysis()
            comparison_data = product_competitor_ajio_analysis.pipeline_ajio(product_details=product_details)

        return comparison_data

    def pipeline(self, item_url: str, platforms: list):
        if 'flipkart' in item_url:
            given_platform = 'Flipkart'
        elif 'amazon' in item_url:
            given_platform = 'Amazon'
        else:
            given_platform = 'Ajio'

        product_details = self.extract_product_details(item_url)
        print("product_details", product_details)

        results = dict()
        results[given_platform] = product_details
        results[given_platform] = {"item_url": item_url, **product_details}

        for platform in platforms:
            if given_platform != platform:
                results[platform] = self.handle(product_details, platform)

        return results

    def _process_platform(self, args: tuple) -> tuple:
        """
        Helper function to process a single platform's analysis
        Returns tuple of (platform, result) for easier dictionary construction
        """
        product_details, platform = args
        try:
            result = self.handle(product_details, platform)
            return platform, result
        except Exception as e:
            print(f"Error processing {platform}: {str(e)}")
            return platform, {"error": str(e)}

    def multi_threaded_pipeline(self, item_url: str, platforms: List[str]) -> Dict:
        print("Processing item_url:", item_url)

        # Determine the source platform
        if 'flipkart' in item_url:
            given_platform = 'Flipkart'
        elif 'amazon' in item_url:
            given_platform = 'Amazon'
        elif 'ajio' in item_url:
            given_platform = 'Ajio'
        else:
            raise ValueError("Unsupported platform in URL")

        # Get product details from the source
        product_details = self.extract_product_details(item_url)
        print("Extracted product details:", product_details)

        # Initialize results with source platform data
        results = {
            given_platform: {
                "item_url": item_url,
                **product_details
            }
        }

        # Filter out the source platform from comparison platforms
        competitor_platforms = [p for p in platforms if p != given_platform]

        # Create tasks for each platform
        tasks = [(product_details, platform) for platform in competitor_platforms]

        # Process competitor platforms in parallel
        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            # Submit all tasks and gather results
            future_to_platform = {
                executor.submit(self._process_platform, task): task[1]
                for task in tasks
            }

            # Collect results as they complete
            for future in concurrent.futures.as_completed(future_to_platform):
                platform, result = future.result()
                results[platform] = result

        return results
