from sys import stderr
class Context:
    label: str = "",
    uri: str = "",
    size: int = 0
    export_file: str = ""
    version: str
    V1: str = "v1"
    V2: str = "v2"

    def __init__(self, label: str, uri: str, size: int, version: str):
        self.label = label
        self.uri = uri
        self.size = size
        if version == Context.V1 or version == Context.V2:
            self.version = version
        else:
            print(f"Version must be {Context.V1} or {Context.V2}, defaulting to {Context.V1}", file=stderr)
            self.version = Context.V1
