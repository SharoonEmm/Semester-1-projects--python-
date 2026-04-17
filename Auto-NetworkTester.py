import os


# Description:
#     This program is a CLI-based network tester that allows users to select
#     preloaded domains or enter a custom domain, then automatically checks
#     whether the domain is reachable using ping.
#
# Purpose:
#     The purpose of this project is to apply concepts learned in Python and
#     Data Communications, including functions, loops, classes, and file handling,
#     to build a structured and functional program.
#
# Improvement:
#     The program is designed to be easily extendable, with future improvements
#     including better input validation, timestamps, and additional network tools.


# Class to represent one network test result
class NetworkTest:
    # Constructor to initialize domain and status
    def __init__(self, domain, status):
        self.domain = domain
        self.status = status

    # Method to display the result in a clean format
    def display_result(self):
        print(f"Domain: {self.domain} | Status: {self.status}")

    # Method to format result for saving into a file
    def save_format(self):
        return f"{self.domain},{self.status}\n"


# Preloaded list of commonly used domains for testing reachability
domains = [
    "google.com",
    "sheridancollege.ca",
    "outlook.com",
    "amazon.com",
    "wikipedia.org"
]

# List to store test results during program execution
result_objects = []


# Function to display the main menu
def show_menu():
    print("\n--- Network Tester ---")
    print("1. Show domains")
    print("2. Test a preloaded domain")
    print("3. Test a custom domain")
    print("4. View current results")
    print("5. Save results to file")
    print("6. View saved results")
    print("7. Exit")


# Function to display all preloaded domains
def show_domains():
    print("\nAvailable Domains:")
    for index in range(len(domains)):
        print(f"{index}: {domains[index]}")


# Function to automatically test if a domain is reachable
def auto_test_domain(domain):
    if os.name == "nt":  # Windows
        response = os.system(f"ping -n 1 {domain}")
    else:  # Mac/Linux
        response = os.system(f"ping -c 1 {domain}")

    if response == 0:
        return "Reachable"
    else:
        return "Unreachable"


# Function to test one of the preloaded domains
def test_preloaded_domain():
    show_domains()

    try:
        select_domain = int(input("\nEnter the index of the domain to test: "))

        if select_domain < 0 or select_domain >= len(domains):
            print("Invalid index.")
            return

        # Get the selected domain from the list
        chosen_domain = domains[select_domain]
        print(f"\nTesting {chosen_domain}...")

        # Automatically test the selected domain
        status = auto_test_domain(chosen_domain)

        # Create an object to store the result
        test_result = NetworkTest(chosen_domain, status)

        # Add result object to the list
        result_objects.append(test_result)

        # Display result
        print("\nTest completed:")
        test_result.display_result()

    except ValueError:
        print("Please enter a valid number.")


# Function to test a custom domain entered by the user
def test_custom_domain():
    # Ask user to enter a custom domain
    domain = input("\nEnter a domain (e.g., google.com): ")

    # Check if user entered an empty value
    if domain == "":
        print("Domain cannot be empty.")
        return

    print(f"\nTesting {domain}...")

    # Automatically test the entered domain
    status = auto_test_domain(domain)

    # Create an object to store the result
    test_result = NetworkTest(domain, status)

    # Add result object to the list
    result_objects.append(test_result)

    # Display result
    print("\nTest completed:")
    test_result.display_result()


# Function to display results from the current session
def view_current_results():
    # Check if there are any results in the list
    if len(result_objects) == 0:
        print("\nNo test results available.")
    else:
        print("\nCurrent Test Results:")
        for result in result_objects:
            result.display_result()


# Function to save current results to a text file
def save_results_to_file():
    # Check if there are results to save
    if len(result_objects) == 0:
        print("\nNo results to save.")
        return

    # Open file in append mode to keep previous data
    file = open("network_results.txt", "a")

    # Write each result to the file
    for result in result_objects:
        file.write(result.save_format())

    # Close file after writing
    file.close()
    print("\nResults saved to network_results.txt")


# Function to read and display saved results from the file
def view_saved_results():
    try:
        # Open file in read mode
        file = open("network_results.txt", "r")

        # Read all lines from the file
        content = file.readlines()

        # Close the file
        file.close()

        # Check if file is empty
        if len(content) == 0:
            print("\nThe file is empty.")
        else:
            print("\nSaved Results:")
            for line in content:
                print(line.strip())

    except FileNotFoundError:
        print("\nNo saved results file found yet.")


# Main function to control program flow
def main():
    # Keep program running until user chooses to exit
    while True:
        show_menu()
        choice = input("\nChoose an option: ")

        # Perform action based on menu choice
        if choice == "1":
            show_domains()
        elif choice == "2":
            test_preloaded_domain()
        elif choice == "3":
            test_custom_domain()
        elif choice == "4":
            view_current_results()
        elif choice == "5":
            save_results_to_file()
        elif choice == "6":
            view_saved_results()
        elif choice == "7":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")


# Run the program
if __name__ == "__main__":
    main()
