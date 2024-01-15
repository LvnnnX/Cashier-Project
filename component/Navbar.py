import sys
sys.path.append('../')
from utils.libs import *
from utils.importer import load_colors

class Navbar(Container):
    def __init__(self,width_change):
        super().__init__()
        colors = load_colors()
        self.width=width_change-30
        self.content=Row(
            controls=[
                Container(
                    width=self.width/100*20,
                    height=100,
                    content=Image(
                        src=IMGPATH / "Bean_Admin.svg"
                    ),
                    alignment=alignment.center,
                    padding=0,
                    margin=0
                ),
                # NavigationBar(
                #     width=self.width/100*60,
                #     height=100,
                #     bgcolor="white",
                #     destinations=[
                #         NavigationDestination(
                #             label="Nota Baru"
                #         ),
                #         NavigationDestination(
                #             label="Daftar Nota"
                #         ),
                #         NavigationDestination(
                #             label="Stok dan Produk"
                #         ),
                #         NavigationDestination(
                #             label="Analitik"
                #         ),
                #         NavigationDestination(
                #             label="Admin"
                #         ),
                #     ],
                #     elevation=50,
                #     adaptive=True
                # ),
                Row(
                    height=100,
                    width=self.width/100*60,
                    controls=[
                        TextButton(
                            "Nota Baru",
                            height=100,
                            width=self.width/100*60/100*20,
                            style=ButtonStyle(
                                shape={
                                    MaterialState.DEFAULT:RoundedRectangleBorder(radius=0),
                                    MaterialState.FOCUSED:RoundedRectangleBorder(radius=0),     
                                },
                                color={
                                    MaterialState.DEFAULT:colors["Primary/500"],
                                    MaterialState.FOCUSED:colors["Primary/500"],
                                    MaterialState.HOVERED:colors["Primary/500"],
                                },
                            ),
                        ),
                        TextButton(
                            "Daftar Nota",
                            height=100,
                            width=self.width/100*60/100*20,
                            style=ButtonStyle(
                                shape={
                                    MaterialState.DEFAULT:RoundedRectangleBorder(radius=0),
                                    MaterialState.FOCUSED:RoundedRectangleBorder(radius=0),     
                                },
                                color={
                                    MaterialState.DEFAULT:colors["blackAlpha/500"],
                                    MaterialState.FOCUSED:colors["Primary/500"],
                                    MaterialState.HOVERED:colors["Primary/500"],
                                },
                            ),
                        ),
                        TextButton(
                            "Stok dan Produk",
                            height=100,
                            width=self.width/100*60/100*20,
                            style=ButtonStyle(
                                shape={
                                    MaterialState.DEFAULT:RoundedRectangleBorder(radius=0),
                                    MaterialState.FOCUSED:RoundedRectangleBorder(radius=0),     
                                },
                                color={
                                    MaterialState.DEFAULT:colors["blackAlpha/500"],
                                    MaterialState.FOCUSED:colors["Primary/500"],
                                    MaterialState.HOVERED:colors["Primary/500"],
                                },
                            ),
                        ),
                        TextButton(
                            "Analitik",
                            height=100,
                            width=self.width/100*60/100*20,
                            style=ButtonStyle(
                                shape={
                                    MaterialState.DEFAULT:RoundedRectangleBorder(radius=0),
                                    MaterialState.FOCUSED:RoundedRectangleBorder(radius=0),     
                                },
                                color={
                                    MaterialState.DEFAULT:colors["blackAlpha/500"],
                                    MaterialState.FOCUSED:colors["Primary/500"],
                                    MaterialState.HOVERED:colors["Primary/500"],
                                },
                            ),
                        ),
                        TextButton(
                            "Admin",
                            height=100,
                            width=(self.width/100*60)/100*15,
                            style=ButtonStyle(
                                shape={
                                    MaterialState.DEFAULT:RoundedRectangleBorder(radius=0),
                                    MaterialState.FOCUSED:RoundedRectangleBorder(radius=0),     
                                },
                                color={
                                    MaterialState.DEFAULT:colors["blackAlpha/500"],
                                    MaterialState.FOCUSED:colors["Primary/500"],
                                    MaterialState.HOVERED:colors["Primary/500"],
                                },
                            ),
                        ),
                    ],
                    alignment=MainAxisAlignment.SPACE_EVENLY,
                    spacing=0,
                ),
                Container(
                    width=self.width/100*20,
                    height=100,
                    content=Row(
                        controls=[
                            Image(
                                src=IMGPATH / "Group_33870.png"
                            ),
                            Column(
                                controls=[
                                    Text(
                                        "Admin",
                                        size=14,
                                        weight="Medium"
                                    ),
                                    Text(
                                        "Shira",
                                        size=14,
                                        weight="bold"
                                    )
                                ],
                                alignment=MainAxisAlignment.CENTER
                            )
                        ],
                    ),
                    alignment=alignment.center,
                    padding=0,
                    margin=0
                ),
            ],
            spacing=0
        )
        self.alignment=alignment.center
        self.padding=0
        self.margin=0
    
    def resize_event(self,page_width):
        self.width=page_width-30
        self.content.controls[0].width=self.width/100*20
        self.content.controls[1].width=self.width/100*60
        self.content.controls[2].width=self.width/100*20
        self.content.controls[1].controls[0].width=self.width/100*60/100*20
        self.content.controls[1].controls[1].width=self.width/100*60/100*20
        self.content.controls[1].controls[2].width=self.width/100*60/100*20
        self.content.controls[1].controls[3].width=self.width/100*60/100*20
        self.content.controls[1].controls[4].width=self.width/100*60/100*20

