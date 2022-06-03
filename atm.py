class Atm(object):
    def __init__(self):
        self.pin = ''
        self.starting_balance = 0.00
        self.cash = 0.00
        self.bill_type = 0
        self.bills = 0
        self.remainder = 0
        self.remaining_balance = 0.00
    
    def get_card_number(self):
        self.pin = input("Enter your 4-digit card PIN number: ")
    
    def get_cash_transaction(self):
        print()
        print("Your card balance is $1000.")
        self.starting_balance = 1000.00
        self.cash = input("Enter the cash amount to withdraw in dollars: $")
        self.bill_type = input("Enter the bill type for the withdrawn amount (1 for $1 bills, 5 for $5 bills, etc.): ")

    def initiate_transaction(self):
        self.bills = int(float(self.cash) / float(self.bill_type))
        self.remainder = int(float(self.cash) % float(self.bill_type))
        print()
        print("You will receive", self.bills, "$" + self.bill_type, "bills and", self.remainder, "dollar bills in change.")
        print()
        self.remaining_balance = "$" + str(int(float(self.starting_balance) - float(self.cash)))
        print("Transaction complete!")
        print("Remaining balance:", self.remaining_balance)
        print("Have a good day!")

user = Atm()
user.get_card_number()
user.get_cash_transaction()
user.initiate_transaction()