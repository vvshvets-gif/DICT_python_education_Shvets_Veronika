import sys
import os

VCS_DIR = "vcs"
CONFIG_FILE = os.path.join(VCS_DIR, "config.txt")
INDEX_FILE = os.path.join(VCS_DIR, "index.txt")

COMMANDS = {
    "config":   "Get and set a username.",
    "add":      "Add a file to the index.",
    "log":      "Show commit logs.",
    "commit":   "Save changes.",
    "checkout": "Switch between commits and restore a previous file state.",
}

HELP = "These are VCS commands:\n" + "\n".join(
    f"{cmd:<10}{desc}" for cmd, desc in COMMANDS.items()
)

os.makedirs(VCS_DIR, exist_ok=True)


def cmd_config(args):
    if not args:
        if os.path.exists(CONFIG_FILE):
            print(f"The username is {open(CONFIG_FILE).read().strip()}.")
        else:
            print("Please, tell me who you are.")
    else:
        with open(CONFIG_FILE, "w") as f:
            f.write(args[0])
        print(f"The username is {args[0]}.")


def cmd_add(args):
    if not args:
        if os.path.exists(INDEX_FILE):
            files = open(INDEX_FILE).read().strip()
            if files:
                print("Tracked files:")
                print(files)
                return
        print("Add a file to the index.")
    else:
        filename = args[0]
        if not os.path.exists(filename):
            print(f"Can't find '{filename}'.")
            return
        tracked = open(INDEX_FILE).read().splitlines() if os.path.exists(INDEX_FILE) else []
        if filename not in tracked:
            with open(INDEX_FILE, "a") as f:
                f.write(filename + "\n")
        print(f"The file '{filename}' is tracked.")


HANDLERS = {
    "config": cmd_config,
    "add": cmd_add,
}

arg = sys.argv[1] if len(sys.argv) > 1 else "--help"
rest = sys.argv[2:]

if arg == "--help":
    print(HELP)
elif arg in HANDLERS:
    HANDLERS[arg](rest)
elif arg in COMMANDS:
    print(COMMANDS[arg])
else:
    print(f"'{arg}' is not a VCS command.")
