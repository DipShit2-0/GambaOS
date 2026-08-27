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

# Quite useless builtins
## Those can be used in some cases to do things the difficult way
def _switch(i: int):
    if i == 0:
        i == 1
        return 1
    else:
        i == 0
        return 0

# Print output
def _out(i: str):
    print(i)