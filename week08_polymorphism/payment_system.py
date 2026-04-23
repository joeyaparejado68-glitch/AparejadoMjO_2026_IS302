class Transaction:
    def process(self):
        print("Handling transaction")

class CashMode(Transaction):
    def process(self):
        print("Transaction completed with cash")

class CardMode(Transaction):
    def process(self):
        print("Transaction completed with card")

payment_list = [CashMode(), CardMode()]

for item in payment_list:
    item.process()