import random

def get_ticket_price(destination: str) -> dict:
    """
    Implementation: returns a random ticket price for the given city.
    """
    price = random.randint(100, 1000)
    return {"destination": destination, "price_usd": price}
