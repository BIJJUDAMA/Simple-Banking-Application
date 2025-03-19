import tkinter as tk # Import the tkinter module for GUI applications
from atm_account import account_creation_screen, validate_account_screen # Import account creation and validation screen functions from atm_account module

def main_screen(root=None):
    #Main screen that asks if the user has an account
    if root:
        root.destroy()  # Close existing window 
    root = tk.Tk() # Create a new Tkinter window 
    root.title("ATM System")  # Set the title of the window
    
    #Displays Welcome label and padding for better space
    tk.Label(root, text="Welcome to the ATM System!", font=("Helvetica", 16)).pack(pady=20) 

    #Displays yes/no options for user to choose whether they have an account or not
    tk.Label(root, text="Do you have an existing account?", font=("Helvetica", 12)).pack(pady=5)

    #Following two lines are the options for button for the user to choose from
    tk.Button(root, text="Yes", command=lambda: validate_account_screen(root, main_screen)).pack(pady=5) 
    tk.Button(root, text="No", command=lambda: account_creation_screen(root, main_screen)).pack(pady=5)
    #Lambda is a small anonmyous function used inline here 
    #It calls validate_account_screen if the user clicks on yes 
    #It calls account_creation_screen if the user clicks on no

    root.mainloop() #Runs Tkinter main loop which constantly checks for user interaction

if __name__ == "__main__":
    main_screen() #Calls the main function to to start
