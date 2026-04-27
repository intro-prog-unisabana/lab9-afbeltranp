from bank_account import BankAccount
from utils import balance_summary, person_data


def main():
    people = []

    while True:
        print("Choose an option:")
        print("1. Add a new person")
        print("2. Add an account to a person")
        print("3. Show all balances")
        print("4. Quit")

        choice = input().strip()

        if choice == "1":
            people.append(person_data())

        elif choice == "2":
            target_name = input("Enter the person's name:\n")
            selected_person = None
            for person in people:
                if person.name == target_name:
                    selected_person = person
                    break

            if selected_person is None:
                print("Person not found.")
            else:
                account_number = int(input("Enter a 4-digit account number:\n"))
                balance = float(input("Enter the initial balance:\n"))
                selected_person.add_account(BankAccount(account_number, balance))

        elif choice == "3":
            if not people:
                print("No data to show.")
            else:
                balance_summary(people)

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please choose 1-4.")


if __name__ == "__main__":
    main()
