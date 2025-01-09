# 🌐 **Product Competitor Analysis Tool**

## 🚀 Overview

The **Product Competitor Analysis Tool** is a sleek and intuitive Streamlit application designed to **compare product
prices and other details** across multiple e-commerce platforms. By entering a product URL, users can quickly see where to get the best
deals, saving time and money.

---

## ✨ Features

- **🔗 URL Input** – Simply paste the product URL to begin analysis.
- **🛍️ Platform Selection** – Choose from popular e-commerce platforms:
    - 🟧 **Amazon**
    - 🔵 **Flipkart**
    - 🟦 **Ajio**
- **📊 Price Comparison Table** – Compare prices, ratings, reviews, specs, and choose the best deal.
---

## 🛠️ Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Flying-Raccoon-AI/raccoon-quickstart.git
   cd Product_Competitor_Analysis
   ```

2. **Create a `.env` file** in the root directory and add the necessary environment variables:
   ```
   RACCOON_EXTRACT_BASE_URL=<your_raccoon_base_url>
   RACCOON_SECRET_KEY=<your_secret_key>
   RACCOON_PASSCODE=<your_passcode>
   ```

3. **run application using virtual environments**:
   ```bash
    python3 -m venv venv
    pip install -r requirements.txt
   ```

4. **Run the Streamlit App**

  ```bash
  streamlit run app.py
  ```

### **4. Enter the Product URL**

- Enter the product URL in the input field.
- Select the platforms you want to compare the product on.
- Click the "Compare Products" button to see the product comparison.

---

## 📦 Code Structure

- **src/**: Contains the main application logic.
    - **ajio_pipeline.py**: Handles product analysis for Ajio.
    - **amazon_pipeline.py**: Handles product analysis for Amazon.
    - **flipkart_pipeline.py**: Handles product analysis for Flipkart.
    - **raccoon/extract.py**: Contains the RaccoonExtract class for extracting product details using the Raccoon API.

- **requirements.txt**: Lists the required Python packages for the application.

---