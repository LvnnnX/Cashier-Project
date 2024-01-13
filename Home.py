from libs import *
from importer import *

def main(page: Page):
    colors = load_colors()
    page.title = "Home"
    
    OS_SIZE = get_monitors()[0]
    OS_WIDTH, OS_HEIGHT = OS_SIZE.width, OS_SIZE.height
    
    header = Container(
        width=OS_WIDTH,
        height=50,
        bgcolor=colors['White'],
        border_radius=10,
        content=Stack(
            [
                # Yang mau diisi di bagian Header
                
            ]
        )
    )
    
    page.add(header)
    
    mainpage = Container(
        width=OS_WIDTH,
        height=OS_HEIGHT-50,
        bgcolor=colors['W_Bg'],
        border_radius=10,
        content=Stack(
            [
                # Yang mau diisi di bagian main page
                Container(
                    left=0,
                    width=OS_WIDTH/2,
                    height=OS_HEIGHT-50,
                    bgcolor=colors['W_Bg'],
                ),
                Container(
                    left=OS_WIDTH/2,
                    width=OS_WIDTH/2,
                    height=OS_HEIGHT-50,
                    bgcolor=colors['B_Bg'],
                )
            ]
        )
    )
    
    page.add(mainpage)
    
    

app(target=main)