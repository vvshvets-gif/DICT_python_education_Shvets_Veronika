import sys

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

arg = sys.argv[1] if len(sys.argv) > 1 else "--help"

if arg == "--help":
    print(HELP)
elif arg in COMMANDS:
    print(COMMANDS[arg])
else:
    print(f"'{arg}' is not a VCS command.")
