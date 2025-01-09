# E-commerce Order Scheduler

This project is an E-commerce Order Scheduler built using FastAPI for the backend and Streamlit for the frontend. It
allows users to schedule orders by providing item details and delivery information.

## Table of Contents

- [Technologies Used](#technologies-used)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)

## Technologies Used

- **Frontend**: Streamlit
- **Backend**: FastAPI
- **Task Queue**: Celery
- **Message Broker**: RabbitMQ
- **Database**: PostgresSQL (implied by `libpq-dev` in Dockerfile)
- **Environment Management**: Python Dotenv

## Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Flying-Raccoon-AI/raccoon-quickstart.git
   cd Order_Scheduler
   ```

2. **Create a `.env` file** in the root directory and add the necessary environment variables:
   ```
   RACCOON_BASE_URL=<your_raccoon_base_url>
   RACCOON_SECRET_KEY=<your_secret_key>
   RACCOON_PASSCODE=<your_passcode>
   ```

3. **run application using virtual environments**:
   ```bash
    cd frontend
    python3 -m venv venv
    pip install -r requirements.txt
   
    cd backend
    python3 -m venv venv
    pip install -r requirements.txt
   ```
4. **(Optional) Build and run the Docker containers**:
   ```bash
   docker-compose up --build
   ```

5. Access the frontend at `http://localhost:5000` and the backend API at `http://localhost:5001`.

## Usage

1. Open the application in your web browser.
2. Fill in the required fields:
    - Item URL
    - Name
    - Phone Number
    - Address (including locality, pincode, city, state, and country)
    - Order Time (in the format YYYY-MM-DD HH:MM:SS)
3. Click on "Schedule Order" to submit your order.

## API Endpoints

### Schedule Order

- **Endpoint**: `/schedule`
- **Method**: `POST`
- **Request Body**:
  ```json
  {
    "item_url": "string",
    "name": "string",
    "phone": "string",
    "address": {
      "address": "string",
      "locality": "string",
      "pincode": "string",
      "city": "string",
      "state": "string",
      "country": "string"
    },
    "order_time": "string"
  }
  ```

- **Response**:
    - Success: `{ "status_code": 200, "message": "Order placed successfully" }`
    - Failure: `{ "status_code": <code>, "message": "Failed to process the request" }`
