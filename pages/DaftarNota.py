import sys
sys.path.append('../')
from utils.libs import *
from utils.importer import load_colors


def main(view:View,super_page:Page):
    COLOUR_JSON=load_colors()
    style_selected=ButtonStyle(
        shape=RoundedRectangleBorder(radius=0),
        color={
            MaterialState.DEFAULT:COLOUR_JSON["Primary/500"],
            MaterialState.FOCUSED:COLOUR_JSON["White"],
            MaterialState.HOVERED:COLOUR_JSON["White"],
        },
        side=BorderSide(1,COLOUR_JSON["Primary/500"]),
        overlay_color=colors.TRANSPARENT,
        bgcolor={
            MaterialState.DEFAULT:COLOUR_JSON["White"],
            MaterialState.FOCUSED:COLOUR_JSON["Primary/500"],
            MaterialState.HOVERED:COLOUR_JSON["Primary/500"],
        }
    )
    style_unselected=ButtonStyle(
        shape=RoundedRectangleBorder(radius=0),
        color=COLOUR_JSON["White"],
        side=BorderSide(1,COLOUR_JSON["Primary/500"]),
        overlay_color=colors.TRANSPARENT,
        bgcolor=COLOUR_JSON["Primary/500"]
    )
    style_selectable=ButtonStyle(
        shape=RoundedRectangleBorder(radius=10),
        color={
            MaterialState.DEFAULT:COLOUR_JSON["Primary/500"],
            MaterialState.FOCUSED:COLOUR_JSON["White"],
            MaterialState.HOVERED:COLOUR_JSON["White"],
        },
        side=BorderSide(1,COLOUR_JSON["Primary/500"]),
        overlay_color=colors.TRANSPARENT,
        bgcolor={
            MaterialState.DEFAULT:COLOUR_JSON["White"],
            MaterialState.FOCUSED:COLOUR_JSON["Primary/500"],
            MaterialState.HOVERED:COLOUR_JSON["Primary/500"],
        }
    )
    daftar_nota_button=[
        TextButton(
            "Nota Berlangsung",
            style=style_selected
        ),
        TextButton(
            "Nota Selesai",
            style=style_unselected
        )
    ]
    columns_table=[
        DataColumn(Text("No",size=12)),
        DataColumn(Text("Barang",size=12)),
        DataColumn(Text("Kuantitas",size=12)),
        DataColumn(Text("Diskon",size=12)),
        DataColumn(Text("Harga",size=12)),
        DataColumn(Text("Aksi",size=12)),
    ]
    def clicked_nota_berlangsung(e):
        daftar_nota_button[0].style=style_selected
        daftar_nota_button[1].style=style_unselected
        super_page.update()
    def clicked_nota_NotaSelesai(e):
        daftar_nota_button[1].style=style_selected
        daftar_nota_button[0].style=style_unselected
        super_page.update()
    daftar_nota_button[1].on_click=clicked_nota_berlangsung
    daftar_nota_button[0].on_click=clicked_nota_NotaSelesai
    body=Container(
        content=Row(
            controls=[
                Container(
                    content=Column(
                        controls=[
                            Text(
                                "Daftar Nota",
                                weight=FontWeight.BOLD,
                                size=24
                            ),
                            Row(
                                controls=daftar_nota_button,
                                spacing=0
                            ),
                            TextField(
                                label="Cari nota",
                                bgcolor=COLOUR_JSON["Primary/100"],
                                border_radius=border_radius.all(25),
                                border_color=COLOUR_JSON["Primary/100"],
                                prefix_icon=icons.SEARCH,
                                color=COLOUR_JSON["Primary/900"],
                            ),
                            Text("NANTI DISINI ADA FILTER COMING SOON!"),
                            Column(
                                controls=[
                                    Container(
                                        bgcolor=COLOUR_JSON["Primary/100"],
                                        padding=padding.all(20),
                                        border_radius=25,
                                        content=Row(
                                            controls=[
                                                Column(
                                                    controls=[
                                                        Text(
                                                            "ID Nota: b332432e",
                                                            weight=FontWeight.W_600
                                                        ),
                                                        Text(
                                                            "Dibuat pada 14 Februari 2023, 21:01",
                                                            weight=FontWeight.W_200
                                                        ),
                                                        Text(
                                                            "Sales: Teguh",
                                                            weight="bold"
                                                        )
                                                    ]
                                                ),
                                                IconButton(
                                                    icon=icons.ARROW_CIRCLE_RIGHT
                                                )
                                            ],
                                            alignment=MainAxisAlignment.SPACE_BETWEEN
                                        )
                                    )
                                ],
                            )
                        ],
                        spacing=30
                    ),
                    bgcolor="White",
                    width=super_page.window_width/100*40,
                    padding=padding.all(20)
                ),
                Column(
                    controls=[
                        Container(
                            content=Column(
                                controls=[
                                    Text(
                                        "Detail Nota",
                                        weight=FontWeight.BOLD,
                                        size=18
                                    ),
                                    Row(
                                        controls=[
                                            Text(
                                                "ID Nota: Pw342r3rf",
                                                color=COLOUR_JSON["blackAlpha/500"]
                                            ),
                                            Text(
                                                "Kasir: Misaki",
                                                color=COLOUR_JSON["blackAlpha/500"]
                                            )
                                        ],
                                        alignment=MainAxisAlignment.SPACE_BETWEEN
                                    ),
                                    Row(
                                        controls=[
                                            Text(
                                                "Sales    : Teguh",
                                                color=COLOUR_JSON["blackAlpha/500"]
                                            ),
                                            Text(
                                                "Tanggal Nota: 14 Januari 2023, 21:01",
                                                color=COLOUR_JSON["blackAlpha/500"]
                                            )
                                        ],
                                        alignment=MainAxisAlignment.SPACE_BETWEEN
                                    ),
                                    DataTable(
                                        columns=columns_table,
                                        width=super_page.window_width/100*40-100,
                                        column_spacing=0,
                                        rows=[
                                            DataRow(
                                                cells=[
                                                    DataCell(Text("1")),
                                                    DataCell(Text("Kopi")),
                                                    DataCell(Text("10")),
                                                    DataCell(Text("10%")),
                                                    DataCell(Text("Rp.220000")),
                                                    DataCell(Text(""))
                                                ]
                                            ),
                                            DataRow(
                                                cells=[
                                                    DataCell(Text("total")),
                                                    DataCell(Text("")),
                                                    DataCell(Text("")),
                                                    DataCell(Text("")),
                                                    DataCell(Text("Rp.220000")),
                                                    DataCell(Text(""))
                                                ]
                                            )
                                        ]
                                    ),
                                    Row(
                                        controls=[
                                            TextButton(
                                                "Tambahkan Nota Pulang",
                                                style=style_selectable,
                                                width=super_page.window_width/100*40/100*40
                                            ),
                                            TextButton(
                                                "Hapus Nota",
                                                style=style_selectable,
                                                width=super_page.window_width/100*40/100*40
                                            )
                                        ],
                                        alignment=MainAxisAlignment.CENTER,
                                        spacing=5
                                    )
                                ],
                                alignment=MainAxisAlignment.START,
                                spacing=10
                            ),
                            bgcolor="White",
                            width=super_page.window_width/100*40,
                            height=super_page.window_height/100*40,
                            padding=padding.all(20)
                            
                        ),
                    ]
                )
            ],
            alignment=MainAxisAlignment.SPACE_EVENLY
        )
        ,bgcolor=COLOUR_JSON["Gray/50"],
        width=super_page.window_width,
        height=super_page.window_height-100,
        padding=padding.only(top=20)
    )
    view.controls.append(body)