# Restaurant menu
menu = {
    1: {"name": "Burger", "price": 5.99},
    2: {"name": "Pizza", "price": 8.49} ,
    3: {"name": "Salad", "price": 4.99} ,
    4: {"name": "Drink", "price": 1.99}
}

# Display the menu items

def display_menu(menu):

    print("Welcome to Yoni's restaurant!")
    print("Here's our menu...")

    for item_number, item_info in menu.items():
        print(f"{item_number}. {item_info['name']} - ${item_info['price']}")

# Take order
order ={}

def take_order(menu):
    #order = {}
    while True:
        display_menu(menu)
        item_choice = int(input("Please select item number: "))
        item_qty = int(input("How many orders would you like? "))

        # add order
        if item_choice in menu:
            item_name = menu[item_choice]['name']

            if item_name in order:
                order[item_name] += item_qty
            else:
                order[item_name] = item_qty

        print("Current order: ", order)
        
        #continue ordering?
        #ask user do you want to continue adding to this order?
        continue_order = input("Do you want to add more items? (yes/no): ").lower()
        #if yes, stay in the loop
        #if no, exit loop
        if continue_order != "yes":
            print("Final order: ", order)
            break
    return order

# calculate total
def calculate_total(menu, order):

    # intialize variable, order_total - to store a float
    order_total = 0.0

    # use a for loop to go over the orders dictionary
    for item_number, item_info in menu.items():
        item_name = item_info['name']

        if item_name in order:
        
        # get item_qty from the orders dictionary
            item_qty = order[item_name]
        # set variable - item_price get item_price from menu dictionary
            item_price = item_info['price']
            item_total = item_qty * item_price
        # add item_total to order_total    
            order_total += item_total

    
        # print item_name, item_qty, item_total
        print(f"{item_name} x {item_qty} = ${item_total}")

    # print order_total
    print(f"Total: ${order_total}")
    print("Thank you for ordering at Yoni's restuarant")
    return(order_total)

take_order(menu)
calculate_total(menu, order)