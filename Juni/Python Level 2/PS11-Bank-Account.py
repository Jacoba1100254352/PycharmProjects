accounts = {"janesmith": "secret123", "bobsmith": "programm3r"}
balances = {"janesmith": 0, "bobsmith": 0}

while True:

    # login functionality
    while True:
        print("Welcome to the bank! Please log in.")
        username = input("Username: ")
        password = input("Password: ")
        if username not in accounts:
            print("\nWe don't recognize your username. Please try again.\n")
        elif password != accounts[username]:
            print("\nYour password is incorrect. Please try again.\n")
        else:
            break

    while True:
        numChoice = input("\nWelcome " + username + "! You currently have $" + str(balances[
                                                                                       username]) + " in your account. What would you like to do?\n\t1. Make a deposit\n\t2. Make a withdrawal\n\t3. Change your password\n\t4. Log out\n")

        if numChoice == "1":
            deposit = input("How much would you like to deposit? ")
            balances[username] += int(deposit)
        elif numChoice == "2":
            withdraw = input("How much would you like to withdraw? ")
            balances[username] -= int(withdraw)
        elif numChoice == "3":
            oldPassword = input("To change your password, please type in your old password:")
            if oldPassword == accounts[username]:
                newPassword = input("Please type in your new password:")
                accounts[username] = newPassword
                print("\nYour password has been changed successfully!")
            else:
                print("\nYour old password does not match the password in our records.")
        elif numChoice == "4":
            break
