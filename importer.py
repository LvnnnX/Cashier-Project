from libs import *
JSONPATH = Path(__file__).parent / 'json'
def load_colors(Path=JSONPATH) -> dict:
    f = open(f"{Path}/bgcolors.json")
    colors = json.load(f)
    return colors