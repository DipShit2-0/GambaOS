

class Integer:
    def __init__(self, integer: str):
        self.data = integer # "4"+
        self.convert()

    def convert(self):
        integer = self.data[1:]
        self.data = int(integer.split('"')[0])

class String:
    def __init__(self, string: str):
        self.data = string # "abc123"!
        self.convert()

    def convert(self):
        string = self.data[1:]
        self.data = str(string.split('"')[0])


class Storage:
    def __init__(self):
        self.variables = {}
        self.functions = {}

    def add_variable(self, var, val):
        self.variables[var] = val
storage = Storage()