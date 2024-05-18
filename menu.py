from colorama import Fore, init

init(autoreset=True)


def gameINIT():
    difficulty = ["1", "2", "3", "4", "5"]
    choice = ""

    while choice not in difficulty:
        # CLear the screen
        print("\033[H", end="")

        # Menu
        print(Fore.LIGHTYELLOW_EX + "★ " * 16)
        print(Fore.LIGHTYELLOW_EX + "★                              ★")
        print(Fore.LIGHTYELLOW_EX + "★  SnakeOnTerminal By Gustavo  ★")
        print(Fore.LIGHTYELLOW_EX + "★                              ★")
        print(Fore.LIGHTYELLOW_EX + "★     Play using: WASD keys    ★")
        print(Fore.LIGHTYELLOW_EX + "★                              ★")
        print(Fore.LIGHTYELLOW_EX + "★    Select the difficulty:    ★")
        print(Fore.LIGHTYELLOW_EX + "★    1 - Easy                  ★")
        print(Fore.LIGHTYELLOW_EX + "★    2 - Normal                ★")
        print(Fore.LIGHTYELLOW_EX + "★    3 - Hard                  ★")
        print(Fore.LIGHTYELLOW_EX + "★    4 - Godlike               ★")
        print(Fore.LIGHTYELLOW_EX + "★                              ★")
        print(Fore.LIGHTYELLOW_EX + "★ " * 16)
        choice = input("\nChoose the difficulty: ")
    return choice


def gameOver(Score, difficulty):
    match difficulty:
        case "1":
            difficulty = "Eazy"
        case "2":
            difficulty = "Normal"
        case "3":
            difficulty = "Hard"
        case "4":
            difficulty = "Hardest"

    print("\033[H", end="")
    print(
        Fore.RED
        + f"\nGame is Over you did {Score} points on {difficulty} difficulty, Nice try"
    )
    print(Fore.LIGHTYELLOW_EX + "★ " * int(Score))


if __name__ == "__main__":
    # gameINIT()
    gameOver(1, 1)
