import sys

sys.path.append("../")
from utils.libs import *
from utils.importer import *

def main(view: View, super_page : Page):
    COLORS_JSON = load_colors()
    # page.title = "Home"
    # page.
    # view.bgcolor = COLORS_JSON["Gray/50"]

    # OS_SIZE = get_monitors()[0]
    # OS_WIDTH, OS_HEIGHT = OS_SIZE.width, OS_SIZE.height
    OS_WIDTH = super_page.window_width
    OS_HEIGHT = super_page.window_height

    # page.window_width = OS_WIDTH
    # page.window_height = OS_HEIGHT
    # # page.window_full_screen = True
    # page.window_focused = True
    style_selectable=ButtonStyle(
        shape=RoundedRectangleBorder(radius=10),
        color={
            MaterialState.DEFAULT:COLORS_JSON["Primary/500"],
            MaterialState.FOCUSED:COLORS_JSON["White"],
            MaterialState.HOVERED:COLORS_JSON["White"],
        },
        side=BorderSide(1,COLORS_JSON["Primary/500"]),
        overlay_color=colors.TRANSPARENT,
        bgcolor={
            MaterialState.DEFAULT:COLORS_JSON["White"],
            MaterialState.FOCUSED:COLORS_JSON["Primary/500"],
            MaterialState.HOVERED:COLORS_JSON["Primary/500"],
        }
    )


    alertYaorBatalkan=[
        TextButton(
            "Batalkan",
            style=style_selectable,
            width=super_page.window_width/100*40/100*20
        ),
        TextButton(
            "Ya",
            style=style_selectable,
            width=super_page.window_width/100*40/100*20
        ),
    ]


    def editDataActionYes(e):
        super_page.dialog.open=False
        super_page.update()
        
        
    def batalkanEditActionEdit(e):
        super_page.dialog.open=False
        super_page.update()
    # for each item, width 250, height 250
    def get_items(N: int = 10):
        items_list = []
        for i in range(N):
            items_list.append(
                Container(
                    width=300,
                    height=200,
                    bgcolor=COLORS_JSON["Primary/100"],
                    border_radius=16,
                    content=Container(
                        content=Column(
                            controls=[
                                Row(
                                    controls=[
                                        Container(
                                            margin=margin.only(left=15, top=15),
                                            width=100,
                                            # bgcolor=COLORS_JSON["B_Bg"],
                                            content=Image(
                                                src=IMGPATH / "dummy-order1.png"
                                            ),
                                        ),
                                        Container(
                                            width=300 - 100,
                                            # bgcolor=COLORS_JSON["B_Bg"],
                                            content=Column(
                                                [
                                                    Container(
                                                        margin=margin.only(top=10),
                                                        alignment=alignment.center_left,
                                                        content=Text(
                                                            value="Kopi Robusta",
                                                            font_family="Poppins",
                                                            size=20,
                                                            color=COLORS_JSON["Black"],
                                                            weight="bold",
                                                        ),
                                                    ),
                                                    Container(
                                                        # margin=margin.only(top=0),
                                                        alignment=alignment.center_left,
                                                        content=Text(
                                                            font_family="Poppins",
                                                            value="Stok: 821",
                                                            color=COLORS_JSON[
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
                                                            color=COLORS_JSON["Black"],
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
                                        bgcolor=COLORS_JSON["Primary/500"],
                                        color=COLORS_JSON["White"],
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
                                                MaterialState.DEFAULT: RoundedRectangleBorder(
                                                    radius=2
                                                ),
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

    searchbar = Container(
        # bgcolor=COLORS_JSON['Black'],
        width=super_page.window_width/100*40-140,
        content=Column(
            controls=[
                Container(
                    # bgcolor=COLORS_JSON['Black'],
                    content=
                    Row(
                    alignment=MainAxisAlignment.SPACE_BETWEEN,
                    # vertical_alignment=CrossAxisAlignment.START,
                    controls=[
                        Text(
                            "Varian Kopi",
                            weight=FontWeight.BOLD,
                            size=30,
                            color=COLORS_JSON['Black'],
                        ),

                            Text(
                            "2 Varian Tersedia",
                            weight=FontWeight.W_500,
                            size=16,
                            color=COLORS_JSON['blackAlpha/500'],
                            )
                        
                    ]
                )
                )
                
                
            ]
        )
    )

    dummy_data = Container(
        width=OS_WIDTH / 2 - OS_WIDTH / 2 / 3,
        height=OS_HEIGHT - OS_HEIGHT / 3,
        margin=margin.only(top=10, left=0),
        # bgcolor=COLORS_JSON["Black"],
        border_radius=10,
        content=Row(
            spacing=40,  # kesamping
            run_spacing=30,  # kebawah
            wrap=True,
            controls=[
                # Container(
                #     width=275,
                #     height=275,
                #     bgcolor=COLORS_JSON["Accent"],
                #     content=Text(
                #         value='1'
                #     )
                # ),
                *get_items(10),
            ],
        ),
    )

    detail_nota = Container(
        # width=super_page.window_width/100*40,
        # height=super_page.window_height-150,
        # margin=margin.only(top=10, left=0),
        # bgcolor=COLORS_JSON["Black"],
        border_radius=10,
        content=
            Column(
                controls=[
                    Container(
                    margin=margin.only(top=20),
                    content=Row(
                        controls=
                        [
                            Text(value='Detail Nota',
                                 size=26,
                                 weight='bold',
                                 font_family='Poppins',
                                 color=COLORS_JSON['Black'])
                        ]
                    )
                )
                ]
            )
    )

    def createPopUpCard(title,content,button):
        return AlertDialog(
            modal=True,
            title=title,
            content=content,
            actions=button,
            actions_alignment=MainAxisAlignment.END,
        )
    NONEDATA=Container(
        content=Column(
            controls=[
                Text(
                    "Tidak Ada Data",
                    weight=FontWeight.BOLD,
                    size=18,
                    width=super_page.window_width/100*40
                ),
                Text(
                    "Pilih Nota dari sebelah kiri untuk mulai perubahan",
                    color=COLORS_JSON["blackAlpha/500"],
                    width=super_page.window_width/100*40
                )
            ],
            alignment=MainAxisAlignment.START,
            spacing=10,
        ),
        bgcolor="White",
        # width=super_page.window_width/100*40,
        # height=super_page.window_height/100*40,
        padding=padding.all(20)
    )
    detailNotaContainer=[]
    detailNotaContainer.append(NONEDATA)

    def alertDialogEditingCellCard(e,data):
        content=Container(
            content=Column(
                controls=[
                    Container(
                        content=Row(
                            controls=[
                                Column(
                                    controls=[
                                        Text("Jumlah Laku"),
                                        TextField()
                                    ]
                                ),
                                Column(
                                    controls=[
                                        Text("Jumlah Sisa"),
                                        TextField()
                                    ]
                                )
                            ]
                        )
                    ),
                    Container(
                        content=Column(
                            controls=[
                                Text("Harga Per Kilo"),
                                TextField()
                            ]
                        )
                    )
                ]
            ),
            width=super_page.window_width/100*50
        )
        card=createPopUpCard(Text("Edit“{}”?".format(data["Barang"])),content,alertYaorBatalkan)
        super_page.dialog=card
        card.open=True
        alertYaorBatalkan[0].on_click=editDataActionYes
        alertYaorBatalkan[1].on_click=batalkanEditActionEdit
        super_page.update()

    def listToTable(list,icon_flag):
        tempList=[]
        icon_row=[]
        rowWidth=super_page.window_width/100*40/100*16
        harga=0
        for i in list:
            icon_cells=[
                IconButton(icon=icons.DELETE,disabled=icon_flag),
                IconButton(icon=icons.EDIT,disabled=icon_flag,on_click=lambda e : alertDialogEditingCellCard(e,i))
            ]
            icon_row.append(icon_cells)
            tempList.append(
                DataRow(
                    cells=[
                        DataCell(Text(str(i["No"]),width=rowWidth)),
                        DataCell(Text(i["Barang"],width=rowWidth)),
                        DataCell(Text(str(i["Kuantitas"]),width=rowWidth)),
                        DataCell(Text("{}%".format(i["Diskon"]),width=rowWidth)),
                        DataCell(Text("Rp.{}".format(i["Harga"]),width=rowWidth)),
                        DataCell(Row(
                            controls=icon_cells
                        ))
                    ]
                )
            )
            harga+=i["Harga"]*i["Kuantitas"]*(1-i["Diskon"]/100)
        tempList.append(
            DataRow(
                cells=[
                    DataCell(Text("Total")),
                    DataCell(Text("")),
                    DataCell(Text("")),
                    DataCell(Text("")),
                    DataCell(Text("Rp.{}".format(harga),width=rowWidth)),
                    DataCell(Text(""))
                ]
            )
        )
        return tempList,icon_row

    def createNotaTableCard(header,data,button,tableRow,pulang):
        bottomCard=Row(
            controls=button,
            alignment=MainAxisAlignment.CENTER,
            spacing=5
        )
        if pulang:
            rowDesc=[
                Text(
                    "{}".format(header),
                    weight=FontWeight.BOLD,
                    size=18
                ),
                Container(
                    content=Row(
                        controls=[
                            Text(
                                "ID Nota : {}".format(data["IdNotaPulang"]),
                                color=COLORS_JSON["blackAlpha/500"]
                            ),
                            Text(
                                "Kasir : {}".format(data["KasirPulang"]),
                                color=COLORS_JSON["blackAlpha/500"]
                            )
                        ],
                        alignment=MainAxisAlignment.SPACE_BETWEEN
                    ),
                    width=super_page.window_width/100*40,
                )
            ]
        else:
            rowDesc=[
                Text(
                    "{}".format(header),
                    weight=FontWeight.BOLD,
                    size=18
                ),
                Container(
                    content=Row(
                        controls=[
                            Text(
                                "ID Nota : {}".format(data["IdNota"]),
                                color=COLORS_JSON["blackAlpha/500"]
                            ),
                            Text(
                                "Kasir : {}".format(data["Kasir"]),
                                color=COLORS_JSON["blackAlpha/500"]
                            )
                        ],
                        alignment=MainAxisAlignment.SPACE_BETWEEN
                    ),
                    width=super_page.window_width/100*40,
                ),
                Container(
                    content=Row(
                        controls=[
                            Text(
                                "Sales : {}".format(data["Sales"]),
                                color=COLORS_JSON["blackAlpha/500"]
                            ),
                            Text(
                                "Tanggal Nota: {}".format(data["Time"]),
                                color=COLORS_JSON["blackAlpha/500"]
                            )
                        ],
                        alignment=MainAxisAlignment.SPACE_BETWEEN
                    ),
                    width=super_page.window_width/100*40,
                )
            ]
        return Container(
            content=Column(
                controls=[*rowDesc,
                        Container(
                            content=DataTable(
                                columns=[
                                    DataColumn(Text("No",size=12,width=super_page.window_width/100*40/100*16,color=COLORS_JSON["Gray/400"])),
                                    DataColumn(Text("Barang",size=12,width=super_page.window_width/100*40/100*16,color=COLORS_JSON["Gray/400"])),
                                    DataColumn(Text("Kuantitas",size=12,width=super_page.window_width/100*40/100*16,color=COLORS_JSON["Gray/400"])),
                                    DataColumn(Text("Diskon",size=12,width=super_page.window_width/100*40/100*16,color=COLORS_JSON["Gray/400"])),
                                    DataColumn(Text("Harga",size=12,width=super_page.window_width/100*40/100*16,color=COLORS_JSON["Gray/400"])),
                                    DataColumn(Text("Aksi",size=12,width=super_page.window_width/100*40/100*16,color=COLORS_JSON["Gray/400"])),
                                ],
                                width=super_page.window_width/100*40,
                                column_spacing=0,
                                rows=tableRow
                            ),
                            alignment=alignment.center
                        ),
                        Container(
                            content=bottomCard,
                            width=super_page.window_width/100*40,
                        )
                    
                    ],
                    alignment=MainAxisAlignment.START,
                    spacing=10
                ),
                bgcolor="White",
                # width=super_page.window_width/100*40,
                # height=super_page.window_height/100*40,
                padding=padding.all(20)
            ),bottomCard

    detailNotaContainer = []

    detailNotaButton=[
        TextButton(
            "Proses Nota",
            style=style_selectable,
            width=super_page.window_width/100*40/100*32
        ),
        TextButton(
            "Kosongkan Nota",
            style=style_selectable,
            width=super_page.window_width/100*40/100*32,
        ),
        TextButton(
            "Hapus Nota",
            style=style_selectable,
            width=super_page.window_width/100*40/100*32
        )
    ]

    def dataToDetailNotaBerlangsung(data):
            rows_table,icon_row=listToTable(dummy_data,True)
            detailNotaContainer.clear()
            DetailNota,cardBottom=createNotaTableCard("DetailNota",data,detailNotaButton,rows_table,False)
            detailNotaContainer.append(DetailNota)
           


    body=Container(
        content=Row(
            controls=[
                Container(
                    content=Column(
                        controls=[
                            Row(
                                alignment=MainAxisAlignment.SPACE_BETWEEN,
                                # vertical_alignment=CrossAxisAlignment.START,
                                controls=[
                                    Text(
                                "Varian Kopi",
                                weight=FontWeight.BOLD,
                                size=24,
                                color=COLORS_JSON['Black'],
                            ),
                                    Text(
                                "2 Varian Tersedia",
                                weight=FontWeight.W_500,
                                size=16,
                                color=COLORS_JSON['blackAlpha/500'],
                                    )
                                ]
                                
                            ),
                            
                            TextField(
                                label="Cari produk",
                                bgcolor=COLORS_JSON["Primary/100"],
                                border_radius=border_radius.all(25),
                                border_color=COLORS_JSON["Primary/100"],
                                prefix_icon=icons.SEARCH,
                                color=COLORS_JSON["Primary/900"],
                            ),
                            Text("NANTI DISINI ADA FILTER COMING SOON!"),

                        ],
                        spacing=30
                    ),
                    bgcolor="White",
                    width=super_page.window_width/100*40,
                    padding=padding.all(20),
                    height=super_page.window_height*90/100-150
                ),
                Container(
                    bgcolor=COLORS_JSON['Black'],
                    content=Column(
                        controls=[
                            detail_nota
                        ]
                    ),
                )
            ],
            alignment=MainAxisAlignment.SPACE_EVENLY,
            vertical_alignment=CrossAxisAlignment.START
        )
        ,bgcolor=COLORS_JSON["Gray/50"],
        width=super_page.window_width,
        height=super_page.window_height-150,
        padding=padding.only(top=20)
    )

    # page.add(mainpage)
    view.controls.append(body)

if __name__ == "__main__":
    app(target=main)  