from utils.libs import *
def load_colors(Path=JSONPATH) -> dict:
    f = open(f"{Path}/bgcolors.json")
    colors = json.load(f)
    return colors

def get_screen_size():
    monitor = get_monitors()[0]
    return monitor.width, monitor.height