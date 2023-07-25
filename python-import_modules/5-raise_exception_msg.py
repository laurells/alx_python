class NameException(Exception):
    pass

def raise_exception_msg(message=""):
    raise NameException(message)

if __name__ == "__main__":
    try:
        message = "C is fun"
        raise_exception_msg(message)
    except NameException as e:
        print(str(e))
