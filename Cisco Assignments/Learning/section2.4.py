#variables are used to store data for something longer
num = 67
#this stores "num" as 67, and can be used later in the code to represent 67
name = "Christopher"
account_balance = 1000.50
print(num, account_balance, name)
#var is the python version, it is a string and can be used to represent the version of python being used
var = "3.8.5"
print("Python version: " + var)
#you can use + to combine strings, but you cannot use + to combine strings and numbers, you must convert the number to a string first
print("My account balance is: " + str(account_balance))
#operator plus an euals sign calulates everything on the right then does the operation on the left
#EX: += *= -= /=
nin = 3
nin += 2
print(nin + 2)

hi = 3
hi *= 2 +5
print(hi ) #printed as 21 because 2+5 is 7 and 3*7 is 21, 