import tkinter as tk
from atm_data import load_accounts, save_accounts

def update_account(card_number, account_data):
    # Update account details in the JSON file
    accounts = load_accounts()
    accounts[card_number] = account_data
    save_accounts(accounts)

def main_menu_screen(root, card_number, main_screen_callback):
    # Main menu screen to select a transaction
    root.destroy()
    new_window = tk.Tk()
    new_window.title("Main Menu")
    tk.Label(new_window, text="Main Menu", font=("Helvetica", 16)).pack(pady=10)
    tk.Button(new_window, text="Withdraw", command=lambda: withdraw_screen(new_window, card_number, main_screen_callback)).pack(pady=5)
    tk.Button(new_window, text="Deposit", command=lambda: deposit_screen(new_window, card_number, main_screen_callback)).pack(pady=5)
    tk.Button(new_window, text="Mini Statement", command=lambda: mini_statement_screen(new_window, card_number, main_screen_callback)).pack(pady=5)
    tk.Button(new_window, text="Exit", command=main_screen_callback).pack(pady=5)  
    # Lambda is used inline here to pass arguments for the functions

def withdraw_screen(root, card_number, main_screen_callback):
    root.destroy()
    new_window = tk.Tk()
    new_window.title("Withdraw")
    account = load_accounts().get(card_number)
    min_balance = 2000.0
    tk.Label(new_window, text=f"Current balance: {account['balance']}").pack()
    tk.Label(new_window, text=f"Max withdrawal: {account['balance'] - min_balance}").pack()
    amount_entry = tk.Entry(new_window)
    amount_entry.pack()

    def withdraw():
        amount = float(amount_entry.get())
        if amount > account['balance'] - min_balance:
            tk.Label(new_window, text="Insufficient balance.", fg="red").pack()
        else:
            account['balance'] -= amount
            account['transactions'].append(f"Withdrawn: {amount}")
            update_account(card_number, account)
            tk.Label(new_window, text="Withdrawal successful!", fg="green").pack()
            # Return to main menu 
            new_window.after(2000, lambda: main_menu_screen(new_window, card_number, main_screen_callback))

    withdraw_button = tk.Button(new_window, text="Withdraw", command=withdraw)
    withdraw_button.pack(pady=10)
    tk.Button(new_window, text="Back to Main Menu", command=lambda: main_menu_screen(new_window, card_number, main_screen_callback)).pack(pady=5)

def deposit_screen(root, card_number, main_screen_callback):
    root.destroy()
    new_window = tk.Tk()
    new_window.title("Deposit")
    tk.Label(new_window, text="Enter amount to deposit:").pack()
    amount_entry = tk.Entry(new_window)
    amount_entry.pack()

    def deposit():
        amount = float(amount_entry.get())
        account = load_accounts().get(card_number)
        account['balance'] += amount
        account['transactions'].append(f"Deposited: {amount}")
        update_account(card_number, account)
        tk.Label(new_window, text="Deposit successful!", fg="green").pack()
        new_window.after(2000, lambda: main_menu_screen(new_window, card_number, main_screen_callback))

    deposit_button = tk.Button(new_window, text="Deposit", command=deposit)
    deposit_button.pack(pady=10)
    tk.Button(new_window, text="Back to Main Menu", command=lambda: main_menu_screen(new_window, card_number, main_screen_callback)).pack(pady=5)

def mini_statement_screen(root, card_number, main_screen_callback):
    root.destroy()
    new_window = tk.Tk()
    new_window.title("Mini Statement")
    account = load_accounts().get(card_number)
    tk.Label(new_window, text="--- Mini Statement ---", font=("Helvetica", 16)).pack()
    for transaction in account["transactions"]:
        tk.Label(new_window, text=transaction).pack()
    tk.Label(new_window, text="----------------------").pack()

    tk.Button(new_window, text="Back to Main Menu", command=lambda: main_menu_screen(new_window, card_number, main_screen_callback)).pack(pady=5)
