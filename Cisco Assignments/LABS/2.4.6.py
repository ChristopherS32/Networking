hatlist = [1, 2, 3, 4, 5]  # This is an existing list of numbers hidden in the hat.

hatlist[3] = int(input("Enter a new number: "))

# Step 2: write a line of code that removes the last element from the list.
del hatlist[-1]

# Step 3: write a line of code that prints the length of the existing list.
print(len(hatlist))
