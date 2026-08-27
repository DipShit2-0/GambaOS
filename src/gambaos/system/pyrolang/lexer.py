import parser

def lexer(code) -> None:

    lines = code.split("\n")

    for line in lines:

        split_line = line.split(" ")
        base_command = split_line[0]

        token = {
            "base_command": base_command
        }

        if base_command == "GET":
            token["action"] = split_line[1]
        else:
            token["base_command"] = "FUNCTION"
            token["action"] = base_command
            token["parameters"] = " ".join(split_line[1:])

        parser.parse(token)