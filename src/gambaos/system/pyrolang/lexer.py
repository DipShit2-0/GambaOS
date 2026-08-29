import parser

main_code = None

def lexer(code, start: int = 0, function=False) -> None:

    lines = code.split("\n")[start:]
    skips = 0

    for count, line in enumerate(lines):
        line: str = line.strip()
        if line == "":
            continue

        if line.startswith("{"):
            skips += 1
            continue

        if line.endswith("}"):
            skips -= 1
            if function and skips == -1:
                return
            continue
        elif skips > 0:
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
        elif base_command == "func":
            token["base_command"] = "FUNC"
            token["name"] = split_line[1]
            token["line"] = count+start
            skips += 1
        else:
            token["base_command"] = "FUNCTION"
            token["action"] = base_command
            token["parameters"] = " ".join(split_line[1:])

        parser.parse(token)