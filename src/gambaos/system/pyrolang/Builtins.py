import storage

# All Built-in methods that are used for PyroLang.
def _add(*values):
    val = storage.Integer(values[0])
    for v in values[1:]: val += v
    return val.data

def _subtract(*values):
    val = storage.Integer(values[0])
    for v in values[1:]: val -= v
    return val.data

def _multiply(*values):
    val = storage.Integer(values[0])
    for v in values[1:]: val *= v
    return val.data

def _divide(*values):
    val = storage.Integer(values[0])
    for v in values[1:]: val /= v
    return val.data

def _equals(a, b):
    return a == b

def _avg(*values):
    return _add(*values) / len(values)

def is_printable_value(value):
    return isinstance(value, storage.String)\
        or isinstance(value, storage.Integer)\
        or isinstance(value, storage.Float)\
        or isinstance(value, storage.Boolean)

def _out(*values, end=True):
    for val in values:
        if is_printable_value(val):
            print(val.data, end=" ")
    if end:
        print()

def _in(*values):
    _out(*values, end=False)
    return storage.String(input(), convert=False)

class Builtins:
    def __init__(self):
        self.methods = {
            "eq": _equals,
            "avg": _avg,
            "add": _add,
            "sub": _subtract,
            "mult": _multiply,
            "div": _divide,
            "out": _out,
            "in": _in
        }

    def load_builtin(self, name):
        if name not in list(self.methods.keys()):
            raise ValueError(f"Method '{name}' does not exist.")
        storage.storage.functions[name] = self.methods[name]
builtins_ = Builtins()