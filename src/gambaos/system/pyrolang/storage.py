

class Integer:
    def __init__(self, integer: str):
        self.data = integer # "4"+

    def convert(self):
        integer = self.data[1:]
        self.data = int(integer.split('"')[0])


class Storage:
    def __init__(self):
        self.variables = {}
        self.functions = {}
storage = Storage()