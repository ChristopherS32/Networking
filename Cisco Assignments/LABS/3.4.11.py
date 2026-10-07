beatles = []
print("Step 1:", beatles)

# step 2
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print("Step 2:", beatles)

# step 3
for i in range(2):
    newmem = input("Enter the name of a new member: ")
    beatles.append(newmem)
print("Step 3:", beatles)

# step 4
del beatles[-1]  # Remove the last element (Stuart Sutcliffe)
del beatles[-1]  # Remove the second-to-last element (Pete Best)
print("Step 4:", beatles)

# step 5
beatles.insert(0, "Ringo Starr")
print("Step 5:", beatles)


# testing list legth
print("The Fab", len(beatles))