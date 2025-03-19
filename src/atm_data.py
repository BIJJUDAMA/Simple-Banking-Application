import json
ACCOUNTS_FILE = "accounts.json" #Name of JSON file used to store data

def load_accounts():
    #Load accounts from JSON file, returning an empty dictionary if the file is empty or invalid
    try:
        with open(ACCOUNTS_FILE, "r") as file:
            # Check if the file has content
            if file.read().strip():
                file.seek(0)  # Go back to the beginning of the file
                return json.load(file)
            else:
                return {}  # Return an empty dictionary if the file is empty
    except (FileNotFoundError, json.JSONDecodeError):
        return {}  # Return an empty dictionary if file doesn't exist or is invalid

def save_accounts(accounts):
    # Save accounts to JSON file
    with open(ACCOUNTS_FILE, "w") as file: #Opening JSON file in write mode
        json.dump(accounts, file, indent=4)
