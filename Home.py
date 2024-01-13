from libs import *
from importer import *

def search_field(function: callable):
    return TextField(
        border_color='transparent',
        height=20,
        text_size=14,
        content_padding=0,
        cursor_color='white',
        cursor_width=1,
        color='white',
        hint_text='Search',
        on_change=function,
    )


def search_bar(control: TextField):
    return Container(
        width=350,
        bgcolor='white10',
        border_radius=6,
        opacity=0,
        animate_opacity=300,
        padding=8,
        content=Row(
            spacing=10,
            vertical_alignment='center',
            controls=[
                Icon(
                    name=icons.SEARCH_ROUNDED,
                    size=17,
                    opacity=0.85,
                ),
                control,
            ]
        )
    )
    
header_style = {
    "height" : 60,
    "bgcolor" : "#081d33",
    "border_radius" : border_radius.only(top_left=15, top_right=15),
    "padding" : padding.only(left=15,right=15)
}


class Header(Container):
    def __init__(self) -> None:
        super().__init__(**header_style,
                        #  on_hover=self.toggle_search
                        )
        
        self.search_value:TextField = search_field(None)
        
        self.search = search_bar(self.search_value)
        
        self.name = Text("Search Bar")
        self.avatar = IconButton("Person")
        
        self.content = Row(
            alignment='spaceBetween',
            controls=[self.name, self.search, self.avatar]
        )
        
        self.search.opacity=1
    
    # def toggle_search(self, e:HoverEvent):
    #     self.search.opacity = 1 if e.data == 'true' else 0
    #     self.search.update()


    
    def filter_dt_rows(self, e):
        ...

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
                # Text(
                #     value="Home",
                #     size=30,
                #     left=OS_WIDTH/2,
                #     top=10,
                #     color=colors['Text']
                # )
                
            ]
        )
    )
    
    page.add(header)
    
    searchbar_header = Header()
    
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
                    content=Stack(
                        [
                            Text(
                            value="Form Input",
                            size=30,
                            left=OS_WIDTH/4 - 100,
                            top=50,
                            color=colors['Text']
                            ),
                            
                            #Diisi tabel list pesanannya disini
                            #Fitur jangan lupa Admin & Kasir
                            #Refund & Void
                            #Tambah kurang barang
                            #Laporan Bulanan
                            #Juml Barang Keluar & Nama Sales
                            #Promo
                            
                            
                        ]
                    )
                    
                ),
                Container(
                    left=(OS_WIDTH/2),
                    width=OS_WIDTH/2,
                    height=OS_HEIGHT-50,
                    bgcolor=colors['B_Bg'],
                    content=Stack(
                        [
                            searchbar_header,
                            # Divider(height=2, color='transparent'),
                            Column(
                                scroll='hidden',
                                expand=True,
                                controls=[Row(controls=[])]
                            )
                        ]
                    )
                )
            ]
        )
    )
    
    page.add(mainpage)
    
    

app(target=main)#