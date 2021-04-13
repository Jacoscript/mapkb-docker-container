import pycurl
import json
from context import Context
from typing import Callable, List
from io import BytesIO
import pathlib
import sys

#LINUX: str = "linux"
#MACOS: str = "darwin"
WINDOWS: str = "win32"
CONTEXT_URI_PLACEHOLDER: str = "%CONTEXT_URL%"
EXPORT_URL: str = f"http://144.47.161.52:8080/marmotta/export/download?context={CONTEXT_URI_PLACEHOLDER}" \
                   "&format=text%2Fturtle"
GET_CONTEXTS_URL: str = "http://144.47.161.52:8080/marmotta/context/list?labels=true"
MARMOTTA_CONTEXT_ENCODING = "utf-8"
EXPORT_FOLDER_V1 = "export\\" if sys.platform == WINDOWS else "export/"
EXPORT_FOLDER_V2 = "export\\v2\\" if sys.platform == WINDOWS else "export/v2/"
EXT = ".ttl"


def get_contexts(c: pycurl.Curl = None, buffer: BytesIO = None) -> List[Context]:
    if c is None:
        c = pycurl.Curl()
    if buffer is None:
        buffer = BytesIO()
    contexts: List[Context] = []
    body = __curl(GET_CONTEXTS_URL, buffer, c)
    context_dict = json.loads(body)
    for i in context_dict:
        context = Context(**i)
        if Context.V2 in context.uri:
            context.version = Context.V2
        contexts.append(context)

    return contexts


def export_context(context: Context, c: pycurl.Curl = None, buffer: BytesIO = None) -> str:
    if c is None:
        c = pycurl.Curl()
    if buffer is None:
        buffer = BytesIO()
    data = __curl(EXPORT_URL.replace(CONTEXT_URI_PLACEHOLDER, context.uri), buffer, c)
    body: str = data.decode(MARMOTTA_CONTEXT_ENCODING)
    return body


def export_contexts(contexts: List[Context],
                    save_func: Callable[[Context, str], None] = lambda a, b: None) -> None:
    for i in contexts:
        try:
            body = export_context(i)
            save_func(i, body)
        except:
            print(f"Unable to export ${i.label}", file=sys.stderr)


def save_exported_context(context: Context, body: str) -> None:
    filename: str
    if context.version == Context.V1:
        filename = f"{EXPORT_FOLDER_V1}{context.label}{EXT}"
    else:
        filename = f"{EXPORT_FOLDER_V2}{context.label}{EXT}"
    f = open(filename, "w")
    f.write(body)
    f.close()
    context.export_file = filename


def __curl(url: str, buffer: BytesIO = None, c: pycurl.Curl = None) -> bytes:

    if buffer is None:
        buffer = BytesIO()
    if c is None:
        c = pycurl.Curl()

    c.setopt(c.URL, url)
    c.setopt(c.WRITEDATA, buffer)
    c.perform()
    c.close()
    return buffer.getvalue()


def __create_export_folders():
    path = pathlib.Path(EXPORT_FOLDER_V1)
    path.mkdir(parents=True, exist_ok=True)
    path = pathlib.Path(EXPORT_FOLDER_V2)
    path.mkdir(parents=True, exist_ok=True)


def main():
    __create_export_folders()
    contexts: List[Context] = get_contexts()
    export_contexts(contexts, save_exported_context)


if __name__ == "__main__":
    main()
