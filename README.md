
# Negotiation Chatbot

## Overview
This project is a negotiation chatbot that simulates a price negotiation between a customer and a supplier. The chatbot is built using Flask and integrates with OpenAI's GPT-3 model to handle conversational interactions.

## Features
- The user can initiate a negotiation for a product price.
- The chatbot will respond with a counteroffer or accept/reject the offer based on predefined pricing logic.
- Integration with OpenAI API for natural language responses.

## Setup

### Requirements
- Python 3.x
- Flask
- OpenAI Python client

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Running the App
1. Make sure you have set your OpenAI API key in `chatbot_response.py`.
2. Run the Flask app:
```bash
python app.py
```
3. Use Postman or curl to send requests to the API.

## API Endpoints
- `GET /start-negotiation`: Starts the negotiation with an initial message.
- `POST /negotiate`: Submit the user's offer and get a counteroffer or chatbot response.
