blocks = int(input("Enter the number of blocks: "))

height = 0
current_layer_requirement = 1

while blocks >= current_layer_requirement:
    blocks -= current_layer_requirement
    height += 1
    current_layer_requirement += 1

print("pyramid height:", height)