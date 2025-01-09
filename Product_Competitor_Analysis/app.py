import streamlit as st
from PIL import Image

from src.pipeline import ProductCompetitorAnalysis

# Page Configuration
st.set_page_config(page_title="Product Competitor Analysis", layout="wide")

st.cache_data.clear()
st.cache_resource.clear()
# App Header
st.title("Product Competitor Analysis Tool")
st.write("Upload a product URL from an e-commerce website to compare prices across different platforms.")

# Sidebar for user input
with st.sidebar:
    st.header("Input Section")
    product_url = st.text_input("Enter Product URL:")
    upload_image = st.file_uploader("Upload Product Image (Optional)", type=["jpg", "png", "jpeg"])

    st.write("---")
    st.write("Select Platforms for Comparison:")
    amazon = st.checkbox("Amazon")
    flipkart = st.checkbox("Flipkart")
    ajio = st.checkbox("Ajio")

# Display uploaded image if available
if upload_image:
    image = Image.open(upload_image)
    st.image(image, caption='Uploaded Product Image', use_column_width=True)

# Submit button
if st.button("Compare Prices"):
    if product_url:
        st.success("Fetching product details and comparing prices...")
        # Placeholder for backend integration
        st.write("Product URL:", product_url)
        st.write("Platforms selected for comparison:")
        platforms = []
        if amazon:
            platforms.append("Amazon")
        if flipkart:
            platforms.append("Flipkart")
        if ajio:
            platforms.append("Ajio")

        if platforms:
            st.write(", ".join(platforms))
            product_competitor_analysis = ProductCompetitorAnalysis(max_workers=4)
            comparison_data = product_competitor_analysis.multi_threaded_pipeline(product_url, platforms)
            st.write(comparison_data)
        else:
            st.warning("No platforms selected. Please select at least one platform.")

        # Placeholder for data fetching and analysis
        st.info("Analyzing product details. Please wait...")
        # Simulated Data Display
        st.write("---")
        st.write("### Product Comparison Table")
    else:
        st.error("Please enter a valid product URL.")

# Footer
st.write("---")
st.caption("Developed by Your Company | © 2024")
