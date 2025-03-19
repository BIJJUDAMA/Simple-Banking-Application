import random

def generate_card_number():
    # Generate a unique 8-digit card number
    return str(random.randint(10000000, 99999999))
