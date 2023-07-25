import sys

def print_arguments(args):
    num_args = len(args)

    print("Number of argument(s):", num_args)
    if num_args == 0:
        return
    elif num_args == 1:
        print("1:", args[0])
    else:
        for i, arg in enumerate(args, 1):
            print(f"{i}: {arg}")

if __name__ == "__main__":
    arguments = sys.argv[1:]
    print_arguments(arguments)
