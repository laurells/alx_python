class NameException(Exception):
    pass

def raise_exception_msg(message=""):
    raise NameException(message)

