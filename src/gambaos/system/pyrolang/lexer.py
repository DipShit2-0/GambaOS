import parser

def lexer(code) -> None:

    lines = code.split("\n")

    for line in lines:
        line = line.strip()
        if line == "":
            continue

        split_line = line.split(" ")
        remove_empties = 0
        for line in split_line:
            if line.strip() == "":
                remove_empties += 1
        for _ in range(remove_empties):
            split_line.remove("")
        base_command = split_line[0]

        token = {
            "base_command": base_command
        }

        if base_command == "GET":
            token["action"] = split_line[1]
        elif base_command == "SET":
            token["action"] = " ".join(split_line[1:])
        elif base_command == "if":
            token["base_command"] = "IF"
            token["expression"] = split_line[1]
            token["evaluation"] = " ".join(split_line[2:4])
        else:
            token["base_command"] = "FUNCTION"
            token["action"] = base_command
            token["parameters"] = " ".join(split_line[1:])

        parser.parse(token)