
BASE_PRICE = 100
MIN_ACCEPTABLE_PRICE = 80

def get_counteroffer(user_offer):
    try:
        offer = float(user_offer)
        if offer >= MIN_ACCEPTABLE_PRICE:
            return "accepted"
        elif offer >= 70:
            return offer + 10
        else:
            return BASE_PRICE
    except ValueError:
        return "invalid"
