import sys
import os
import subprocess


def print(content):
    sys.stdout.write(content + "\n")
    return 0


def parseInput(inputString):
    parts = inputString.split(maxsplit=1)
    command = parts[0] if parts else ""
    contents = parts[1] if len(parts) > 1 else ""
    return command, contents


def findExecutableInPath(command):
    directories = os.environ.get("PATH", "").split(os.pathsep)

    for directory in directories:
        possiblePath = os.path.join(directory, command)
        if os.path.isfile(possiblePath) and os.access(possiblePath, os.X_OK):
            return possiblePath
    return None


def invalidCommand(command):
    print(command + ": not found")
    return 0


def typeBuiltin(commandArgs):
    builtins = {'type', 'exit', 'echo'}

    args = commandArgs.split()
    for command in args:
        if command in builtins:
            print(command + " is a shell builtin")
            continue
        
        path = findExecutableInPath(command)
        if path:
            print(command + " is " + path)
        else:
            invalidCommand(command)


def executeCommand(command, args):
    path = findExecutableInPath(command)
    if not path:
        invalidCommand(command)
        return 0
    
    result = subprocess.run([command] + args.split(), capture_output=True, text=True)
    print(result.stdout.strip())


def main():
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()

        command, args = parseInput(input())

        if command == "exit":
            break
        elif command == "type":
            typeBuiltin(args)
        elif command == "echo":
            print(args)
        else:
            executeCommand(command, args)
    return 0


if __name__ == "__main__":
    main()
