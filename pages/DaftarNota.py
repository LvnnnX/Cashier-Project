import sys
sys.path.append('../')
from utils.libs import *
from utils.importer import *


def main(view:View,super_page:Page):
    detailNotaContainer=[]
    changeSizeList=[]
    daftarNotaList={
        "berlangsung":[],
        "selesai":[]
    }
    super_page.flagDaftarNota=True
    dummy_data=[
        {
            "No":1,
            "Barang":"Kopi Lanang",
            "Kuantitas":10,
            "Diskon":10,
            "Harga":2743723,
        },
        {
            "No":2,
            "Barang":"Kopi Lanang",
            "Kuantitas":20,
            "Diskon":30,
            "Harga":2123723,
        },
        {
            "No":3,
            "Barang":"Kopi Robusta",
            "Kuantitas":20,
            "Diskon":30,
            "Harga":2743723,
        },
        # {
        #     "No":1,
        #     "Barang":"Kopi Lanang",
        #     "Kuantitas":10,
        #     "Diskon":10,
        #     "Harga":2743723,
        # }
    ]
    structProperty={}
    dataIdHeader=loadNotaHeaderByTime(None,datetime.datetime.now())
    dataIdHeader=getAndJoinSalesById(dataIdHeader)
    listNamaSales=getUniqueSalesName()
    listNamaBarang=getUniqueBarangName()
    listNamaToko=getUniqueTokoName()
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
    style_unselectable=ButtonStyle(
        shape=RoundedRectangleBorder(radius=10),
        bgcolor=COLOUR_JSON["Gray/400"],
        color=COLOUR_JSON["White"]
    )
    daftar_nota_button=[
        TextButton(
            "Nota Berlangsung",
            style=style_selected,
            width=super_page.window_width/100*40/100*25
        ),
        TextButton(
            "Nota Selesai",
            style=style_unselected,
            width=super_page.window_width/100*40/100*25
        )
    ]
    notaPulangButton=[
        TextButton(
            "Selesaikan Nota",
            style=style_selectable,
            width=super_page.window_width/100*40/100*40
        ),
        TextButton(
            "Batalkan",
            style=style_selectable,
            width=super_page.window_width/100*40/100*40
        )
    ]
    detailNotaButton=[
        TextButton(
            "Edit",
            style=style_selectable,
            width=super_page.window_width/100*40/100*32
        ),
        TextButton(
            "Tambahkan Nota Pulang",
            style=style_selectable,
            width=super_page.window_width/100*40/100*32,
        ),
        TextButton(
            "Hapus Nota",
            style=style_selectable,
            width=super_page.window_width/100*40/100*32
        )
    ]
    detailNotaPulangSelesaiButton=[
        TextButton(
            "Edit Nota Pulang",
            style=style_selectable,
            width=super_page.window_width/100*40/100*40
        ),
        TextButton(
            "Hapus Nota Pulang",
            style=style_selectable,
            width=super_page.window_width/100*40/100*40,
        ),
    ]
    notaPulangEditingButton=[
        TextButton(
            "Simpan Perubahan",
            style=style_selectable,
            width=super_page.window_width/100*40/100*40
        ),
        TextButton(
            "Batalkan",
            style=style_selectable,
            width=super_page.window_width/100*40/100*40,
        ),
    ]
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
    salesDropOption=[ dropdown.Option(x) for x in listNamaSales]
    filterDetailNotaBerlangsung=[
        Dropdown(
            options=[
                dropdown.Option("Hari ini"),
                dropdown.Option("Bulan ini"),
                dropdown.Option("Tahun ini"),
            ],
            width=super_page.window_width/100*40/100*25
        ),
        Dropdown(
            options=salesDropOption,
            width=super_page.window_width/100*40/100*25
        )
    ]
    def disableNotaButton(button):
        for i in button:
            detailNotaButton[i].disabled=True
            detailNotaButton[i].style=style_unselectable
    def enableNotaButton(button):
        for i in button:
            detailNotaButton[i].disabled=False
            detailNotaButton[i].style=style_selectable
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
                    color=COLOUR_JSON["blackAlpha/500"],
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
    
    detailNotaContainer.append(NONEDATA)
    def clicked_nota_berlangsung(e):
        daftar_nota_button[0].style=style_selected
        daftar_nota_button[1].style=style_unselected
        containerDaftarNota.controls=daftarNotaList["berlangsung"]
        super_page.flagDaftarNota=True
        detailNotaContainer.clear()
        detailNotaContainer.append(NONEDATA)
        enableNotaButton([0,1,2])
        super_page.update()
    def clicked_nota_NotaSelesai(e):
        daftar_nota_button[0].style=style_unselected
        daftar_nota_button[1].style=style_selected
        containerDaftarNota.controls=daftarNotaList["selesai"]
        super_page.flagDaftarNota=False
        detailNotaContainer.clear()
        detailNotaContainer.append(NONEDATA)
        enableNotaButton([0,1,2])
        super_page.update()
    daftar_nota_button[0].on_click=clicked_nota_berlangsung
    daftar_nota_button[1].on_click=clicked_nota_NotaSelesai
    def listToTableV2(list,icon_flag):
        tempList=[]
        icon_row=[]

        rowWidth=super_page.window_width/100*40/100*16
        harga=0
        for index,row in list.iterrows():
            temp = alertDialogEditingCellCard(row)
            icon_cells=[
                IconButton(icon=icons.DELETE,disabled=icon_flag),
                IconButton(icon=icons.EDIT,disabled=icon_flag,on_click=temp.alert)
            ]
            icon_row.append(icon_cells)
            tempList.append(
                DataRow(
                    cells=[
                        DataCell(Text(str(index+1),width=super_page.window_width/100*40/100*4)),
                        DataCell(Text(row["nama"],width=super_page.window_width/100*40/100*22)),
                        DataCell(Text(str(row["qty"]),width=super_page.window_width/100*40/100*16)),
                        DataCell(Text("{}%".format(row["disc"]),width=super_page.window_width/100*40/100*16)),
                        DataCell(Text("Rp.{}".format(row["harga_satuan"]*row["qty"]*(1-row["disc"]/100)),width=super_page.window_width/100*40/100*22)),
                        DataCell(Row(
                            controls=icon_cells
                        ))
                    ]
                )
            )
            harga+=row["harga_satuan"]*row["qty"]*(1-row["disc"]/100)
        tempList.append(
            DataRow(
                cells=[
                    DataCell(Text("")),
                    DataCell(Text("Total")),
                    DataCell(Text("")),
                    DataCell(Text("")),
                    DataCell(Text("Rp.{}".format(harga),width=rowWidth)),
                    DataCell(Text(""))
                ]
            )
        )
        return tempList,icon_row
    def batalkanNotaPulang(e):
        enableNotaButton([0,1])
        detailNotaContainer.pop()
        super_page.update()
    def selesaikanNotaPulang(e):
        enableNotaButton([0,1])        
        detailNotaContainer.clear()
        detailNotaContainer.append(NONEDATA)
        super_page.update()
    def editDataActionYes(e):

        super_page.dialog.open=False
        super_page.update()
    def batalkanEditActionEdit(e):
        super_page.dialog.open=False
        super_page.update()
    class alertDialogEditingCellCard():
        def __init__(self,i):
            self.i=i
        def alert(self,e):
            self.jumlahLaku=TextField()
            self.jumlahSisa=TextField()
            content=Container(
                content=Column(
                    controls=[
                        Container(
                            content=Row(
                                controls=[
                                    Column(
                                        controls=[
                                            Text("Jumlah Laku"),
                                            self.jumlahLaku
                                        ],
                                        width=super_page.window_width/100*50/100*45
                                    ),
                                    Column(
                                        controls=[
                                            Text("Jumlah Sisa"),
                                            self.jumlahSisa
                                        ],
                                        width=super_page.window_width/100*50/100*45,
                                    )
                                ],
                                spacing=10
                            )
                        ),
                        Container(
                            content=Column(
                                controls=[
                                    Text("Harga Per Kilo"),
                                    TextField()
                                ],
                                width=super_page.window_width/100*50/100*90+10
                            )
                        )
                    ],
                ),
            width=super_page.window_width/100*50,
            height=200,
            expand=True,
            padding=padding.all(0),
            )
            card=createPopUpCard(Text("Edit“{}”?".format(self.i["nama"])),content,alertYaorBatalkan)
            super_page.dialog=card
            card.open=True
            alertYaorBatalkan[0].on_click=editDataActionYes
            alertYaorBatalkan[1].on_click=batalkanEditActionEdit
            super_page.update()
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
                                "ID Nota : {}".format(data["id_nota"]),
                                color=COLOUR_JSON["blackAlpha/500"]
                            ),
                            Text(
                                "Kasir : {}".format(data["id_karyawan"]),
                                color=COLOUR_JSON["blackAlpha/500"]
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
                                "ID Nota : {}".format(data["id_nota"]),
                                color=COLOUR_JSON["blackAlpha/500"]
                            ),
                            Text(
                                "Kasir : {}".format(data["id_karyawan"]),
                                color=COLOUR_JSON["blackAlpha/500"]
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
                                "Sales : {}".format(data["id_sales"]),
                                color=COLOUR_JSON["blackAlpha/500"]
                            ),
                            Text(
                                "Tanggal Nota: {}".format(data["tanggal"]),
                                color=COLOUR_JSON["blackAlpha/500"]
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
                                    DataColumn(Text("No",size=12,width=super_page.window_width/100*40/100*4,color=COLOUR_JSON["Gray/400"])),
                                    DataColumn(Text("Barang",size=12,width=super_page.window_width/100*40/100*22,color=COLOUR_JSON["Gray/400"])),
                                    DataColumn(Text("Kuantitas",size=12,width=super_page.window_width/100*40/100*16,color=COLOUR_JSON["Gray/400"])),
                                    DataColumn(Text("Diskon",size=12,width=super_page.window_width/100*40/100*16,color=COLOUR_JSON["Gray/400"])),
                                    DataColumn(Text("Harga",size=12,width=super_page.window_width/100*40/100*22,color=COLOUR_JSON["Gray/400"])),
                                    DataColumn(Text("Aksi",size=12,width=super_page.window_width/100*40/100*16,color=COLOUR_JSON["Gray/400"])),
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
    def notaPulangSelesaikanNotaPopUpButtonActionBatal(e):
        super_page.dialog.open=False
        super_page.update()
    def notaPulangSelesaikanNotaPopUpButtonActionYa(e,bottomCard,icon_row):
        for i in icon_row:
            i[1].disabled=True
        bottomCard.controls=detailNotaPulangSelesaiButton
        detailNotaPulangSelesaiButton[0].on_click=lambda e : ChangeCardToeditTable(e,bottomCard,icon_row)
        detailNotaPulangSelesaiButton[1].on_click=alertDialogNotaPulangSelesaiHapus
        super_page.dialog.open=False
        super_page.update()
    def notaPulangEditingActionbatalkan(e,bottomCard,icon_row):
        for i in icon_row:
            i[1].disabled=True
        bottomCard.controls=detailNotaPulangSelesaiButton
        detailNotaPulangSelesaiButton[0].on_click=lambda e : ChangeCardToeditTable(e,bottomCard,icon_row)
        detailNotaPulangSelesaiButton[1].on_click=alertDialogNotaPulangSelesaiHapus
        super_page.dialog.open=False
        super_page.update()
    def ChangeCardToeditTable(e,bottomCard,icon_row):
        for i in icon_row:
            i[1].disabled=False
        bottomCard.controls=notaPulangEditingButton
        notaPulangEditingButton[0].on_click=lambda e : alertDialogNotaPulangSelesai(e,bottomCard,icon_row)
        notaPulangEditingButton[1].on_click=lambda e : notaPulangEditingActionbatalkan(e,bottomCard,icon_row)
        super_page.update()
    #function di call untuk ngeluarin pop up di nota pulang yang selesai 
    def alertDialogNotaPulangSelesai(e,bottomCard,icon_row):
        card=createPopUpCard(Text("Simpan Nota Pulang"),Text("Apakah Anda yakin ingin menyimpan perubahan pada nota pulang?"),alertYaorBatalkan)
        super_page.dialog=card
        card.open=True
        alertYaorBatalkan[1].on_click=lambda e : notaPulangSelesaikanNotaPopUpButtonActionYa(e,bottomCard,icon_row)
        alertYaorBatalkan[0].on_click= notaPulangSelesaikanNotaPopUpButtonActionBatal
        super_page.update()
    def notaPulangSelesaiHapusNotaPopUpButtonActionBatal(e):
        super_page.dialog.open=False
        super_page.update()
    def notaPulangSelesaiHapusNotaPopUpButtonActionYa(e):
        detailNotaContainer.clear()
        detailNotaContainer.append(NONEDATA)
        super_page.dialog.open=False
        super_page.update()
    def alertDialogNotaPulangSelesaiHapus(e):
        card=createPopUpCard(Text("Hapus Nota Pulang?"),Text("Apakah Anda yakin ingin menghapus Nota Pulang? Nota yang sudah dihapus tidak bisa dikembalikan.\n\nStatus nota akan kembali menjadi “Nota Berlangsung”!"),alertYaorBatalkan)
        super_page.dialog=card
        card.open=True
        alertYaorBatalkan[0].on_click=notaPulangSelesaiHapusNotaPopUpButtonActionBatal
        alertYaorBatalkan[1].on_click=notaPulangSelesaiHapusNotaPopUpButtonActionYa
        super_page.update()
    def detailNotaBerlangsungHapusPopUpButtonActionYa(e):
        detailNotaContainer.clear()
        detailNotaContainer.append(NONEDATA)
        super_page.dialog.open=False
        super_page.update()
    def detailNotaBerlangsungHapusPopUpButtonActionBatal(e):
        super_page.dialog.open=False
        super_page.update()
    def alertDialogDetailNotaBerlangsungHapus(e):
        card=createPopUpCard(Text("Hapus Nota?"),Text("Apakah Anda yakin ingin menghapus Nota? Nota yang sudah dihapus tidak bisa dikembalikan."),alertYaorBatalkan)
        super_page.dialog=card
        card.open=True
        alertYaorBatalkan[0].on_click=detailNotaBerlangsungHapusPopUpButtonActionBatal
        alertYaorBatalkan[1].on_click=detailNotaBerlangsungHapusPopUpButtonActionYa
        super_page.update()
    def alertDialogNotaPulangSimpanActionYa(e):
        selesaikanNotaPulang(e)
        super_page.dialog.open=False
        super_page.update()
    def alertDialogNotaPulangSimpanActionBatal(e):
        super_page.dialog.open=False
        super_page.update()
    def alertDialogNotaPulangSimpan(e):
        card=createPopUpCard(Text("Simpan Perubahan? "),Text("Apakah Anda yakin ingin menyimpan perubahan pada nota?"),alertYaorBatalkan)
        super_page.dialog=card
        card.open=True
        alertYaorBatalkan[0].on_click=alertDialogNotaPulangSimpanActionBatal
        alertYaorBatalkan[1].on_click=alertDialogNotaPulangSimpanActionYa
        super_page.update()
    def createNotaBerlangsungPulang(e,data):
        disableNotaButton([0,1])
        structProperty["detailnew"]=loadNotaDetailbyIdNotaPrimary(data["id_nota_primary"],datetime.datetime.now()).reset_index()
        structProperty["detailnew"]=getAndJoinStokById(structProperty["detailnew"])
        structProperty["detailnew"]=getAndJoinKopiById(structProperty["detailnew"])
        notaPulangRow,icon_row=listToTableV2(structProperty["detailnew"].loc[structProperty["detailnew"]["id_nota_primary"]==data["id_nota_primary"]],False)
        for i in icon_row:
            i[0].visible=False
        NotaPulang,cardBottom=createNotaTableCard("Nota Pulang",data,notaPulangButton,notaPulangRow,True)
        detailNotaContainer.append(NotaPulang)
        notaPulangButton[0].on_click=alertDialogNotaPulangSimpan
        notaPulangButton[1].on_click=batalkanNotaPulang
        super_page.update()
    def dataToDetailNotaBerlangsung(data):
        enableNotaButton([0,1])
        structProperty["detaildata"]=loadNotaDetailbyIdNotaPrimary(data["id_nota_primary"],datetime.datetime.now()).reset_index()
        structProperty["detaildata"]=getAndJoinStokById(structProperty["detaildata"])
        structProperty["detaildata"]=getAndJoinKopiById(structProperty["detaildata"])
        rows_table,icon_row=listToTableV2(structProperty["detaildata"].loc[structProperty["detaildata"]["id_nota_primary"]==data["id_nota_primary"]],True)
        detailNotaContainer.clear()
        DetailNota,cardBottom=createNotaTableCard("DetailNota",data,detailNotaButton,rows_table,False)
        detailNotaContainer.append(DetailNota)
        detailNotaButton[1].on_click=lambda e : createNotaBerlangsungPulang(e,data)
        detailNotaButton[2].on_click=alertDialogDetailNotaBerlangsungHapus
    def dataToDetailNotaSelesai(data):
        dataselesaiambil=dataIdHeader.loc[(dataIdHeader["id_nota"]==data["id_nota"]) & (dataIdHeader["jenis_transaksi"]==0) ]
        dataselesaipulang=dataIdHeader.loc[(dataIdHeader["id_nota"]==data["id_nota"]) & (dataIdHeader["jenis_transaksi"]==1) ]
        structProperty["detaildata"]=loadNotaDetailbyIdNotaPrimary(dataselesaiambil.iloc[0]["id_nota_primary"],datetime.datetime.now()).reset_index()
        structProperty["pulangdata"]=loadNotaDetailbyIdNotaPrimary(dataselesaipulang.iloc[0]["id_nota_primary"],datetime.datetime.now()).reset_index()
        structProperty["detaildata"]=getAndJoinStokById(structProperty["detaildata"])
        structProperty["pulangdata"]=getAndJoinStokById(structProperty["pulangdata"])
        structProperty["detaildata"]=getAndJoinKopiById(structProperty["detaildata"])
        structProperty["pulangdata"]=getAndJoinKopiById(structProperty["pulangdata"])
        rows_tableDetail,icon_rowDetail=listToTableV2(structProperty["detaildata"],True)
        rows_tablePulang,icon_rowPulang=listToTableV2(structProperty["pulangdata"],True)
        detailNotaContainer.clear()
        DetailNota,cardBottomDetail=createNotaTableCard("DetailNota",data,[],rows_tableDetail,True)
        detailNotaContainer.append(DetailNota)
        NotePulang,cardBottomPulang=createNotaTableCard("Nota Pulang",data,detailNotaPulangSelesaiButton,rows_tablePulang,True)
        detailNotaContainer.append(NotePulang)
        for i in icon_rowPulang:
            i[0].visible=False
        detailNotaPulangSelesaiButton[0].on_click=lambda e : ChangeCardToeditTable(e,cardBottomPulang,icon_rowPulang)
        detailNotaPulangSelesaiButton[1].on_click=alertDialogNotaPulangSelesaiHapus
    class daftarNotaListAction():
        def __init__(self,data):
            self.data=data
        def buttonAction(self,e):
                if not super_page.flagDaftarNota:
                    dataToDetailNotaSelesai(self.data)
                    super_page.update()
                else :
                    dataToDetailNotaBerlangsung(self.data)
                    super_page.update()
    def daftarNotaListToContainer(data:pd.DataFrame):
        for index,row in data.loc[data["status_nota"]==0].iterrows():
            buttonAction=daftarNotaListAction(row)
            daftarNotaList["berlangsung"].append(
                Container(
                    bgcolor=COLOUR_JSON["Primary/100"],
                    padding=padding.all(20),
                    border_radius=25,
                    content=Row(
                        controls=[
                            Column(
                                controls=[
                                    Text(
                                        "ID Nota: {}".format(row["id_nota"]),
                                        weight=FontWeight.W_600
                                    ),
                                    Text(
                                        "Dibuat pada {}".format(row["tanggal"]),
                                        weight=FontWeight.W_200
                                    ),
                                    Text(
                                        "Sales: {}".format(row["nama"]),
                                        weight="bold"
                                    )
                                ]
                            ),
                            IconButton(
                                icon=icons.ARROW_CIRCLE_RIGHT,
                                on_click=buttonAction.buttonAction
                            )
                        ],
                        alignment=MainAxisAlignment.SPACE_BETWEEN
                    )
                )
            )
        for index,row in data.loc[(data["status_nota"]==1) & (data["jenis_transaksi"]==0)].iterrows():
            buttonAction=daftarNotaListAction(row)
            daftarNotaList["selesai"].append(
                Container(
                    bgcolor=COLOUR_JSON["Primary/100"],
                    padding=padding.all(20),
                    border_radius=25,
                    content=Row(
                        controls=[
                            Column(
                                controls=[
                                    Text(
                                        "ID Nota: {}".format(row["id_nota"]),
                                        weight=FontWeight.W_600
                                    ),
                                    Text(
                                        "Dibuat pada {}".format(row["tanggal"]),
                                        weight=FontWeight.W_200
                                    ),
                                    Text(
                                        "Sales: {}".format(row["nama"]),
                                        weight="bold"
                                    )
                                ]
                            ),
                            IconButton(
                                icon=icons.ARROW_CIRCLE_RIGHT,
                                on_click=buttonAction.buttonAction
                            )
                        ],
                        alignment=MainAxisAlignment.SPACE_BETWEEN
                    )
                )
            )
    daftarNotaListToContainer(dataIdHeader)
    containerDaftarNota=Column(
        controls=daftarNotaList["berlangsung"],
        scroll=ScrollMode.AUTO
        )
    
    body=Row(
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
                            Row(
                                controls=filterDetailNotaBerlangsung
                            ),
                            Container(
                                content=containerDaftarNota,
                                expand=True
                            )
                        ],
                        spacing=30
                    ),
                    bgcolor="White",
                    width=super_page.window_width/100*40,
                    padding=padding.all(20),
                    height=super_page.window_height*90/100-150
                ),
                Container(
                    content=Column(
                        controls=detailNotaContainer,
                        scroll=ScrollMode.AUTO,
                    ),
                    height=super_page.window_height*90/100-150
                )
            ],
            alignment=MainAxisAlignment.SPACE_EVENLY,
            vertical_alignment=CrossAxisAlignment.START
        )
    def changeSizeOnWindowsEvent():
        pass
    view.controls.append(body)
    view.expand=True