import sys
sys.path.append('../')
from utils.libs import *
from utils.importer import load_colors

def admin_page(view:View,page:Page):
    dummy_data=[
        {
            "No":1,
            "NamaKasir":"Made Putra teguh Pramana",
            "IdKasir":"C12134",
            "Status":"Aktif",
        },
        {
            "No":2,
            "NamaKasir":"Made Putra teguh Pramana",
            "IdKasir":"C12134",
            "Status":"Aktif",
        },
        {
            "No":3,
            "NamaKasir":"Made Putra teguh Pramana",
            "IdKasir":"C12134",
            "Status":"Aktif",
        },
        {
            "No":4,
            "NamaKasir":"Made Putra teguh Pramana",
            "IdKasir":"C12134",
            "Status":"Aktif",
        },
        {
            "No":5,
            "NamaKasir":"Made Putra teguh Pramana",
            "IdKasir":"C12134",
            "Status":"Aktif",
        },
    ]
    structProperty={
        "maxLength":50
    }
    COLOUR_JSON=load_colors()
    style_unselected=ButtonStyle(
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
    style_selected=ButtonStyle(
        shape=RoundedRectangleBorder(radius=0),
        color=COLOUR_JSON["White"],
        side=BorderSide(1,COLOUR_JSON["Primary/500"]),
        overlay_color=colors.TRANSPARENT,
        bgcolor=COLOUR_JSON["Primary/500"]
    )
    adminMainButton=[
        TextButton(
            "Manajemen Kasir",
            style=style_selected,
            width=page.window_width/100*40/100*50
        ),
        TextButton(
            "Manajemen Sales",
            style=style_unselected,
            width=page.window_width/100*40/100*50
        ),
        TextButton(
            "Manajemen Nota",
            style=style_unselected,
            width=page.window_width/100*40/100*50
        )
    ]
    dataRowTable=[]
    
    for i in dummy_data:
        dataRowTable.append(
            DataRow(
                [
                    DataCell(Text("{}".format(i["No"]))),
                    DataCell(Text("{}".format(i["NamaKasir"]))),
                    DataCell(Text("{}".format(i["IdKasir"]))),
                    DataCell(Text("{}".format(i["Status"]))),
                    DataCell(Row(
                            controls=[
                                IconButton(icon=icons.DELETE),
                                IconButton(icon=icons.EDIT)
                            ]
                        )
                    )
                ]
            )
        )
    table=DataTable(
        columns=[
            DataColumn(Text("No")),
            DataColumn(Text("Nama Kasir")),
            DataColumn(Text("ID Kasir")),
            DataColumn(Text("Status")),
            DataColumn(Text("Aksi")),
        ],
        rows=dataRowTable

    )
    filterDropDown=Dropdown(
        options=[
            dropdown.Option("Sales(Pulang)"),
            dropdown.Option("Sales(ambil)"),
            dropdown.Option("beli"),
            dropdown.Option("None"),
        ]
    )
    optionDropdownShowing=[dropdown.Option("{}".format(i)) for i in range(structProperty["maxLength"])]
    showingData=Dropdown(
        options=optionDropdownShowing
    )
    bottomTableChange=[]
    bottomTableChange.append(IconButton(icon=icons.ARROW_LEFT))
    for i in range(min(structProperty["maxLength"],5)):
        bottomTableChange.append(TextButton("{}".format(i+1)))
    bottomTableChange.append(IconButton(icon=icons.ARROW_RIGHT))
    filterDropDown.value="None"
    body=Container(
        content=Column(
                controls=[
                    Container(
                        content=Column(
                            controls=[
                                Text("Halaman Admin"),
                                Row(
                                    controls=adminMainButton,
                                    spacing=0
                                ),
                                Row(
                                    controls=[
                                        filterDropDown,
                                        Row(
                                            controls=[
                                                Text("Pencarian :"),
                                                TextField()
                                            ]
                                        )
                                    ],
                                    alignment=MainAxisAlignment.SPACE_BETWEEN
                                ),
                                table,
                                Row(
                                    controls=[
                                        Row(
                                            controls=[
                                                Text("Showing"),
                                                showingData,
                                                Text("{}".format(structProperty["maxLength"]))
                                            ]
                                        ),
                                        Row(
                                            controls=bottomTableChange
                                        )
                                    ],
                                    alignment=MainAxisAlignment.SPACE_BETWEEN
                                )
                            ]
                        ),
                        bgcolor=COLOUR_JSON["White"],
                        padding=padding.all(20),
                        
                    )
                ],
                alignment=MainAxisAlignment.START,
                horizontal_alignment=CrossAxisAlignment.CENTER
        ),
        bgcolor=COLOUR_JSON["Gray/50"],
        width=page.window_width,
        height=page.window_height-150,
        padding=padding.only(top=20)
    )
    view.controls.append(body)
    view.scroll=ScrollMode.AUTO