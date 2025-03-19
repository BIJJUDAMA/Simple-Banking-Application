import tkinter as tk

def main_menu_screen(root, card_number, withdraw_callback, deposit_callback, statement_callback):
       
    #card_number: The card number of the user, passed for transaction identification.
    #withdraw_callback: A function to handle the withdrawal process.
    #deposit_callback: A function to handle the deposit process.
    #statement_callback: A function to handle the mini statement request.

    # Main menu screen to select a transaction
    root.destroy()
    new_window = tk.Tk()
    new_window.title("Main Menu")
    tk.Label(new_window, text="Main Menu", font=("Helvetica", 16)).pack(pady=10)
    tk.Button(new_window, text="Withdraw", command=lambda: withdraw_callback(new_window, card_number, main_menu_screen)).pack(pady=5)
    tk.Button(new_window, text="Deposit", command=lambda: deposit_callback(new_window, card_number, main_menu_screen)).pack(pady=5)
    tk.Button(new_window, text="Mini Statement", command=lambda: statement_callback(new_window, card_number, main_menu_screen)).pack(pady=5)
    #Lambda is used inline here to pass arguments for the callback functions
    tk.Button(new_window, text="Exit", command=new_window.destroy).pack(pady=5)
