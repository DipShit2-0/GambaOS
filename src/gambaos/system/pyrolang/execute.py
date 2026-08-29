import lexer

def execute(code: str) -> None:
    lexer.main_code = code
    lexer.tokenize(code)

with open("main.pr", "r") as f:
    execute(f.read())