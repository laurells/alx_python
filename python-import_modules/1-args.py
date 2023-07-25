import sys

def print_arguments(args):
    num_args = len(args)

    print(f"Number of argument(s): {num_args}", end='')
    if num_args == 0:
        print(".")
    elif num_args == 1:
        print(f", argument: {args[0]}")
        print("1:", args[0])
    else:
        print(f", arguments: {', '.join(args)}")
        for i, arg in enumerate(args, 1):
            print(f"{i}: {arg}")

if __name__ == "__main__":
    arguments = sys.argv[1:]
    print_arguments(arguments)
