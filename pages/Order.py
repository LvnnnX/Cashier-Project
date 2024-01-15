import sys

sys.path.append("../")
from utils.libs import *
from utils.importer import *


def search_field(function: callable, colors, width):
    return TextField(
        border_color="transparent",
        width=width,
        height=20,
        text_size=14,
        content_padding=0,
        cursor_color=colors["Primary/900"],
        cursor_width=1,
        color=colors["Primary/900"],
        hint_text="Cari Barang",
        on_change=function,
        hint_style=TextStyle(color=colors["Primary/900"]),
    )


def search_bar(control: TextField, colors=colors, width=500):
    return Container(
        width=width,
        bgcolor=colors["Primary/100"],
        border_radius=14,
        opacity=0,
        animate_opacity=300,
        padding=8,
        # margin=margin.only(left=20),
        content=Row(
            spacing=10,
            vertical_alignment="center",
            controls=[
                Container(
                    margin=margin.only(left=15),
                    content=Icon(
                        name=icons.SEARCH_ROUNDED,
                        size=17,
                        opacity=0.85,
                        color=colors["Primary/900"],
                    ),
                ),
                Container(margin=margin.only(left=0), content=control),
            ],
        ),
    )


class Header(Container):
    def __init__(self, width, colors, header_style) -> None:
        super().__init__(
            **header_style,
            #  on_hover=self.toggle_search
        )
        self.width = width
        self.search_value: TextField = search_field(self, colors, width=self.width)

        self.search = search_bar(
            self.search_value, colors=colors, width=self.width * 2 / 3
        )

        self.name = Text("")
        self.avatar = IconButton("Person")

        self.content = Container(
            Column(
                [
                    Column(
                        [
                            Container(
                                width=self.width / 2,
                                margin=margin.only(top=20),
                                content=Row(
                                    controls=[
                                        Container(
                                            margin=margin.only(left=0),
                                            content=Text(
                                                "Varian Kopi",
                                                color=colors["Black"],
                                                size=30,
                                                weight="bold",
                                            ),
                                        ),
                                        Container(
                                            margin=margin.only(
                                                self.width - (self.width / 1.5)
                                            ),
                                            content=Text("2 Varian Kopi Tersedia"),
                                        ),
                                    ]
                                ),
                            ),
                            Container(margin=margin.only(top=20), content=self.search),
                        ]
                    ),
                ]
            )
        )

        self.search.opacity = 1


def main(page: Page):
    colors = load_colors()
    page.title = "Home"
    page.bgcolor = colors["White"]

    OS_SIZE = get_monitors()[0]
    OS_WIDTH, OS_HEIGHT = OS_SIZE.width, OS_SIZE.height
    
    page.window_width=OS_WIDTH
    page.window_height=OS_HEIGHT
    # page.window_full_screen = True
    page.window_focused = True

    header = Container(
        width=OS_WIDTH,
        height=50,
        bgcolor=colors["White"],
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
        ),
    )

    page.add(header)

    header_style = {
        "width": OS_WIDTH / 2,
    }
    searchbar_header = Header(
        width=OS_WIDTH / 2, colors=colors, header_style=header_style
    )

    # for each item, width 250, height 250
    def get_items(N: int = 10):
        items_list = []
        for i in range(N):
            items_list.append(
                Container(
                    width=300,
                    height=200,
                    bgcolor=colors["Primary/100"],
                    border_radius=16,
                    content=Container(
                        content=Column(
                            controls=[
                                Row(
                                    controls=[
                                        Container(
                                            margin=margin.only(left=15, top=15),
                                            width=100,
                                            # bgcolor=colors["B_Bg"],
                                            content=Image(
                                                src=IMGPATH / "dummy-order1.png"
                                            ),
                                        ),
                                        Container(
                                            width=300 - 100,
                                            # bgcolor=colors["B_Bg"],
                                            content=Column(
                                                [
                                                    Container(
                                                        margin=margin.only(top=10),
                                                        alignment=alignment.center_left,
                                                        content=Text(
                                                            value="Kopi Robusta",
                                                            font_family="Poppins",
                                                            size=20,
                                                            color=colors["Black"],
                                                            weight="bold",
                                                        ),
                                                    ),
                                                    Container(
                                                        # margin=margin.only(top=0),
                                                        alignment=alignment.center_left,
                                                        content=Text(
                                                            font_family="Poppins",
                                                            value="Stok: 821",
                                                            color=colors[
                                                                "blackAlpha/500"
                                                            ],
                                                        ),
                                                    ),
                                                    Container(
                                                        # margin=margin.only(top=0),
                                                        alignment=alignment.center_left,
                                                        content=Text(
                                                            font_family="Poppins",
                                                            value="Rp. 120.000",
                                                            weight="bold",
                                                            color=colors["Black"],
                                                        ),
                                                    ),
                                                ]
                                            ),
                                        ),
                                    ]
                                ),
                                Container(
                                    alignment=alignment.center,
                                    content=ElevatedButton(
                                        "Tambah Barang",
                                        width=200,
                                        height=40,
                                        # border_radius=0,
                                        bgcolor=colors["Primary/500"],
                                        color=colors["White"],
                                        style=ButtonStyle(
                                            shape={
                                                # "border_radius": 10,
                                                # "border_width": 0,
                                                MaterialState.FOCUSED: RoundedRectangleBorder(
                                                    radius=2
                                                ),
                                                MaterialState.HOVERED: RoundedRectangleBorder(
                                                    radius=8
                                                ),
                                                MaterialState.DEFAULT: RoundedRectangleBorder(radius=2)
                                            }
                                        ),
                                    ),
                                ),
                            ]
                        ),
                    ),
                ),
            )
        return items_list

    dummy_data = Container(
        width=OS_WIDTH / 2 - OS_WIDTH / 2 / 3,
        height=OS_HEIGHT - OS_HEIGHT / 3,
        margin=margin.only(top=10, left=0),
        # bgcolor=colors["Black"],
        border_radius=10,
        content=Row(
            spacing=40,  # kesamping
            run_spacing=30,  # kebawah
            wrap=True,
            controls=[
                # Container(
                #     width=275,
                #     height=275,
                #     bgcolor=colors["Accent"],
                #     content=Text(
                #         value='1'
                #     )
                # ),
                *get_items(10),
            ],
        ),
    )
    
    detail_nota = Container(
        width=OS_WIDTH / 2 - OS_WIDTH / 2 / 3,
        height=OS_HEIGHT - OS_HEIGHT / 3,
        margin=margin.only(top=10, left=0),
        # bgcolor=colors["Black"],
        border_radius=10,
        content=Container(
            content=
            Column(
                controls=[
                    Row(
                        
                    )
                ]
            )
        )
    )

    mainpage = Container(
        width=OS_WIDTH,
        height=OS_HEIGHT,
        margin=margin.only(top=50, left=80),
        bgcolor=colors["White"],
        content=Row(
            controls=[
                Column([searchbar_header, dummy_data]),
                Column([detail_nota])
            ]
        ),
    )

    page.add(mainpage)


app(target=main)  #ma
