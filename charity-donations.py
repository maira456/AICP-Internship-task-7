# Initialize charity names and donation totals
charities = ["Save the Animals", "Clean Water Project", "Education for All"]
charity_totals = [0, 0, 0]

# TASK 1
def setup_donation_system():
    print("\nCharities available for donation:\n")
    for i in range(3):
        print(f"\t\t{i+1}. {charities[i]}")

    # Initialize variables for donation calculation
    shopping_bill = 0
    charity_choice = 0

    while charity_choice not in [1, 2, 3]:
        charity_choice = int(input("\n\t\tChoose a charity (1-3): "))

    shopping_bill = float(input("Enter the value of the customer's shopping bill: "))

    # TASK 2
    record_and_total_donation(charity_choice, shopping_bill)

# TASK 2
def record_and_total_donation(charity_choice, shopping_bill):
    donation = shopping_bill * 0.1  # Adjust the percentage as needed
    charity_totals[charity_choice - 1] += donation

    print(f"\n\t\t\tDonation of ${donation:.2f} recorded for {charities[charity_choice - 1]}.")

# TASK 3
def show_totals():
    print("\nCharities and their totals in descending order:")
    sorted_charities = sorted(zip(charities, charity_totals), key=lambda x: x[1], reverse=True)
    for charity, total in sorted_charities:
        print(f"{charity}: ${total:.2f}")

    grand_total = sum(charity_totals)
    print(f"\nGRAND TOTAL DONATED TO CHARITY: ${grand_total:.2f}")

# Main program
# Allow multiple customers to donate
while True:
    print("\t\t================= Menu ===================")
    print("\n\t\t\t1. Make a donation\n\t\t\t2. Show totals\n\t\t\t3. Quit")
    choice = int(input("\nEnter your choice: "))

    if choice == 1:
        setup_donation_system()
    elif choice == 2:
        show_totals()
    elif choice == 3:
        print("\nQuitting the program. Thank you!")
        break
    else:
        print("Invalid choice. Please choose again.")
