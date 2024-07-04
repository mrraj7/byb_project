# ================================== Practical Task 2 ===================================
# This program calculate the worth of total stock of 4 items in a cafe in stering pounds

# Create a list of items in cafe
menu_list = ["Croissants", "Muffins", "Cupcakes", "Pastries"]

# Create a list of price for each items in cafe
stock_list = [75,50,100,35]

# Create a list of price of each item in a cafe
price_list = [1.50, 1.25, 1.10, 2.50]

# Combine the menu and stock list to create a list of menu items & stock list 
# and then create a stock dictionary using that list
stock = {menu_list[i]: stock_list[i] for i in range(len(menu_list))}
print(f"Stock Dictionary : {stock}")

# Combine the menu & price list to create a list of menu items & price list 
# and then create a price dictionary using that list
price = {menu_list[i]: price_list[i] for i in range(len(menu_list))}
print(f"Price Dictionary : {price}")

# Calculate each item value and then determine the total stock worth in the cafe for each item
total_stock = 0
for item in menu_list:
    item_value = stock[item] * price[item]
    total_stock = total_stock + item_value

# Print the output of total stock worth
print(f"Total stock worth : £ {total_stock}")
