import time
from colorama import Fore, Style, init

# ASCII art

ascii_art = '''
                       ___                                     __    _               
 _   _____  ____  ____/ (_)___  ____ _   ____ ___  ____ ______/ /_  (_)___  ___      
| | / / _ \/ __ \/ __  / / __ \/ __ `/  / __ `__ \/ __ `/ ___/ __ \/ / __ \/ _ \\     
| |/ /  __/ / / / /_/ / / / / / /_/ /  / / / / / / /_/ / /__/ / / / / / / /  __/     
|___/\\___/_/ /_/\\__,_/_/_/ /_/\__, /  /_/ /_/ /_/\\__,_/\\___/_/ /_/ /_/ /_/\\___/      
                             /____/                                                  
'''

print(ascii_art)



# Initialize Colorama to support colored terminal output
init(autoreset=True)

# Vending machine inventory
inventory = {
    'A1': {'name': 'Coke', 'price': 1.25, 'category': 'Cold Drinks', 'stock': 10},
    'A2': {'name': 'Pepsi', 'price': 1.25, 'category': 'Cold Drinks', 'stock': 10},
    'A3': {'name': 'Water', 'price': 1.00, 'category': 'Cold Drinks', 'stock': 20},
    'B1': {'name': 'Coffee', 'price': 2.00, 'category': 'Hot Drinks', 'stock': 10},
    'B2': {'name': 'Tea', 'price': 1.50, 'category': 'Hot Drinks', 'stock': 10},
    'B3': {'name': 'Hot Chocolate', 'price': 2.50, 'category': 'Hot Drinks', 'stock': 7},
    'C1': {'name': 'Chips', 'price': 1.00, 'category': 'Snacks', 'stock': 15},
    'C2': {'name': 'Chocolate Bar', 'price': 1.50, 'category': 'Snacks', 'stock': 8},
    'C3': {'name': 'Nuts', 'price': 1.75, 'category': 'Snacks', 'stock': 5},
    'D1': {'name': 'Granola Bar', 'price': 1.25, 'category': 'Protein Snacks', 'stock': 12},
    'D2': {'name': 'Fruit Snacks', 'price': 1.00, 'category': 'Protein Snacks', 'stock': 15}
}

# Function to categorize the items in the inventory
def get_categories():
    return sorted(set(item['category'] for item in inventory.values()))

# Function to display list of available categories
def display_categories():
    categories = get_categories()
    print(Fore.BLUE + "\n\nChoose from available Categories:\n")
    for i, category in enumerate(categories, 1):
        print(Fore.CYAN + str(i) + " - " + category)

# Function to display items within each category
def display_items(category):
    print(Fore.BLUE + "\nSelect Item\n\n" + category + ":")
    for code, item in inventory.items():
        if item['category'] == category:
            # Display in green if the item is in stock, otherwise, display in red
            stock_color = Fore.GREEN if item['stock'] > 0 else Fore.RED
            print(stock_color + f"{code}: {item['name']} - ${item['price']} ({item['stock']} in stock)")
    print("\n")

def select_category():
    display_categories()
    print(Fore.YELLOW + "0 - Exit\n")
    print("----------------------------------------\n")

    while True:
        choice = input(Fore.YELLOW + "Choose a category (or 0 to exit): ")

        # Validate if the correct category is entered
        if choice.isdigit():
            choice = int(choice)
            if 1 <= choice <= len(get_categories()):
                # Return the selection
                return get_categories()[choice - 1]
            elif choice == 0:
                return None
        print(Fore.RED + "Invalid selection. Please try again.")

# Function to handle select item
def select_item(category):
    # Display items in the passed category
    display_items(category)

    while True:
        choice = input(Fore.YELLOW + "Choose an item (Enter Code or type 'back' to return): ").upper()

        # Validate input code
        if choice in inventory and inventory[choice]['category'] == category:
            # Check if in stock
            if inventory[choice]['stock'] > 0:
                return choice
            else:
                print(Fore.RED + "\nItem out of stock. Please choose another item.")
        # If the user wants to go to the main menu
        elif choice == 'BACK':
            return None
        else:
            print(Fore.RED + "\nInvalid selection. Please try again.\n")

# Function to handle select category
def select_items():
    # Array to store selected items
    cart = []

    while True:
        category = select_category()
        if category is None:
            break

        # Select item inside the category
        item_code = select_item(category)
        if item_code:
            cart.append(item_code)
            print(Fore.GREEN + f"\nItem {inventory[item_code]['name']} added to cart.\n\n")

        # Ask if the user wants to buy more items
        add_more = input(Fore.YELLOW + "Do you want to add more items? (yes/no): ").lower()
        if add_more != 'yes':
            break

    return cart

# Function to calculate cart total
def calculate_total(cart):
    return sum(inventory[item]['price'] for item in cart)

# Function to handle payment
def process_payment(total_cost):
    total_inserted = 0

    # If the user enters the amount multiple times (like inserting coins)
    while total_inserted < total_cost:
        response = input(Fore.YELLOW + f"Total inserted: ${total_inserted:.2f}. Insert more money (Enter amount): ")

        # Check if the input is a positive number (either int or float)
        if response.replace('.', '', 1).isdigit() and response.count('.') <= 1 and float(response) > 0:
            amount_inserted = float(response)
            total_inserted += amount_inserted
            if total_inserted >= total_cost:
                return total_inserted - total_cost
            else:  # If the entered amount is not sufficient
                print(Fore.RED + f"Total inserted: ${total_inserted:.2f}. Remaining: ${total_cost - total_inserted:.2f}")
        else:
            print(Fore.RED + "Please insert a valid amount of money.")
    # Return the balance amount
    return total_inserted - total_cost

# Function to vend items
def vend_items(cart, change):
    for item_code in cart:
        inventory[item_code]['stock'] -= 1
        print(Fore.GREEN + f"\nDispensing {inventory[item_code]['name']}.....")
    print(Fore.GREEN + f"\n\nYour total change is ${change:.2f}. Thank you for your purchase!")

if __name__ == "__main__":
    while True:
        # Welcome message
        print(Fore.CYAN + "\n\n**------------------------------------------------**")
        print(Fore.CYAN + "                     welcome :) ")
        print(Fore.CYAN + "**------------------------------------------------**")

        # Ask the user to select items
        cart = select_items()

        # If the user didn't select anything, restart.
        if not cart:
            print(Fore.RED + "No items selected. Exiting.")
            continue

        # Call function to calculate the total cost of items in the cart
        total_cost = calculate_total(cart)
        print(Fore.BLUE + f"\nTotal cost: ${total_cost:.2f}\n")

        # Call function to process payment
        change = process_payment(total_cost)

        # If payment completed, vend items
        if change is not None:
            print(Fore.YELLOW + "\nProcessing....")
            time.sleep(2)
            vend_items(cart, change)

        # Wait 4 seconds to start the next cycle
        time.sleep(4)
