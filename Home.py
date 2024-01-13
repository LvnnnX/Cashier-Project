from libs import *
from importer import *

dummy_data = {
    0: {"name": "Apple", "description": "Red and juicy", "quantity": 5, "price": 1.99},
    1: {
        "name": "Bread",
        "description": "Whole wheat loaf",
        "quantity": 2,
        "price": 3.49,
    },
    2: {
        "name": "Milk",
        "description": "Organic whole milk",
        "quantity": 1,
        "price": 2.99,
    },
    3: {
        "name": "Carrot",
        "description": "Fresh and crunchy",
        "quantity": 10,
        "price": 0.99,
    },
    4: {
        "name": "Eggs",
        "description": "Free-range brown eggs",
        "quantity": 12,
        "price": 2.79,
    },
    5: {
        "name": "Chicken",
        "description": "Boneless skinless breasts",
        "quantity": 2,
        "price": 7.99,
    },
    6: {
        "name": "Banana",
        "description": "Ripe and yellow",
        "quantity": 6,
        "price": 0.49,
    },
}


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
        width=500,
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
    # "border_radius" : border_radius.only(top_left=15, top_right=15),
    "padding" : padding.only(left=15,right=15)
}


class Header(Container):
    def __init__(self, dt: DataTable) -> None:
        super().__init__(**header_style,
                        #  on_hover=self.toggle_search
                        )
        self.dt = dt

        self.search_value:TextField = search_field(self)
        
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


class Controller:
    items = dummy_data
    counter = len(items)
    
    @staticmethod
    def get_items():
        return Controller.items
    
    @staticmethod
    def add_item(data: dict):
        Controller.counter += 1
        Controller.items[Controller.counter] = data
        
        
column_names = ["Column One", "Column Two", "Column Three", "Column Four"]

data_table_style = {
    "expand" : True,
    "border_radius" : 8,
    "border" : border.all(2, '#ebebeb'),
    "horizontal_lines" : border.BorderSide(1, "#ebebeb"),
    "columns" : [
        DataColumn(Text(index, size=12, color='black', weight='bold')) for index in column_names
    ]
}        

class Data_Table(DataTable):
    def __init__(self):
        super().__init__(**data_table_style)
        self.df = Controller.get_items()
        
    def fill_data_table(self):
        self.rows = []
        
        for values in self.df.values():
            data = DataRow()
            data.cells = [
                DataCell(Text(value, color='black' )) for value in values.values()
            ]

            self.rows.append(data)

        self.update()


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
    
    table = Data_Table()
    searchbar_header = Header(dt=table)
    
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
                    content=Column(
                        [
                            searchbar_header,
                            Divider(height=2, color='transparent'),
                            Column(
                                scroll='hidden',
                                expand=True,
                                controls=[Row(controls=[table])]
                            )
                        ]
                    )
                )
            ]
        )
    )
    
    page.add(mainpage)
    
    table.fill_data_table()
    
    

app(target=main)#