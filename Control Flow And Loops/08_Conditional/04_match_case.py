a = int(input("Enter a lucky number between 1 to 10: "))

match a:
    case 1:
        print("You won charger")
    case 3:
        print("you won phone")
    case 6:
        print("you won bike")
    case _:
        print("Better Luck next time")