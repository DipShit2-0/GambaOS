from src.gambaos.system.pyrolang import execute as exe
from src.gambaos.system.pyrolang import storage
from src.gambaos.system.GambaOS.FileManager import resource_path
import sverpykit as spk

input_bar: spk.SearchBar
text_box: spk.TextBlock

def execute(operation: str):
    text_box.change_text(
        f"{text_box.text} {operation}\n"
    )

    split_operation = operation.split(" ")
    if split_operation[0] in commands:
        if len(split_operation) > 1:
            commands[split_operation[0]](*split_operation[1:])
        else:
            commands[split_operation[0]]()
    else:
        text_box.change_text(
            f"{text_box.text}[Error] >> "
            f"Command '{split_operation[0]}' not found!\n"
        )

    text_box.change_text(
        f"{text_box.text}>> "
    )

def clear_screen():
    text_box.change_text(">> ")

def run_pyrolang_script(file: str):
    input_bar.function = lambda : None
    storage.storage = storage.Storage(text_box)
    exe.execute(resource_path(f"user/{file}"))
    input_bar.function = execute

commands = {
    "cls": clear_screen,
    "pyro": run_pyrolang_script
}