# Backend - Scheduler Code
from datetime import datetime

from celery import Celery

from raccoon.run import RaccoonActionModel

# Celery Configuration
app = Celery('order_scheduler', broker='amqp://admin:mypass@rabbit:5672', backend='rpc://')


# Celery task to place order
@app.task
def place_order(item_url, additional_info, name, phone, address):
    query = f"""Order this {additional_info} from the link below: \n Delivery Address: {address.get("address")}, {address.get("locality")}, {address.get("pincode")}, {address.get("city")}, {address.get("state")}, {address.get("country")}. Payment method: Cash on Delivery (COD). Name : {name}, Phone number {phone} \n Scroll if 'Buy Now' or 'Add to Bag' or 'COD' options aren't immediately visible."""

    response = RaccoonActionModel().pipeline(query=query, app_url=item_url, stream=True)
    return response


# Function to schedule an order
def schedule_order(item_url, additional_info, name, phone, address, order_time):
    now = datetime.now()
    schedule_time = datetime.strptime(order_time, "%Y-%m-%d %H:%M:%S")
    delay = (schedule_time - now).total_seconds()

    if delay > 0:
        place_order.apply_async((item_url, additional_info, name, phone, address), countdown=delay)
        return f"Order scheduled for {name} at {order_time}"
    else:
        return "Order time must be in the future."
