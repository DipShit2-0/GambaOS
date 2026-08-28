
class Boolean:
    def __init__(self, boolean: str | bool):
        self.data = boolean # "True"=
        if isinstance(self.data, str):
            self.convert()

    def convert(self):
        boolean = self.data[1:].split('"')[0]
        self.data = boolean == "true" or boolean == "True"

class Float:
    def __init__(self, float_: str | float):
        self.data = float_ # "4.0"-
        if isinstance(self.data, str):
            self.convert()

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

    def convert(self):
        integer = self.data[1:]
        self.data = int(integer.split('"')[0])

class String:
    def __init__(self, string: str, convert=True):
        self.data = string # "abc123"!
        if convert:
            self.convert()

    def convert(self):
        string = self.data[1:]
        self.data = str(string.split('"')[0])

class List:
    def __init__(self, list: str | list):
        self.data = list # ["a", "b", "c"]#
        if isinstance(self.data, str):
            self.convert()
        
    def convert(self):
        list = self.data.strip("[]").replace('"', '').split(', ')
        self.data = list


class Storage:
    def __init__(self):
        self.variables = {}
        self.functions = {}

    def add_variable(self, var, val):
        self.variables[var] = val
storage = Storage()

test = List("(\"a\", \"b\", \"c\")")
print(test)