import Builtins, runtime, storage

def parse_value(value):
    value = value.strip()
    if value.endswith('"!'):
        return storage.String(value)
    if value.endswith('"+'):
        return storage.Integer(value)
    raise ValueError(f"Unrecognized data-type '{value[-1]}'.")

def parse(token):
    # print(token)

    func = lambda : None
    values = []

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
        print(parameters)
        values = []
        for parameter in parameters:
            text = parameter.strip()[1:]
            text = text[:text.find('"')]
            values.append(text)

    runtime.run(func, *values)