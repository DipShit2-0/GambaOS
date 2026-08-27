# Built-in mathematical functions
## These functions are translated and parsed through Pyrolang
def _equals(a, b):
    return a == b

def _med(a, b):
    return (a + b) / 2

def _add(a, b):
    return a + b

def _subtract(a, b):
    return a - b

def _multiply(a, b):
    return a * b

def _divide(a, b):
    return a / b

def _out(i: str):
    print(i)