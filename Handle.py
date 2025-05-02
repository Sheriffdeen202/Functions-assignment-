

def atm():
    balance = 1000  # Starting balance

    try:
        card_inserted = input("Insert card (type 'yes' to proceed): ").strip().lower()
        if card_inserted != 'yes':
            raise Exception("Card not inserted properly.")

        pin = int(input("Enter your 4-digit PIN: "))
        if pin != 1234:
            raise ValueError("Incorrect PIN.")

        amount = int(input("Enter amount to withdraw: "))
        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")
        if amount > balance:
            raise ValueError("Insufficient funds.")

        print(f"Please collect your cash: {amount}")
        balance -= amount
        print(f"Remaining balance: {balance}")

    except ValueError as ve:
        print("Value Error:", ve)
    except Exception as e:
        print("Error:", e)
    finally:
        print("Thank you for using the ATM.")

# Run the ATM simulation
atm()