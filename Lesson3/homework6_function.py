balance=0
def deposit(cash):
    global balance
    balance+=cash
    return balance
def withdraw(cash):
    global balance
    balance=balance-cash
    return balance

while True:
    num= int(input("Enter amount of deposit:"))
    if num>0:
        print("The remaining balance is:", deposit(num))
        break

while True:
    num= int(input("Enter amount of withdraw:"))
    if num > balance:
        print("The amount you enter is greater than your remaining balance. Please Enter it again!")
    elif num>0:
        print("The remaining balance is:", withdraw(num))
        break