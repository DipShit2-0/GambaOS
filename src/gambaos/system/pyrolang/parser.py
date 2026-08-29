import Builtins, runtime, storage

number_operations = "<>-+*/"
operations = "<>-+*/="

def parse_value(value):
    value = value.strip()
    if value.endswith('"!'):
        return storage.String(value)
    if value.endswith('"+'):
        return storage.Integer(value)
    if value.endswith('"-'):
        return storage.Float(value)
    if value.endswith('"='):
        return storage.Boolean(value)
    if value in storage.storage.variables.keys():
        return storage.storage.variables[value]
    raise ValueError(f"Unrecognized data-type '{value[-1]}'.")

def parse_expression(expression: str) -> bool:

    token = []

    last_count = 0
    for c, char in enumerate(expression):
        if char == ">":
            token.append(expression[:c])
            token.append(char)
        else:
            continue
        last_count = c
    token.append(expression[last_count+1:])


    for c, key in enumerate(token):

        if key not in operations:
            continue

        last_value = parse_value(token[c-1])
        next_value = parse_value(token[c+1])

        if key in number_operations and not (
            isinstance(last_value, storage.Integer) or
            isinstance(last_value, storage.Float)
        ) and not (
            isinstance(next_value, storage.Integer) or
            isinstance(next_value, storage.Float)
        ):
            raise TypeError(f"Invalid data type(s) for operator '{key}'.")

        if key == ">":
            if not (last_value > next_value):
                return False
    return True

def parse_parameters(parameters: str):
    if parameters.strip() == "()":
        return {
            "values": [],
            "save": None
        }
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
    elif token["base_command"] == "FUNC": # Creation
        func = storage.storage.add_pr_function
        values = [token["name"], token["line"]]
    elif token["base_command"] == "FUNCTION": # Calling
        func = storage.storage.functions[token["action"]]
        if isinstance(func, storage.Function):
            func = func.run
        payload = parse_parameters(token["parameters"])
        save = payload["save"]
        values = payload["values"]

    runtime.run(func, *values, save=save)