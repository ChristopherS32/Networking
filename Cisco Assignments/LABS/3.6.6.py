my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

ulist = []
for i in my_list:
    if i not in ulist:
        ulist.append(i)

my_list = ulist
print("The list with unique elements only:")
print(my_list)

