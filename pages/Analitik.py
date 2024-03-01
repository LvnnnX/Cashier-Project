import sys

sys.path.append("../")
from utils.libs import *
from utils.importer import *
from utils.converter import *

def main(view: View, super_page: Page):
    colors = load_colors()
    
    body = Container(
        content=Column(),
        bgcolor=colors["Gray/50"],
        width=super_page.window_width,
        height=super_page.window_height - 150,
        padding=padding.only(
            top=super_page.window_height / 100 * 2,
            left=super_page.window_width / 100 * 5,
            right=super_page.window_width / 100 * 5,
        ),
    )

    view.controls.append(body)