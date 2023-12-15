# This program allows the user to manage and display a list of favorite things.

# Function to display the list of favorite things
def display_favorite_things(favorite_things):
    """
    Displays the list of favorite things.
    
    Parameters:
    favorite_things (list): The list of favorite things to be displayed.
    """
    print("Your Favorite Things:")
    for idx, item in enumerate(favorite_things, start=1):
        print(f"{idx}. {item}")

# Function to add a new favorite thing to the list
def add_favorite_thing(favorite_things, new_thing):
    """
    Adds a new favorite thing to the list.
    
    Parameters:
    favorite_things (list): The list of favorite things.
    new_thing (str): The new favorite thing to be added.
    """
    favorite_things.append(new_thing)
    print(f"{new_thing} has been added to your favorite things!")

# Main function to run the program
def main():
    # Initial list of favorite things
    my_favorite_things = [
        "Listening to music",
        "Hiking in nature",
        "Eating ice cream",
        "making cold coffee",
        "writng poem",

    ]

    # Display the initial list of favorite things
    display_favorite_things(my_favorite_things)

    # Add a new favorite thing
    new_favorite_thing = "Watching sunset at the beach"
    add_favorite_thing(my_favorite_things, new_favorite_thing)

    # Display the updated list of favorite things
    display_favorite_things(my_favorite_things)

# Run the main function if the script is executed
if __name__ == "__main__":
    main()
