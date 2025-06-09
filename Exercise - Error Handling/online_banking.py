class MoneyNotEnoughError(Exception):
    pass


class PINCodeError(Exception):
    pass


class UnderageTransactionError(Exception):
    pass


class MoneyIsNegativeError(Exception):
    pass


LEGAL_AGE = 18
acc_info = input().split(", ")
my_pin_code, balance, age = int(acc_info[0]), float(acc_info[1]), int(acc_info[2])

while True:
    command = input()
    if command == "End":
        break

    command_type = command.split("#")
    if command_type[0] == "Send Money":
        money, pin_code = float(command_type[1]), int(command_type[2])
        if money > balance:
            raise MoneyNotEnoughError("Insufficient funds for the requested transaction")
        if pin_code != my_pin_code:
            raise PINCodeError("Invalid PIN code")
        if age < LEGAL_AGE:
            raise UnderageTransactionError("You must be 18 years or older to perform online transactions")

        balance -= money
        print(f"Successfully sent {money:.2f} money to a friend")
        print(f"There is {balance:.2f} money left in the bank account")

    elif command_type[0] == "Receive Money":
        money = float(command_type[1])

        if money < 0:
            raise MoneyIsNegativeError("The amount of money cannot be a negative number")

        total_received = money / 2
        balance += total_received
        print(f"{total_received:.2f} money went straight into the bank account")
