class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = list()

    def deposit(self, dep_amount, description=''):
        '''
        A method that accepts an amount and description. If no description is given, it defaults to an empty string.
        Should append to the ledger in the form {'amount': amount, 'description': description}
        '''
        self.ledger.append({'amount': dep_amount, 'description': description})

    def withdraw(self, with_amount, description=''):
        '''
        A method that accepts an amount and description. If no description is given, it defaults to an empty string.
        Converts the amount into a negative. If there are not enough funds, nothing should be added
        Should append to the ledger in the form {'amount': amount, 'description': description}
        Returns True if the withdrawal takes place, otherwise false
        '''
        if self.check_funds(with_amount):
            self.ledger.append({'amount': -with_amount, 'description': description})
            return True
        return False

    def get_balance(self):
        '''
        Adds all the deposits and withdrawals to find the total amount available for the given category
        '''
        total = 0
        for item in self.ledger:
            total += item['amount']
        return total

    def transfer(self, amount, category):
        '''
        Accepts an amount and another budget category as arguments. Should add a withdrawal with the amount
        and the description 'Transfer to [Destination Category]'. Then should add a deposit to the other category
        with the amount and the description 'Transfer from [Source Category]'
        If not enough funds, nothing is done to either ledger. Returns True if the transfer took place, False otherwise
        '''
        if self.check_funds(amount):
            self.withdraw(amount, f'Transfer to {category.name}')
            category.deposit(amount, f'Transfer from {self.name}')
            return True
        else:
            return False

    def check_funds(self, amount):
        '''
        Method that accepts an amount as an argument. Returns False if the amount is greater than the balance of the
        budget category, and True otherwise
        '''
        if self.get_balance() >= amount:
            return True
        else:
            return False



def create_spend_chart(categories):
    pass