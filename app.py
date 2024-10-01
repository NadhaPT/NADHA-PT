
from flask import Flask, jsonify, request
from pricing_logic import get_counteroffer
from chatbot_response import get_chatbot_response

app = Flask(__name__)

@app.route('/start-negotiation', methods=['GET'])
def start_negotiation():
    initial_message = "Welcome! The initial product price is $100. Please make an offer."
    return jsonify({"message": initial_message})

@app.route('/negotiate', methods=['POST'])
def negotiate():
    user_offer = request.json.get("user_offer")
    counteroffer = get_counteroffer(user_offer)

    if counteroffer == "accepted":
        return jsonify({"message": f"Your offer of ${user_offer} is accepted!"})
    else:
        bot_response = get_chatbot_response(f"The user offers ${user_offer}, counter with ${counteroffer}.")
        return jsonify({"message": f"Your offer of ${user_offer} is too low. Counteroffer: ${counteroffer}.", "chatbot_response": bot_response})

if __name__ == '__main__':
    app.run(debug=True)
