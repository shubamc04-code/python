from pathlib import Path


def readfileandfolder():
    """Display files and folders in the current directory."""
    items = sorted(Path.cwd().iterdir(), key=lambda item: item.name.lower())
    if not items:
        print("The directory is empty.")
        return
    for number, item in enumerate(items, start=1):
        kind = "DIR" if item.is_dir() else "FILE"
        print(f"{number}: [{kind}] {item.name}")


def get_path():
    return Path(input("Please enter the file name: ").strip())


def createfile():
    path = get_path()
    if path.exists():
        print("This file already exists.")
        return
    data = input("What do you want to write? ")
    try:
        path.write_text(data, encoding="utf-8")
        print("FILE CREATED SUCCESSFULLY")
    except OSError as err:
        print(f"An error occurred: {err}")


def readfile():
    path = get_path()
    try:
        if not path.is_file():
            print("File not found.")
            return
        print("\n" + path.read_text(encoding="utf-8"))
    except OSError as err:
        print(f"An error occurred: {err}")


def updatefile():
    path = get_path()
    if not path.is_file():
        print("File not found.")
        return
    new_name = input("Enter the new file name (or press Enter to keep it): ").strip()
    if new_name:
        new_path = Path(new_name)
        try:
            path.rename(new_path)
            path = new_path
        except OSError as err:
            print(f"An error occurred: {err}")
            return

    mode = input("Enter 1 to overwrite or 2 to append: ").strip()
    if mode not in {"1", "2"}:
        print("Invalid option.")
        return
    data = input("Enter the text: ")
    try:
        file_mode = "w" if mode == "1" else "a"
        with path.open(file_mode, encoding="utf-8") as file:
            file.write(data)
        print("FILE UPDATED SUCCESSFULLY")
    except OSError as err:
        print(f"An error occurred: {err}")


def deletefile():
    path = get_path()
    if not path.is_file():
        print("File not found.")
        return
    try:
        path.unlink()
        print("FILE DELETED SUCCESSFULLY")
    except OSError as err:
        print(f"An error occurred: {err}")


def main():
    actions = {
        "1": createfile,
        "2": readfile,
        "3": updatefile,
        "4": deletefile,
        "5": readfileandfolder,
    }
    while True:
        print("\n1. Create file\n2. Read file\n3. Update file\n4. Delete file")
        print("5. List files\n0. Exit")
        check = input("Please choose an option: ").strip()
        if check == "0":
            print("Goodbye!")
            break
        action = actions.get(check)
        if action:
            action()
        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()