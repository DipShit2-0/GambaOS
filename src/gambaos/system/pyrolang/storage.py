
class Boolean:
    def __init__(self, boolean: str | bool):
        self.data = boolean # "True"=
        if isinstance(self.data, str):
            self.convert()

    @staticmethod
    def is_bool(value: str):
        return value.startswith('"') and value.endswith('"=')

    def convert(self):
        boolean = self.data[1:].split('"')[0]
        self.data = boolean == "true" or boolean == "True"

class Float:
    def __init__(self, float_: str | float):
        self.data = float_ # "4.0"-
        if isinstance(self.data, str):
            self.convert()

    @staticmethod
    def is_float(value: str) -> bool:
        return value.startswith('"') and value.endswith('"-')

    def __add__(self, other):
        return Float(self.data + other.data)

    def convert(self):
        float_ = self.data[1:]
        self.data = float(float_.split('"')[0])

class Integer:
    def __init__(self, integer: str | int):
        self.data = integer # "4"+
        if isinstance(self.data, str):
            self.convert()

    @staticmethod
    def is_int(value: str):
        return value.startswith('"') and value.endswith('"+')

    def __add__(self, other):
        if isinstance(other, Integer):
            return Integer(self.data + other.data)
        if isinstance(other, Float):
            return Float(self.data + other.data)
        return Integer(self.data + other)

    def __sub__(self, other):
        if isinstance(other, Integer):
            return Integer(self.data - other.data)
        if isinstance(other, Float):
            return Float(self.data - other.data)
        return Integer(self.data - other.data)

    def __truediv__(self, other):
        if isinstance(other, Integer) or\
                isinstance(other, Float):
            return Float(self.data / other.data)
        return Float(self.data / other)

    def __mul__(self, other):
        if isinstance(other, Integer):
            return Integer(self.data, other.data)
        if isinstance(other, Float):
            return Float(self.data, other.data)
        return Integer(self.data * other)

    def __eq__(self, value) -> Boolean:
        if isinstance(value, Integer) or\
                isinstance(value, Float):
            return Boolean(self.data == value.data)
        return Boolean(self.data == value)

    def __lt__(self, other):
        if isinstance(other, Integer) or\
                isinstance(other, Float):
            return self.data < other.data
        return self.data < other

    def __gt__(self, other):
        if isinstance(other, Integer) or\
                isinstance(other, Float):
            return self.data > other.data
        return self.data > other

    def convert(self):
        integer = self.data[1:]
        self.data = int(integer.split('"')[0])

class String:
    def __init__(self, string: str, convert=True):
        self.data = string # "abc123"!
        if convert:
            self.convert()

    @staticmethod
    def is_str(value: str):
        return value.startswith('"') and value.endswith('"!')

    def convert(self):
        string = self.data[1:]
        self.data = str(string.split('"')[0])

# FIX: Make the import at the top of the file.
class Function:
    def __init__(self, start):
        self.start = start+1

    def run(self):
        import lexer
        lexer.lexer(lexer.main_code, self.start, function=True)


class Storage:
    def __init__(self):
        self.variables = {}
        self.functions = {}

    def add_variable(self, var, val):
        self.variables[var] = val

    def add_pr_function(self, name, start):
        self.functions[name] = Function(start)
storage = Storage()