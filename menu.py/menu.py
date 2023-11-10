menu_items = {
    1: {"Item name": "Apple", "Price": 0.49},
    2: {"Item name": "Tea - Thai iced", "Price": 3.99},
    3: {"Item name": "Fried banana", "Price": 4.49},
}

order = []

while True:
    print("Menu:")
    for key, value in menu_items.items():
        print(f"{key}. {value['Item name']} - ${value['Price']:.2f}")

    menu_selection = input("Enter your selection from the menu (1, 2, 3): ")

    if not menu_selection.isdigit():
        print("Error: Please enter a valid number.")
        continue

    menu_selection = int(menu_selection)

    if menu_selection not in menu_items.keys():
        print("Error: Invalid menu selection.")
        continue

    item_name = menu_items[menu_selection]["Item name"]
    quantity = input(f"How many {item_name}s would you like? (Default is 1): ")

    if not quantity.isdigit():
        print("Invalid input. Quantity set to 1.")
        quantity = 1
    else:
        quantity = int(quantity)

    order.append({
        "Item name": item_name,
        "Price": menu_items[menu_selection]["Price"],
        "Quantity": quantity
    })

    place_order = input("Would you like to order more? (y/n): ").lower()

    match place_order:
        case 'y':
            continue
        case 'n':
            print("Thank you for your order.")
            break
        case _:
            print("Invalid input. Please try again.")
print("\nOrder Receipt")
print("{:<25} | {:<7} | {:<8}".format("Item name", "Price", "Quantity"))
print("-" * 41)

total_price = sum(item["Price"] * item["Quantity"] for item in order)

for item in order:
    item_name, price, quantity = item["Item name"], item["Price"], item["Quantity"]
    spaces_item = " " * (25 - len(item_name))
    spaces_price = " " * (7 - len(str(price)))
    print(f"{item_name}{spaces_item}| ${price:.2f}{spaces_price}| {quantity}")

print("-" * 41)
print(f"Total{' ' * 31}| ${total_price:.2f}")
