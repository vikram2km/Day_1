import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class BankAccount:
    def __init__(self,name,balance):
        self._name=name
        if balance < 0:
            raise ValueError("Invalid starting balance")
        self._balance=balance
        logging.info(f"Hi {self._name}, your account created with the initial deposit of {self._balance}")
    
    @property
    def balance(self):
        logging.exception('Restricted Access')
        raise
    
    def deposit(self,amount):
        if amount < 0:
            raise ValueError("Invalid starting balance")
        self._balance=self._balance+amount
        logging.info(f"Hi {self._name}, deposit of {self._balance} amount is successful")
    def withdraw(self,amount):
        if amount>self._balance:
            logging.info(f"Hi {self._name}, amount specified is more than the balance")
        else:
            self._balance=self._balance-amount
            logging.info(f"Hi {self._name}, withdraw request of {amount} has been processed")
    def get_balance(self):
        logging.info(f"Hi {self._name}, your current balance is {self._balance}")
        
def main():
    ch1=BankAccount('Vikram',0)
    ch2=BankAccount('Varun',500)
    ch1.deposit(500)
    ch1.get_balance()
    ch1.withdraw(600)
    ch1.withdraw(500)
    ch1.get_balance()
    ch2.get_balance()
    
    
if __name__=="__main__":
    main()