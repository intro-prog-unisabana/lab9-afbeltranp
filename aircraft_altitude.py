from aircraft import Aircraft


def main():
    model = input("Enter aircraft model:\n")
    aircraft = Aircraft(model)

    while True:
        command = input("Enter command (A for ascent, D for descent, X to exit):\n").strip()
        if command == "X":
            break

        action, feet = command.split()
        feet = int(feet)

        if action == "A":
            aircraft.climb(feet)
        elif action == "D":
            aircraft.descend(feet)

    print(f"Final altitude: {aircraft.altitude} feet")


if __name__ == "__main__":
    main()
