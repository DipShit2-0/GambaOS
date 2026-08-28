import Builtins, runtime, storage

def parse_value(value):
    value = value.strip()
    if value.endswith('"!'):
        return storage.String(value)
    if value.endswith('"+'):
        return storage.Integer(value)
    if value.endswith("="):
        return storage.Boolean(value)
    if value.endswith("#"):
        return storage.List(value)
    if value in storage.storage.variables.keys():
        return storage.storage.variables[value]
    raise ValueError(f"Unrecognized data-type '{value[-1]}'.")

def parse(token: dict):
    # print(token)

    func = lambda : None
    values = []
    save: str | None = None

    if token["base_command"] == "GET":
        func = Builtins.builtins_.load_builtin
        values = [token["action"]]
    elif token["base_command"] == "SET":
        func = storage.storage.add_variable
        split_action = token["action"].strip().split(" ")
        values = [split_action[0], parse_value(split_action[1])]
    elif token["base_command"] == "FUNCTION":
        func = storage.storage.functions[token["action"]]
        parameters = token["parameters"].strip()[1:].split(";")
        if not parameters[-1].strip().endswith(")"):
            function_end = parameters[-1].rfind(") -> ")
            save = parameters[-1][function_end+5:]
            parameters[-1] = parameters[-1][:function_end]
        else:
            parameters[-1] = parameters[-1][:-1]
        values = []
        for parameter in parameters:
            values.append(parse_value(parameter))

    runtime.run(func, *values, save=save)