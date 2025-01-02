# Travel Planner

## Overview

Travel Planner is a web application that helps users plan their itineraries by providing information about flights and hotels. The application uses AI to search for real-time data and present the top options based on user queries.

## Features

- **AI-Powered Search**: Utilize AI to search for flights and hotels based on natural language queries.
- **Real-Time Data**: Get the latest information on flights and hotels.
- **User-Friendly Interface**: Easy-to-use interface for planning your travel itinerary.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/travel-planner.git
    cd travel-planner
    ```

2. Install dependencies:
    ```sh
    npm install
    ```

3. Run the development server:
    ```sh
    npm run dev
    ```

## Usage

1. Open your browser and navigate to `http://localhost:3000`.
2. Enter your travel queries in the chat interface.
3. View the top flight and hotel options based on your input.

## Environment Variables

Create a `.env.local` file in the root directory and add the following variables:

```plaintext
OPENAI_API_KEY = sk-***********
RACCOON_PASSCODE = ************
RACCOON_SECRET_KEY = **********
````