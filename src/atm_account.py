import tkinter as tk
from atm_data import load_accounts, save_accounts # To load and save account data
from atm_utils import generate_card_number # To generate a unique card number for new accounts
from atm_transactions import main_menu_screen  # To navigate to the main menu after validation

def account_creation_screen(root, main_screen):
    #Account creation screen gathers user details and set up a new account
    root.destroy()  
    new_window = tk.Tk()
    new_window.title("Create Account")
    tk.Label(new_window, text="Create a New Account", font=("Helvetica", 16)).pack(pady=10)

    #Input field for user details
    name_label = tk.Label(new_window, text="Name:")
    name_label.pack()
    name_entry = tk.Entry(new_window)
    name_entry.pack() # Use the pack geometry manager to add position the label in the window                
    
    email_label = tk.Label(new_window, text="Email ID:")
    email_label.pack()
    email_entry = tk.Entry(new_window)
    email_entry.pack()
    
    phone_label = tk.Label(new_window, text="Phone Number:")
    phone_label.pack()
    phone_entry = tk.Entry(new_window)
    phone_entry.pack()
    
    pin_label = tk.Label(new_window, text="Create a 4-digit PIN:")
    pin_label.pack()
    pin_entry = tk.Entry(new_window, show="*")
    pin_entry.pack()

    def create_account():
        accounts = load_accounts() # Load existing accounts from accounts.json
        # Getting user input
        name = name_entry.get()
        email = email_entry.get()
        phone = phone_entry.get()
        pin = pin_entry.get()

        if len(pin) == 4 and pin.isdigit(): #Checking if the pin is 4 digits long and is a digit
            card_number = generate_card_number() #Generates a unique card number
            accounts[card_number] = {           # Creating a nested dictionary with card number as key and user details as values
                "name": name,
                "email": email,
                "phone": phone,
                "pin": int(pin),
                "balance": 100000.0,  # Default balance
                "transactions": []    # Empty transaction history since account is being created
            }
            save_accounts(accounts) # Saving the accounts data
            tk.Label(new_window, text=f"Account created! Your card number is {card_number}", fg="green").pack()
            new_window.after(3000, lambda: [new_window.destroy(), main_screen()])
        else:
            # Error message for wrong pin
            tk.Label(new_window, text="Invalid PIN! Please enter exactly 4 digits.", fg="red").pack()

    create_button = tk.Button(new_window, text="Create Account", command=create_account)
    create_button.pack(pady=10)

def validate_account_screen(root, main_screen):
    # Screen to validate an existing account by card number and PIN
    root.destroy()  
    validation_window = tk.Tk()
    validation_window.title("Validate Account")
    
    # Input fields for card number and PIN
    tk.Label(validation_window, text="Enter Card Number:", font=("Helvetica", 12)).pack(pady=5)
    card_entry = tk.Entry(validation_window)
    card_entry.pack()
    tk.Label(validation_window, text="Enter PIN:", font=("Helvetica", 12)).pack(pady=5)
    pin_entry = tk.Entry(validation_window, show="*")
    pin_entry.pack()

    def validate_account():
        # Checks the entered card number and pin against stored account data
        accounts = load_accounts()
        card_number = card_entry.get()
        pin = pin_entry.get()
        
        if card_number in accounts and accounts[card_number]["pin"] == int(pin):
            tk.Label(validation_window, text="Login successful!", fg="green").pack()
            validation_window.after(
                1500,
                lambda: main_menu_screen(
                    validation_window, card_number, main_screen  # Pass main_screen as a callback
                )
            )  # Navigate to main menu after login
        else:
            tk.Label(validation_window, text="Invalid card number or PIN. Try again.", fg="red").pack()

    validate_button = tk.Button(validation_window, text="Login", command=validate_account)
    validate_button.pack(pady=10)
    
    # Option to go back to the main screen
    tk.Button(validation_window, text="Back to Main", command=lambda: [validation_window.destroy(), main_screen()]).pack(pady=5)
