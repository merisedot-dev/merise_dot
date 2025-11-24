import os


def check_script(context, f_name: str) -> None:
    contents: str = ""
    with open(f"{os.getcwd()}/features/assets/{f_name}.sql", 'r') as file:
        contents = file.read().strip().replace('    ', '\t') # space constraint
    output: str = str(context.script)
    print(output)
    assert output == contents
