import sys
import os
import hashlib
import shutil

VCS_DIR = "vcs"
CONFIG_FILE = os.path.join(VCS_DIR, "config.txt")
INDEX_FILE = os.path.join(VCS_DIR, "index.txt")
LOG_FILE = os.path.join(VCS_DIR, "log.txt")
COMMITS_DIR = os.path.join(VCS_DIR, "commits")

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
os.makedirs(COMMITS_DIR, exist_ok=True)


def read_file(path, default=""):
    return open(path).read() if os.path.exists(path) else default


def tracked_files():
    return read_file(INDEX_FILE).splitlines()


def files_hash():
    h = hashlib.sha256()
    for filename in tracked_files():
        if os.path.exists(filename):
            h.update(open(filename, "rb").read())
    return h.hexdigest()


def last_commit_hash():
    log = read_file(LOG_FILE)
    if not log:
        return None
    first_line = log.splitlines()[0]
    return first_line.split()[1] if first_line.startswith("commit ") else None


def cmd_config(args):
    if not args:
        if os.path.exists(CONFIG_FILE):
            print(f"The username is {read_file(CONFIG_FILE).strip()}.")
        else:
            print("Please, tell me who you are.")
    else:
        with open(CONFIG_FILE, "w") as f:
            f.write(args[0])
        print(f"The username is {args[0]}.")


def cmd_add(args):
    if not args:
        files = read_file(INDEX_FILE).strip()
        if files:
            print("Tracked files:")
            print(files)
        else:
            print("Add a file to the index.")
    else:
        filename = args[0]
        if not os.path.exists(filename):
            print(f"Can't find '{filename}'.")
            return
        tracked = read_file(INDEX_FILE).splitlines()
        if filename not in tracked:
            with open(INDEX_FILE, "a") as f:
                f.write(filename + "\n")
        print(f"The file '{filename}' is tracked.")


def cmd_commit(args):
    if not args:
        print("Message was not passed.")
        return

    message = args[0]
    commit_id = files_hash()
    last_id = last_commit_hash()

    if commit_id == last_id:
        print("Nothing to commit.")
        return

    author = read_file(CONFIG_FILE).strip()
    commit_dir = os.path.join(COMMITS_DIR, commit_id)
    os.makedirs(commit_dir)

    for filename in tracked_files():
        if os.path.exists(filename):
            shutil.copy2(filename, commit_dir)

    entry = f"commit {commit_id}\nAuthor: {author}\n{message}\n\n"
    existing = read_file(LOG_FILE)
    with open(LOG_FILE, "w") as f:
        f.write(entry + existing)

    print("Changes are committed.")


def cmd_log(args):
    log = read_file(LOG_FILE).strip()
    if not log:
        print("No commits yet.")
        return
    print(log)


def cmd_checkout(args):
    if not args:
        print("Commit id was not passed.")
        return

    commit_id = args[0]
    commit_dir = os.path.join(COMMITS_DIR, commit_id)

    if not os.path.exists(commit_dir):
        print("Commit does not exist.")
        return

    for filename in os.listdir(commit_dir):
        shutil.copy2(os.path.join(commit_dir, filename), filename)

    print(f"Switched to commit {commit_id}.")


HANDLERS = {
    "config":   cmd_config,
    "add":      cmd_add,
    "commit":   cmd_commit,
    "log":      cmd_log,
    "checkout": cmd_checkout,
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
