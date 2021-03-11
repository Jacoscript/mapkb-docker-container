class Context:
    label: str = "",
    uri: str = "",
    size: int = 0
    export_file: str = ""

    def __init__(self, label: str, uri: str, size: int):
        self.label = label
        self.uri = uri
        self.size = size
