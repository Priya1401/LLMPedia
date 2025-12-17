import os
from serpapi import GoogleSearch

def get_ticket_price(destination: str, origin: str = "JFK") -> dict:
    """
    Returns the real-time cheapest ticket price.
    IMPORTANT: 'destination' and 'origin' MUST be 3-letter IATA airport codes (e.g. 'LHR', 'JFK', 'BOS', 'ATL').
    Do not use city names like 'London' or 'Atlanta'.
    Defaults origin to 'JFK' if not specified.
    """
    api_key = os.getenv("SERPAPI_API_KEY")
    if not api_key:
        return {"error": "SERPAPI_API_KEY not found in .env"}

    from datetime import datetime, timedelta
    tomorrow = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")

    params = {
        "engine": "google_flights",
        "departure_id": origin, 
        "arrival_id": destination, 
        "outbound_date": tomorrow,
        "currency": "USD",
        "hl": "en",
        "type": "2", # One-way ticket
        "api_key": api_key
    }

    try:
        search = GoogleSearch(params)
        results = search.get_dict()
        
        # Parse the first 'best_flights' option
        if "best_flights" in results and len(results["best_flights"]) > 0:
            flight = results["best_flights"][0]
            price = flight.get("price", "Unknown")
            return {
                "destination": destination, 
                "price": price, 
                "airline": flight["flights"][0]["airline"],
                "duration": flight["total_duration"]
            }
        else:
            return {"error": "No flights found for parameters."}
            
    except Exception as e:
        return {"error": f"API Search failed: {str(e)}"}
