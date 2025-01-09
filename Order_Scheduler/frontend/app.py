# Frontend - Streamlit Code
import requests
import streamlit as st

API_ENDPOINT = "http://backend:5001/schedule"

st.title("E-commerce Order Scheduler")

item_url = st.text_input("Item URL")
additional_info = st.text_input("Like Size, Quantity, etc.")
name = st.text_input("Name")
phone = st.text_input("Phone Number")
address = {
    "address": st.text_input("Address"),
    "locality": st.text_input("Locality"),
    "pincode": st.text_input("Pincode"),
    "city": st.text_input("City"),
    "state": st.text_input("State"),
    "country": st.text_input("Country")
}

order_date = st.date_input("Order Date")
order_time = st.time_input("Order Time")

# Combine date and time into a single datetime string
order_datetime = f"{order_date} {order_time}"

if st.button("Schedule Order"):
    payload = {
        "item_url": item_url,
        "additional_info": additional_info,
        "name": name,
        "phone": phone,
        "address": address,
        "order_time": order_datetime
    }
    response = requests.post(API_ENDPOINT, json=payload)
    st.write(response.text)
