import pathlib
import sys
from typing import List
from typing import Tuple
from glob import glob
import re
from io import StringIO
from time import time
from context import Context

RUN_CHECKPOINT = False
WINDOWS: str = "win32"
EXPORT_FOLDER_V1: str = "export\\" if sys.platform == WINDOWS else "export/"
EXPORT_FOLDER_V2: str = "export\\v2\\" if sys.platform == WINDOWS else "export/v2/"
IMPORT_FOLDER: str = "import\\" if sys.platform == WINDOWS else "import/"
GRAPH_URI: str = "$GRAPH_URI"
FILENAME: str = "$FILENAME"
QUERY_V1: str = f"ld_dir_all('/export', '{GRAPH_URI}.ttl', 'http://data.usgs.gov/{GRAPH_URI}');\n"
QUERY_V2: str = f"ld_dir_all('/export/v2', '{GRAPH_URI}.ttl', 'http://data.usgs.gov/{GRAPH_URI}');\n"
RDF_LOADER_RUN = "rdf_loader_run();\n"
CHECKPOINT = "checkpoint;\n"
GLOB_STRING_V1: str = f"{EXPORT_FOLDER_V1}*.*"
GLOB_STRING_V2: str = f"{EXPORT_FOLDER_V2}*.*"
graphs: List[Tuple[str, str, str]] = []


def create_import_folder() -> None:
    path = pathlib.Path(IMPORT_FOLDER)
    path.mkdir(parents=True, exist_ok=True)


def parse_filenames() -> Tuple[List[str], List[str]]:
    files: Tuple[List[str], List[str]] = ([], [])
    files_v1 = glob(GLOB_STRING_V1)
    win_export_folder_v1 = EXPORT_FOLDER_V1.replace("\\", "\\\\")
    win_export_folder_v2 = EXPORT_FOLDER_V2.replace("\\", "\\\\")
    regex: str = f"{win_export_folder_v1}(.*?\\.ttl)" if sys.platform == WINDOWS else f"{EXPORT_FOLDER_V1}(.*?\\.ttl)"
    for idx, i in enumerate(files_v1):
        match = re.search(regex, i)
        files_v1[idx] = match.group(1)

    files_v2 = glob(GLOB_STRING_V2)
    regex: str = f"{win_export_folder_v2}(.*?\\.ttl)" if sys.platform == WINDOWS else f"{EXPORT_FOLDER_V2}(.*?\\.ttl)"
    for idx, i in enumerate(files_v2):
        match = re.search(regex, i)
        files_v2[idx] = match.group(1)
    files = (files_v1, files_v2)
    return files


def __create_graph_iri(filename, version) -> Tuple[str, str]:
    if version != Context.V1 and version != Context.V2:
        print(f"Version must be {Context.V1} or {Context.V2}, default to {Context.V1}", file=sys.stderr)
        version = Context.V1
    regex: str = "(.*?).ttl"
    match = re.search(regex, filename)
    iri = match.group(1);
    if version == Context.V2:
        iri = f"{version}/{iri}"
    return filename, iri, version


def create_graph_tuples(filenames: Tuple[List[str], List[str]]) -> None:
    for i in filenames[0]:
        graphs.append(__create_graph_iri(i, Context.V1))

    for i in filenames[1]:
        graphs.append(__create_graph_iri(i, Context.V2))


def create_query(checkpoint: bool = True) -> str:
    query: StringIO = StringIO()
    for i in graphs:
        if i[2] == Context.V1:
            query.write(QUERY_V1.replace(GRAPH_URI, i[1]))
        elif i[2] == Context.V2:
            query.write(QUERY_V2.replace(GRAPH_URI, i[1]).replace(f"{Context.V2}/", "", 1))
    query.write(RDF_LOADER_RUN)
    if checkpoint:
        query.write(CHECKPOINT)
    return query.getvalue()


def save_query(query: str) -> None:
    file = open(f"{IMPORT_FOLDER}import_{time()}.sql", 'w')
    file.write(query)
    file.close()


def main():
    create_import_folder()
    filenames = parse_filenames()
    create_graph_tuples(filenames)
    query = create_query(RUN_CHECKPOINT)
    save_query(query)


if __name__ == "__main__":
    main()
