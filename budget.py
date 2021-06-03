class Category:
    def __init__(self, category):
        self.category = category
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
        pass

    def transfer(self, amount, category):
        pass

    def check_funds(self, amount):
        pass



def create_spend_chart(categories):
    pass