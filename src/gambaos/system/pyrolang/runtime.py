import Builtins, storage

def run(func, *values, save: str | None = None):
    val = func(*values)
    print(val, func, save)
    if save:
        if isinstance(val, storage.Integer) or\
                isinstance(val, storage.String) or\
                isinstance(val, storage.Float) or\
                isinstance(val, storage.Boolean) or\
                isinstance(val, storage.List):
            storage.storage.add_variable(save, val)
    # print(storage.storage.variables)