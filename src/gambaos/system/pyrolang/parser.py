import Builtins, runtime, storage

def parse(token):

    func = lambda : None
    values = []

    if token["base_command"] == "GET":
        func = Builtins.builtins_.load_builtin
        values = [token["action"]]
    elif token["base_command"] == "FUNCTION":
        func = storage.storage.functions[token["action"]]
        parameters = token["parameters"].strip()[1:-1].split(";")
        values = []
        for parameter in parameters:
            text = parameter.strip()[1:]
            text = text[:text.find('"')]
            values.append(text)

    runtime.run(func, *values)