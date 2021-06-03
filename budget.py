class Category:
    def __init__(self, category, ledger=[]):
        self.category = category
        self.ledger = ledger

    def deposit(self, amount, description):
        pass

    def withdraw(self, amount, description):
        pass

    def get_balance(self):
        pass

    def transfer(self, amount, category):
        pass

    def check_funds(self, amount):
        pass



def create_spend_chart(categories):