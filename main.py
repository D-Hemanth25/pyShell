import sys

def print(content):
    sys.stdout.write(content + "\n")
    return 0


def main():
    while True:
        sys.stdout.write("$ ")
        
        command = input()
        print(command + ": command not found")

if __name__ == "__main__":
    main()
