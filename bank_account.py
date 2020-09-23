import random

# possible_notes=[1,5,10,20,50,100]
atm_notes = {
    100:1000,
    50:1000,
    20:1000,
    10:1000,
    5:1000,
    1:1000
}
deposit_notes={
    100:10,
    50:5,
}

class Account_holder():
    def __init__(self,name):
        self.name=name

class Money():
    def __init__(self,value,count):
        self.value=value
        self.count=count

class Bank_account(Account_holder):
    def __init__(self,balance,name):
        Account_holder.__init__(self,name)
        self.balance=balance
    def credit(self,amount):
        self.balance+=amount
    def is_enough(self,amount):
        return self.balance>amount
    def debit(self,amount):
        if self.is_enough(amount):
            self.balance-=amount
        else:
            print('Insufficient balance to make transaction')

class ATM():
    def __init__(self,location,balance_notes={}):
        self.location = location
        self.balance_notes=balance_notes
    def deposit(self,notes):
        for denomination in notes:
            self.balance_notes[denomination]+=notes[denomination]
    def atm_balance(self):
        balance=0
        for denomination, count in self.balance_notes.items():
            balance+=denomination*count
        return balance
    def is_enough(self,amount):
        return self.atm_balance()>amount
    def withdraw(self,amount):
        if self.is_enough(amount):
            for denomination in self.balance_notes:
                if amount % denomination == 0:
                    self.balance_notes[denomination]-= amount//denomination
                    amount-=denomination*amount//denomination
        else:
            print('Sorry insufficient atm balance')

class Bank():
    def __init__(self,bank_name):
        self.bank_name=bank_name
        self.accounts = {}
        self.atms={}
    def add_acount(self,balance,name):
        self.accounts[name]=Bank_account(balance,name)
    def add_atm(self,location,balance_notes):
        self.atms[location]=ATM(location,balance_notes)
    def deposit(self,name,location,deposit_notes):
        amount = 0
        for denomination,count in deposit_notes.items():
            amount+=denomination*count
        self.accounts[name].credit(amount)
        self.atms[location].deposit(deposit_notes)
    def withdraw(self,name,location,amount):
        if self.accounts[name].is_enough(amount) and self.atms[location].is_enough(amount):
            self.accounts[name].debit(amount)
            self.atms[location].withdraw(amount)

maybank = Bank("maybank")
maybank.add_acount(100000,'kesihain')
maybank.add_atm('damansara',atm_notes)
print(maybank.atms['damansara'].atm_balance())
print('')
maybank.withdraw('kesihain','damansara',3000)
print('Atm balance: ',maybank.atms['damansara'].atm_balance())
print('Atm notes left: ',maybank.atms['damansara'].balance_notes)
print('Bank balance: ',maybank.accounts['kesihain'].balance)
maybank.deposit('kesihain','damansara',deposit_notes)
print('')
print('Atm balance: ',maybank.atms['damansara'].atm_balance())
print('Atm notes left: ',maybank.atms['damansara'].balance_notes)
print('Bank balance: ',maybank.accounts['kesihain'].balance)