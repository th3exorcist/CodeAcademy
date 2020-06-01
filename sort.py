inventory = ['twin bed', 'twin bed', 'headboard', 'queen bed', 'king bed', 'dresser', 'dresser', 'table', 'table', 'nightstand', 'nightstand', 'king bed', 'king bed', 'twin bed', 'twin bed', 'sheets', 'sheets', 'pillow', 'pillow']


inventory_len = len(inventory)

first = inventory[0]

last = inventory[-1]

# Select items from the inventory starting at index 2 and up to, but not including, index 6
inventory_2_6 = inventory[2:6]

# Select the first 3 items of inventory and save it to the variable first_3.
first_3 = inventory[:3]

twin_beds = inventory.count('twin bed')

inventory.sort()

new_list = sorted(inventory)
