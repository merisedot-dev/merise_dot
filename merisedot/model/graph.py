class Graph:
    # TODO write attributes

    def __init__(self, path: str) -> None:
        contents: str = ""
        with open(path, 'r') as file:
            contents = file.read()
