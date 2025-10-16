def get_positive_integer(prompt):
    """Safely gets a positive integer from the user."""
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            else:
                print("Please enter a positive number > 0.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")

def get_number(prompt):
    """Safely gets a number (integer or float) from the user."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def main():
    """Main function to run the sum calculation program."""
    print("--- Sum of 'n' Numbers Calculator ---")
    
    try:
        num_count = get_positive_integer("How many numbers do you want to sum? ")
        
        numbers = []
        total_sum = 0.0
        
        print("\nEnter the numbers one by one:")
        for i in range(num_count):
            number = get_number(f"Enter number #{i + 1}: ")
            numbers.append(number)
            total_sum += number
            
        print("\n-------------------------------------")
        print(f"You entered the numbers: {numbers}")
        print(f"The sum is: {total_sum}")
        print("-------------------------------------")

    except KeyboardInterrupt:
        print("\n\nProgram exited by user.")

if __name__ == "__main__":
    main()
