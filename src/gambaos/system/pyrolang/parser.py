import Builtins, runtime, storage

def parse_value(value):
    value = value.strip()
    if value.endswith('"!'):
        return storage.String(value)
    if value.endswith('"+'):
        return storage.Integer(value)
    if value.endswith("="):
        return storage.Boolean(value)
    if value in storage.storage.variables.keys():
        return storage.storage.variables[value]
    raise ValueError(f"Unrecognized data-type '{value[-1]}'.")

def parse_expression(expression: str) -> bool:

    token = []

    for c, char in enumerate(expression):
        if char == ">":
            token.append(char)
        else:
            continue
        token.append(expression[:c])

    for key in token:
        if key == ">":
            pass
    return True

def parse_parameters(parameters: str):
    save = None
    parameters = parameters.strip()[1:].split(";")
    if not parameters[-1].strip().endswith(")"):
        function_end = parameters[-1].rfind(") -> ")
        save = parameters[-1][function_end+5:]
        parameters[-1] = parameters[-1][:function_end]
    else:
        parameters[-1] = parameters[-1][:-1]
    values = []

    # Change values to their own class.
    for parameter in parameters:
        values.append(parse_value(parameter))

    return {
        "values": values,
        "save": save
    }

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
    elif token["base_command"] == "IF":
        expression = token["expression"].strip()
        if not (expression.startswith("[") and expression.endswith("]")):
            return
        expression = expression[1:-1]
        if not parse_expression(expression):
            return
        evaluation = token["evaluation"].strip()
        if not (evaluation.startswith("_") and evaluation.endswith("_")):
            raise SyntaxError("Evaluations must start and end with '_'.")
        evaluation = evaluation[1:-1].split(' ')
        name = evaluation[0]
        arguments = evaluation[1]
        payload = parse_parameters(arguments)
        func = storage.storage.functions[name]
        save = payload["save"]
        values = payload["values"]
    elif token["base_command"] == "FUNCTION":
        func = storage.storage.functions[token["action"]]
        payload = parse_parameters(token["parameters"])
        save = payload["save"]
        values = payload["values"]

    runtime.run(func, *values, save=save)