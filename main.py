import sys

def print(content):
    sys.stdout.write(content + "\n")
    return 0


def parseInput(inputString):
    parts = inputString.split(maxsplit=1)
    command = parts[0] if parts else ""
    contents = parts[1] if len(parts) > 1 else ""
    return command, contents


def typeBuiltin(command):
    builtins = {'type', 'exit', 'echo'}
    if command in builtins:
        print(command + " is a shell builtin")
    else:
        print(command + ": not found")


def invalidCommand(command):
    print(command + ": command not found")
    return 0


def main():
    while True:
        sys.stdout.write("$ ")

        command, contents = parseInput(input())

        if command == "exit":
            break
        elif command == "type":
            typeBuiltin(contents)
        elif command == "echo":
            print(contents)
        else:
            invalidCommand(command)
    return 0


if __name__ == "__main__":
    main()
