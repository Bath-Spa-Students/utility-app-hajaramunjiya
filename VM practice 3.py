#Create a Nested dictionary to store the item category, item name,item code, price, and stock. And display the list of items using thefunction

# Define a nested dictionary to store item information
items_dict = {
    "item1": {
        "category": "Electronics",
        "name": "Laptop",
        "code": "LPT001",
        "price": 2000.00,
        "stock": 15,
    },
    "item2": {
        "category": "Clothing",
        "name": "T-Shirt",
        "code": "TS001",
        "price": 12.00,
        "stock": 50,
    },
    "item3": {
        "category": "Books",
        "name": "Python Programming",
        "code": "PYB001",
        "price": 45.00,
        "stock": 20,
    },
    # Add more items as needed
}

# Function to display the list of items
def display_items(item_dict):
    print("List of Items:")
    print("-" * 30)

    for item_key, item_info in item_dict.items():
        print(f"Item Code: {item_info['code']}")
        print(f"Item Name: {item_info['name']}")
        print(f"Category: {item_info['category']}")
        print(f"Price: ${item_info['price']:.2f}")
        print(f"Stock: {item_info['stock']} units")
        print("-" * 30)

# Call the function to display the list of items
display_items(items_dict)
