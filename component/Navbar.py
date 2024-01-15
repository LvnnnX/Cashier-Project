import sys
sys.path.append('../')
from utils.libs import *
from utils.importer import load_colors

class Navbar(Container):
    def __init__(self,width_change):
        super().__init__()
        self.width=width_change
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
                Container(
                    width=self.width/100*12,
                    height=100,
                    content=Text(
                        "Nota Baru",
                        size=16,
                        weight="bold"
                    ),
                    alignment=alignment.center,
                    padding=0,
                    margin=0
                ),
                Container(
                    width=self.width/100*12,
                    height=100,
                    content=Text(
                        "Daftar Nota",
                        size=16,
                        weight="light"
                    ),
                    alignment=alignment.center,
                    padding=0,
                    margin=0
                ),
                Container(
                    width=self.width/100*12,
                    height=100,
                    content=Text(
                        "Stok dan Produk",
                        size=16,
                        weight="light",
                        text_align=TextAlign.CENTER
                    ),
                    alignment=alignment.center,
                    padding=0,
                    margin=0
                ),
                Container(
                    width=self.width/100*12,
                    height=100,
                    content=Text(
                        "Analitik",
                        size=16,
                        weight="light"
                    ),
                    alignment=alignment.center,
                    padding=0,
                    margin=0
                ),
                Container(
                    width=self.width/100*12,
                    height=100,
                    content=Text(
                        "Admin",
                        size=16,
                        weight="light"
                    ),
                    alignment=alignment.center,
                    padding=0,
                    margin=0
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
        self.width=page_width
        self.content.controls[0].width=self.width/100*20
        self.content.controls[1].width=self.width/100*12
        self.content.controls[2].width=self.width/100*12
        self.content.controls[3].width=self.width/100*12
        self.content.controls[4].width=self.width/100*12
        self.content.controls[5].width=self.width/100*12
        self.content.controls[6].width=self.width/100*20