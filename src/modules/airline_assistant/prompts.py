# System prompt for the assistant
system_message = (
    "You are a helpful Airline AI Assistant. "
    "You can answer general travel questions and book flights by "
    "calling the function get_ticket_price when asked about ticket prices."
)

# Describe the function to the model
function_spec = {
    "name": "get_ticket_price",
    "description": "Get the ticket price for a one-way flight to the given destination city.",
    "parameters": {
        "type": "object",
        "properties": {
            "destination": {
                "type": "string",
                "description": "The city you want to fly to"
            }
        },
        "required": ["destination"]
    }
}
