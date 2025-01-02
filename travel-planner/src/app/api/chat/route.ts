import { openai } from '@ai-sdk/openai';
import { streamText, tool } from 'ai';
import { z } from 'zod';

import { searchFlights, searchHotels } from './raccoon';

export const maxDuration = 300;

/**
 * The POST method for the chat API.
 * @param req The request object
 * @returns Streamed response
 */

export async function POST(req: Request) {
  const { messages } = await req.json();

  const result = streamText({
    model: openai('gpt-4o'),
    messages,

    // Define the tools that the user can use. We use our custom tools where we use Raccoon AI to search for realtime data of hotels and flights.

    tools: {
      hotels: tool({
        description: 'Get available hotels from makemytrip by a query in natural language. Just enter the city name and preferred dates in natural language. and we will return the top 5 hotels.',
        parameters: z.object({
          query: z.string().describe('The query to search for hotels with additional information if user wants to provide'),
        }),
        execute: async ({ query }) => {
            return await searchHotels(query);
        }
      }),

      flights: tool({
        description: 'Get available flights from google flights by a query in natural language. Just enter the source, destination city names, one-way or round trip preference and preferred dates in natural language. and we will return the top 5 flights.',
        parameters: z.object({
          query: z.string().describe('The query to search for flights with additional information if user wants to provide'),
        }),
        execute: async ({ query }) => {
            return await searchFlights(query);
        }
      }),
    },
  });

  return result.toDataStreamResponse();
}