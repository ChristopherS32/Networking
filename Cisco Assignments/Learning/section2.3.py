# + // addition
# - // subtraction
# * // multiplication
# / // division
# // // floor division
# % // modulo
# ** // exponentiation
# if a least one argument is a float, the result will be a float
print(2**3) #this will return 8 because 2^3 is 8
print(2**3.0) #this will return 8.0 because 2^3 is 8 and one of the arguments is a float
#same for *(multiplication)
#divison is a little different, if both arguments are integers, the result will be a float
print(2*3) #this will return 6 because 2*3 is 6
print(2*3.0) #this will return 6.0 because 2*3 is 6 and one of the arguments is a float
print(6/3) #this will return 2.0 because 6/3 is 2.0
print(6/3.0) #this will return 2.0 because 6/3 is 2.0
#// divides and rounds to the lower number, arguments are the same as exponentiation and multiplication
print(6//4) #this will return 1 because 6//4 is 1.5, rounded down to 1
# % returns the remainder of a division, arguments are the same as exponentiation and multiplication also
#  called modulo
print(6%4) #this will return 2 because 6%4 is 2, the remainder of 6/4 is 2
print(3+2*2) #this will return 7 because 2*2 is 4 and 3+4 is 7
print(3-2) #this will return 1 because 3-2 is 1
#() // parentheses, used to group operations and change the order of operations (BEDMAS)
print((3+2)*2) #this will return 10 because (3+2) is 5 and 5*2 is 10