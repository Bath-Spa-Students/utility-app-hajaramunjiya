#Write a program to take 5 numbers as an input from the user andprint the sum and average

# Initialize variables to store sum and count of numbers
sum_of_numbers = 0
count_of_numbers = 5  # We are taking 5 numbers as input

# Iterate through a loop to get 5 numbers from the user
for i in range(count_of_numbers):
    # Prompt the user to enter a number
    user_input = float(input(f"Enter number {i + 1}: "))
    
    # Add the entered number to the sum
    sum_of_numbers += user_input

# Calculate the average by dividing the sum by the count
average_of_numbers = sum_of_numbers / count_of_numbers

# Print the sum and average with detailed comments
print("\nResults:")
print("-" * 20)  # Print a line for separation
print(f"Sum of the numbers: {sum_of_numbers}")
print(f"Average of the numbers: {average_of_numbers}")

# Additional information for the user
print("\nAdditional Information:")
print("-" * 20)
print(f"We took {count_of_numbers} numbers as input.")
print("The sum is calculated by adding all the numbers.")
print("The average is calculated by dividing the sum by the count of numbers.")
