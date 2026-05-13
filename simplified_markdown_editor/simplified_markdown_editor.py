FORMATTERS = (
    "plain",
    "bold",
    "italic",
    "header",
    "link",
    "inline-code",
    "ordered-list",
    "unordered-list",
    "new-line"
)

SPECIAL_COMMANDS = ("!help", "!done")

def show_help():
    print("Available formatters:", *FORMATTERS)
    print("Special commands:", *SPECIAL_COMMANDS)

while True:
    user_input = input("Choose a formatter: ")

    if user_input == "!help":
        show_help()

    elif user_input == "!done":
        break

    elif user_input in FORMATTERS:
        print(f"You selected formatter: {user_input}")

    else:
        print("Unknown formatting type or command")