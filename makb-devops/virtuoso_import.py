import pathlib
import sys
from typing import List
from typing import Tuple
WINDOWS: str = "win32"
IMPORT_FOLDER: str = "import\\" if sys.platform == WINDOWS else "import/"
GRAPH_URI: str = "$GRAPH_URI"
QUERY: str = f"ld_dir_all('/export', '${GRAPH_URI}.ttl', 'http://data.usgs.gov/${GRAPH_URI}.ttl');"
graphs: List[Tuple[str, str]] = []

def __create_import_folder():
    path = pathlib.Path(IMPORT_FOLDER)
    path.mkdir(parents=True, exist_ok=True)


# TODO: Parse file names in /export folder to get list of graph URIs
# TODO: Build SQL file to call RDF loader for each ttl file
# TODO: Export SQL file to be run against isql