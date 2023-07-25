import sys

def print_arguments(args):
    num_args = len(args)

    if num_args == 0:
        print("0 arguments")
    elif num_args == 1:
        print("1 argument:")
        print("1:", args[0])
    else:
        print(f"{num_args} arguments:")
        for i, arg in enumerate(args, 1):
            print(f"{i}: {arg}")

if __name__ == "__main__":
    arguments = sys.argv[1:]
    print_arguments(arguments)
