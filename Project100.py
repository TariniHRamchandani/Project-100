class BankATM:
    def_init_(self):

        #FUNCTION FOR BALENCE
self.balance=0
print('Your Account is Created.')
def deposit(self):
    #We enter the amount to be deposited
amount=int(input('Enter the amount to deposit:'))

self.balance+=amount
#this function adds the balence to the oringinal amount in the account.Thanks to print it also prints the value.
print('Your New Balance =%d' %self.balance)

#This function will help the user to withdraw the money from the account.
def withdraw(self):
amount=int(input('Enter the amount to withdraw:'))
#this will help us to enter the amount to withdraw.
if(amount>self.balance):
    #if the user has 4000 rupees in the bank and wants to take out 5000 or an amount greater then 4000, the program will print the message line 21.
print('Insufficient Balance!')
#otherwise it will withdraw the amount required and print the remaining balence
else:
self.balance-=amount
print('Your Remaining Balance =%d' %self.balance)
def enquiry(self):
print('Your Balance =%d' %self.balance)
account= Account()
account.deposit()
account.withdraw()
account.enquiry()