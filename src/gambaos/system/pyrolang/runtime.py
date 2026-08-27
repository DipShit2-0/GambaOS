import Builtins, storage

def run(func, *values):
    func(*values)
    # print(storage.storage.variables)