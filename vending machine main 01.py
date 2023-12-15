import pygame
import sys
import time

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600# Set the dimensions of the game window
FPS = 60  # Frames per second
WHITE = (255, 255, 255)  # Define a white color
BLACK = (0, 0, 0)  # Define a black color
GRAY = (100, 100, 100)  # Define a gray color
RED = (250, 0, 0)  # Define a red color
GREEN = (0, 250, 0)  # Define a green color
FONT_SIZE = 15  # Font size for general text
HEADING_FONT_SIZE = 30  # Font size for headings
POPUP_FONT_SIZE = 15  # Font size for popup messages
BUTTON_COLOR = (30, 144, 255)  # Color for buttons
SELECTED_COLOR = (200, 200, 0)  # Color for selected items



# Vending machine inventory with details for each item
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

# Pygame setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))# Initialize the game window
pygame.display.set_caption("Vending Machine GUI")  # Set the window title
clock = pygame.time.Clock()  # Create a clock object to control the frame rate

# Fonts
font = pygame.font.SysFont('arial', FONT_SIZE)# Create a font for general text
heading_font = pygame.font.SysFont('arial', HEADING_FONT_SIZE)  # Create a font for headings
popup_font = pygame.font.SysFont('arial', POPUP_FONT_SIZE)  # Create a font for popup messages

# State variables
coin_inserted = 0# Variable to track the amount of money inserted
selected_item = None  # Variable to track the currently selected item
current_state = 'categories'  # Initial state of the vending machine
cart = []  # List to store items in the cart
selected_category = None  # Variable to store the currently selected category
categories = sorted(set(item['category'] for item in inventory.values()))  # List of unique categories

# Function to draw text on the screen with optional box width
def draw_text(text, center_x, y, font, color=WHITE,box_width=190):
    text_surface = font.render(text, True, color)
    text_width, text_height = text_surface.get_size()
    x = center_x - text_width // 2
    screen.blit(text_surface, (x, y))

# Function to calculate the total cost of items in the cart
def calculate_total(cart):
    total_cost = 0
    for item_code in cart:
        item = inventory[item_code]
        total_cost += item['price']
    return total_cost

# Function to draw a button with text
def draw_button(text, rect, color):
    pygame.draw.rect(screen, color, rect)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect(center=rect.center)
    screen.blit(text_surface, text_rect)

# Function to draw the back button and return its rectangle
def draw_back_button():
    back_button_rect = pygame.Rect(10, 10, 100, 30)
    draw_button("Back", back_button_rect, GRAY)
    return back_button_rect

# Function to draw the checkout button and return its rectangle
def draw_checkout_button():
    checkout_button_rect = pygame.Rect(WIDTH - 200, 550, 200, 50)
    draw_button("Checkout", checkout_button_rect, BUTTON_COLOR)
    return checkout_button_rect

# Function to draw the checkout button and return its rectangle
def draw_exit_button():
    exit_button_rect = pygame.Rect(WIDTH // 3 - 100, 300, 200, 50) 
    draw_button("Exit", exit_button_rect, BUTTON_COLOR)
    return exit_button_rect

# Function to draw text in a rectangle with specified alignment and padding
def draw_text_in_rect(text, rect, font, color, alignment='center', padding=10):
    text_surf = font.render(text, True, color)
    
    if alignment == 'center':
        text_rect = text_surf.get_rect(center=rect.center)
    elif alignment == 'left':
        text_rect = text_surf.get_rect(midleft=(rect.left + padding, rect.centery))
    else:
        text_rect = text_surf.get_rect(center=rect.center)

    screen.blit(text_surf, text_rect)

# Function to draw the categories screen
def draw_categories_screen():
    global categories
    screen.fill(BLACK)  # Clear the screen

    # Heading
    draw_text("Select a Category", WIDTH // 2.5, 90, heading_font, WHITE)

    # Button dimensions
    button_width = 200
    button_height = 50
    button_margin = 20
    start_y = 150  # Starting y position of the first button

# Loop through items in the category and draw buttons
    for i, category in enumerate(categories):
        button_x = (WIDTH - button_width) // 3
        button_y = start_y + i * (button_height + button_margin)

        # Draw button rectangle
        button_rect = pygame.Rect(button_x, button_y, button_width, button_height)
        pygame.draw.rect(screen, BUTTON_COLOR, button_rect)

        # Draw category text in button
        draw_text_in_rect(category, button_rect, font, WHITE, 'center')


def draw_items_screen(category):
    global inventory
    screen.fill(BLACK)  # Clear the screen

    # Heading
    draw_text(f"Choose the {category}", WIDTH // 3, 90, heading_font, WHITE)

    # Button dimensions
    button_width = 200
    button_height = 50
    button_margin = 20
    start_y = 150  # Starting y position of the first button

    # Filter items by category
    items_in_category = {code: item for code, item in inventory.items() if item['category'] == category}

    for i, (code, item) in enumerate(items_in_category.items()):
        button_x = (WIDTH - button_width) // 3
        button_y = start_y + i * (button_height + button_margin)

        # Draw button rectangle
        button_rect = pygame.Rect(button_x, button_y, button_width, button_height)
        pygame.draw.rect(screen, BUTTON_COLOR, button_rect)

        # Draw item name and price
        item_text = f"{item['name']} - ${item['price']}"
        item_text_rect = pygame.Rect(button_x, button_y, button_width, button_height // 2)
        draw_text_in_rect(item_text, item_text_rect, font, WHITE, 'center')

        # Draw stock information
        stock_text = f"{item['stock']} in stock" if item['stock'] > 0 else "Out of Stock"
        stock_text_rect = pygame.Rect(button_x, button_y + button_height // 2, button_width, button_height // 2)
        stock_color = GRAY if item['stock'] > 0 else RED
        draw_text_in_rect(stock_text, stock_text_rect, font, stock_color,'center')

    draw_back_button()


def draw_cart_screen():
    global cart, inventory
    sidebar_width = 200
    sidebar_height = HEIGHT
    sidebar_x = WIDTH - sidebar_width  # Starting x-coordinate of the sidebar
    item_height = 20  # Height of each item in the cart
    padding = 10  # Padding inside the sidebar

    # Draw the sidebar background
    sidebar_rect = pygame.Rect(sidebar_x, 0, sidebar_width, sidebar_height)
    pygame.draw.rect(screen, GRAY, sidebar_rect)

    # Draw a heading for the cart
    cart_heading_rect = pygame.Rect(sidebar_x, padding, sidebar_width, item_height)
    draw_text_in_rect("Cart", cart_heading_rect, heading_font, WHITE,'center')

    # Display each item in the cart
    y_position = cart_heading_rect.bottom + padding
    for i, item_code in enumerate(cart):
        item = inventory[item_code]
        item_rect = pygame.Rect(sidebar_x, y_position, sidebar_width, item_height)
        item_text = f"{item['name']}   -   ${item['price']}"
        draw_text_in_rect(item_text, item_rect, font, WHITE,'left')
        y_position += item_height

    # Calculate total cost
    total_cost_rect = pygame.Rect(sidebar_x, HEIGHT - item_height - 60, sidebar_width, item_height)
    draw_text_in_rect(f"Total: ${calculate_total(cart):.2f}", total_cost_rect, font, WHITE,'center')


def get_category_button_rect(index):
    # Function to get the rectangle for a category button
    button_width = 200
    button_height = 50
    button_margin = 20

    # Calculate the x and y position of the button based on the index
    button_x = (WIDTH - button_width) // 3
    button_y = 150 + index * (button_height + button_margin)

    # Create and return a pygame.Rect object for the button
    return pygame.Rect(button_x, button_y, button_width, button_height)

def get_item_button_rect(index):
    # Function to get the rectangle for an item button
    button_width = 200
    button_height = 50
    button_margin = 20

    # Calculate the x and y position of the button
    button_x = (WIDTH - button_width) // 3
    button_y = 150 + index * (button_height + button_margin)

    # Create and return a pygame.Rect object for the button
    return pygame.Rect(button_x, button_y, button_width, button_height)

#main loop
def main():
    global current_state, selected_category, cart, coin_inserted
    while True:
        screen.fill(BLACK)
# State machine for different screens
        if current_state == 'categories':
            draw_categories_screen()
        elif current_state == 'items':
            draw_items_screen(selected_category)
                        # Draw the checkout screen
        elif current_state == 'checkout':
            draw_text("Insert Coins (Enter number Keys)", WIDTH // 3, 150, heading_font, WHITE)
            draw_text(f"Total Cost: ${calculate_total(cart):.2f}", WIDTH // 3, 200, font, WHITE)
            draw_text(f"Coins Inserted: ${coin_inserted:.2f}", WIDTH // 3, 250, font, GREEN)
        elif current_state == 'complete':
            draw_text(f"Transaction Complete, Balance: ${coin_inserted - calculate_total(cart):.2f}", WIDTH // 3, 200, font, GREEN)
            draw_text(f"Dispensing Items........", WIDTH // 3, 230, font, WHITE)
            draw_text(f"Thank you for your purchase!", WIDTH // 3, 260, font, WHITE)
            exit_button_rect = draw_exit_button()  # Draw the exit button
           
         # Draw the cart and buttons
        draw_cart_screen()
        checkout_button_rect = draw_checkout_button()
         
         # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if current_state == 'checkout':
                    # Handle coin insertion via number keys
                    if event.key in [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5, pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9]:
                        coin_inserted += int(event.unicode)
                        if coin_inserted >= calculate_total(cart):
                            current_state = 'complete'  # Change to a completion state
                             # Handle coin insertion via 'C' key
                    elif event.key == pygame.K_c:
                        coin_inserted += 1

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
               
                # Handle clicks based on the current state
                if current_state == 'categories':
                     # Check if a category button is clicked
                    for i, category in enumerate(categories):
                        button_rect = get_category_button_rect(i)
                        if button_rect.collidepoint(mouse_x, mouse_y):
                            selected_category = category
                            current_state = 'items'
                            break

                elif current_state == 'items':
                    # Check if the back button is clicked
                    back_button_rect = draw_back_button()
                    if back_button_rect.collidepoint(mouse_x, mouse_y):
                        current_state = 'categories' 
                        # Check if an item button is clicked
                    items_in_category = {code: item for code, item in inventory.items() if item['category'] == selected_category}
                    for i, (code, item) in enumerate(items_in_category.items()):
                        button_rect = get_item_button_rect(i)
                        if button_rect.collidepoint(mouse_x, mouse_y):
                            if inventory[code]['stock']>0:
                                cart.append(code)
                                inventory[code]['stock'] -= 1
                            current_state = 'items'
                            break
                elif current_state == 'complete':
                     # Check if the exit button is clicked
                    if exit_button_rect.collidepoint(mouse_x, mouse_y):
                        current_state = 'categories'
                        cart = []  #clear the cart
                        coin_inserted = 0
                # Checkout button click
                if cart and checkout_button_rect.collidepoint(mouse_x, mouse_y):
                    current_state = 'checkout'

        pygame.display.flip()
        clock.tick(FPS)

#Run the main function if the script is executed
if __name__ == "__main__":
    main()