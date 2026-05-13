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

markdown = ""


def show_help():
    print("Available formatters:", *FORMATTERS)
    print("Special commands: !help !done")


def done():
    global running
    running = False


def plain():
    return input("Text: ")


def bold():
    return f"**{input('Text: ')}**"


def italic():
    return f"*{input('Text: ')}*"


def inline_code():
    return f"`{input('Text: ')}`"


def new_line():
    return "\n"


def link():
    label = input("Label: ")
    url = input("URL: ")
    return f"[{label}]({url})"


def header():
    while True:
        level = int(input("Level: "))
        if 1 <= level <= 6:
            break
        print("The level should be within the range of 1 to 6")

    text = input("Text: ")
    return f"{'#' * level} {text}\n"


def ordered_list():
    rows = int(input("Number of rows: "))
    result = ""
    for i in range(1, rows + 1):
        result += f"{i}. {input(f'Row #{i}: ')}\n"
    return result


def unordered_list():
    rows = int(input("Number of rows: "))
    result = ""
    for i in range(rows):
        result += f"* {input(f'Row #{i + 1}: ')}\n"
    return result


FORMATTER_ACTIONS = {
    "plain": plain,
    "bold": bold,
    "italic": italic,
    "inline-code": inline_code,
    "new-line": new_line,
    "link": link,
    "header": header,
    "ordered-list": ordered_list,
    "unordered-list": unordered_list,
}

COMMANDS = {
    "!help": show_help,
    "!done": done,
}

running = True

while running:
    cmd = input("Choose a formatter: ")

    action = COMMANDS.get(cmd)
    if action:
        action()
        continue

    formatter = FORMATTER_ACTIONS.get(cmd)
    if not formatter:
        print("Unknown formatting type or command")
        continue

    markdown += formatter()
    print(markdown)