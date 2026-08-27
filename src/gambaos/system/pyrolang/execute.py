import lexer

def execute(code: str) -> None:
    lexer.lexer(code)

with open("main.pr", "r") as f:
    execute(f.read())