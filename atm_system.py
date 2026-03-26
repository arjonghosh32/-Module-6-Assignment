 # ------------------2. Initial Setup ------------
initial_balance = 1000
transactions = [] 
total_Deposit = 0
total_Withdraw = 0


# -------------------1. Main Menu (Must use while loop)-----------------

while True:
    print("\n===== ATM MENU =====")

    print("1. Check Balance.")
    print("2. Deposit Amount.")
    print("3. Withdraw Amount.")
    print("4. Transaction History.")
    print("5. Exit\n")

    Option = float(input("\nEnter choice: "))


# --------------------3. Check Balance (For Option 1)--------------------
    if Option == 1:
        print("\nYour current balance is :",initial_balance)
        
# ----------------------4. Deposit (For Option 2)-------------------------
    elif Option == 2:
        Amount = float(input("\nEnter your deposit amount :"))
        if Amount > 0:
            initial_balance = initial_balance + Amount
            total_Deposit = total_Deposit + Amount
            transactions.append(f"Deposited: {Amount}")
            print("Deposit successful!")
            print("New balance :", initial_balance)
        else:
            print("Invalid amount")

# -----------------------5. Withdraw (For Option 3)-------------------------
    elif Option == 3:
        Withdraw = float(input("Enter amount to withdraw: "))
        if Withdraw <= initial_balance and Withdraw > 0:
            initial_balance = initial_balance - Withdraw
            total_Withdraw = total_Withdraw + Withdraw
            transactions.append(f"Withdrawn: {Withdraw}")
            print("Withdrawal successful!")
            print("Remaining balance:",initial_balance)
        elif Withdraw > initial_balance:
            print(" Insufficient balance!")
        else:
            print("invalid amount!")
    
# -------------------------6. Transaction History (For Option 4)-------------

    elif Option == 4:
        print("\n--- Transaction History ---")
        if len(transactions) == 0:
            print("No transactions yet.")
        else:
            for i in transactions:
                print("-",i)
                

                print()

        print("Total-Deposit : ",total_Deposit)
        print("total-Withdraw :",total_Withdraw)
        
# ---------------------------8. Exit (For Option 5)-----------------------------

    elif Option == 5:
        print("Thank you for using ATM. Goodbye!")
        break
    else:
        print("Invalid choice! Please select between 1-5.")
   