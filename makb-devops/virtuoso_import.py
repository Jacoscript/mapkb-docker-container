import pathlib
import sys
from typing import List
from typing import Tuple
from glob import glob
import re
from io import StringIO
from time import time

WINDOWS: str = "win32"
EXPORT_FOLDER: str = "export\\" if sys.platform == WINDOWS else "export/"
IMPORT_FOLDER: str = "import\\" if sys.platform == WINDOWS else "import/"
GRAPH_URI: str = "$GRAPH_URI"
QUERY: str = f"ld_dir_all('/export', '{GRAPH_URI}.ttl', 'http://data.usgs.gov/{GRAPH_URI}');\n"
RDF_LOADER_RUN = "rdf_loader_run();\n"
CHECKPOINT = "checkpoint;\n"
GLOB_STRING: str = f"{EXPORT_FOLDER}*.*"
graphs: List[Tuple[str, str]] = []


def create_import_folder() -> None:
    path = pathlib.Path(IMPORT_FOLDER)
    path.mkdir(parents=True, exist_ok=True)


def parse_filenames() -> List[str]:
    files = glob(GLOB_STRING)
    regex: str = f"{EXPORT_FOLDER}\\(.*?\\.ttl)" if sys.platform == WINDOWS else f"{EXPORT_FOLDER}(.*?\\.ttl)"
    for idx, i in enumerate(files):
        match = re.search(regex, i)
        files[idx] = match.group(1)
    return files


def __create_graph_iri(filename) -> Tuple[str, str]:
    regex: str = "(.*?).ttl"
    match = re.search(regex, filename)
    return filename, match.group(1)


def create_graph_tuples(filenames: List[str]) -> None:
    for i in filenames:
        graphs.append(__create_graph_iri(i))


def create_query() -> str:
    query: StringIO = StringIO()
    for i in graphs:
        query.write(QUERY.replace(GRAPH_URI, i[1]))
    query.write(RDF_LOADER_RUN)
    query.write(CHECKPOINT)
    return query.getvalue()


def save_query(query: str) -> None:
    file = open(f"{IMPORT_FOLDER}import_{time()}.sql", 'w')
    file.write(query)


def main():
    create_import_folder()
    filenames = parse_filenames()
    create_graph_tuples(filenames)
    query = create_query()
    save_query(query)


if __name__ == "__main__":
    main()
