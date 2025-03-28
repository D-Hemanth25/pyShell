import sys

def print(content):
    sys.stdout.write(content + "\n")
    return 0


def invalidCommand(command):
    print(command + ": command not found")
    return 0


def main():
    while True:
        sys.stdout.write("$ ")

        command = input()
        if command == "exit 0":
            break
        else:
            invalidCommand(command)
    return 0


if __name__ == "__main__":
    main()
