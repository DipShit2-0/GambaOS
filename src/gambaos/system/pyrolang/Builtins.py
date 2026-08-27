import storage

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

def _out(*values):
    print(*values)

class Builtins:
    def __init__(self):
        self.methods = {
            "eq": _equals,
            "med": _med,
            "add": _add,
            "sub": _subtract,
            "mult": _multiply,
            "div": _divide,
            "out": _out
        }

    def load_builtin(self, name):
        if name not in list(self.methods.keys()):
            raise ValueError(f"Method '{name}' does not exist.")
        storage.storage.functions[name] = self.methods[name]
builtins_ = Builtins()