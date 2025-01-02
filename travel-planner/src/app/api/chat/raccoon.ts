
const baseUrl = 'https://api.flyingraccoon.tech/lam/extract'; // Base URL for the Flying Raccoon API.

/**
 * Extracts data from the Flying Raccoon API.
 * 
 * @async
 * @function extract
 * @param {Object} body - The request payload.
 * @param {string} body.query - The query string.
 * @param {string} body.app_url - The application URL.
 * @param {Object} body.schema - The schema object.
 * @param {number} body.max_count - The maximum count of items to extract.
 * @returns {Promise<Object[]>} The extracted items.
 * @throws {Error} If the extraction fails.
 */
const extract = async (body: {
    query: string;
    app_url: string;
    schema: object;
    max_count: number;
}) => {
    const response = await fetch(baseUrl, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'raccoon-passcode': process.env.RACCOON_PASSCODE ?? '',
            'secret-key': process.env.RACCOON_SECRET_KEY ?? '',
            'platform': 'web',
        },
        body: JSON.stringify(body),
    });

    if (!response.ok) {
        throw new Error(`Failed to extract: ${response.statusText}`);
    }

    const data = await response.json();
    const items = data[data.length - 1].data;
    console.log(items);

    return items;
}

/**
 * Searches for hotels using the Flying Raccoon API.
 * 
 * @async
 * @function searchHotels
 * @param {string} query - The search query.
 * @returns {Promise<Object[]>} The list of hotels.
 * @throws {Error} If the search fails.
 */
export const searchHotels = async (query: string) => {
    const hotels = await extract({
        query: query + '\n source and destination city must be entered in the textboxes, correctly before searching or exploring!',
        app_url: 'https://www.google.com/travel/hotels',
        schema: {
            name: 'name',
            address: 'address',
            rating: 'rating',
            price: 'price',
        },
        max_count: 5,
    });

    return hotels;
}

/**
 * Searches for flights using the Flying Raccoon API.
 * 
 * @async
 * @function searchFlights
 * @param {string} query - The search query.
 * @returns {Promise<Object[]>} The list of flights.
 * @throws {Error} If the search fails.
 */
export const searchFlights = async (query: string) => {
    const flights = await extract({
        query: query + '\n Only put the ',
        app_url: 'https://www.google.com/travel/flights',
        schema: {
            name: 'name of the airline',
            departure: 'departure time',
            arrival: 'arrival time',
            price: 'price of the ticket',
        },
        max_count: 5,
    });

    return flights;
}

