import sys
sys.path.append('../')
from utils.libs import *
from utils.importer import load_colors

def admin_page(view:View,page:Page):
    page.overlay.clear()
    dummy_data={
        "ManajemenKasir":[
            {
                
                "NamaKasir":"Made Putra teguh Pramana",
                "IdKasir":"C12134",
                "Status":"Aktif",
            },
            {
                
                "NamaKasir":"Made Putra teguh Pramana",
                "IdKasir":"C12134",
                "Status":"Aktif",
            },
            {
                
                "NamaKasir":"Made Putra teguh Pramana",
                "IdKasir":"C12134",
                "Status":"Aktif",
            },
            {
                
                "NamaKasir":"Made Putra teguh Pramana",
                "IdKasir":"C12134",
                "Status":"Aktif",
            },
            {
                
                "NamaKasir":"Made Putra teguh Pramana",
                "IdKasir":"C12134",
                "Status":"Aktif",
            },
        ],
        "ManajemenSales":[
            {
                "NamaSales":"Made Putra Teguh Pramana",
                "Alamat":"Jalan Perum Pasraman Unud no A51",
                "NoHp":"Status",
            },
            {
                "NamaSales":"Made Putra Teguh Pramana",
                "Alamat":"Jalan Perum Pasraman Unud no A51",
                "NoHp":"Status",
            },
            {
                "NamaSales":"Made Putra Teguh Pramana",
                "Alamat":"Jalan Perum Pasraman Unud no A51",
                "NoHp":"Status",
            },
            {
                "NamaSales":"Made Putra Teguh Pramana",
                "Alamat":"Jalan Perum Pasraman Unud no A51",
                "NoHp":"Status",
            },
        ],
        "ManajemenNota":[
            {
                "IdNota":"N12312331",
                "NotaPembelian":"Nota Pembelian",
                "StatusNota":"selesai",
                "TanggalNota":"21-01-2023",
            },
            {
                "IdNota":"N12312331",
                "NotaPembelian":"Nota Pembelian",
                "StatusNota":"selesai",
                "TanggalNota":"21-01-2023",
            },
            {
                "IdNota":"N12312331",
                "NotaPembelian":"Nota Pembelian",
                "StatusNota":"selesai",
                "TanggalNota":"21-01-2023",
            },
            {
                "IdNota":"N12312331",
                "NotaPembelian":"Nota Pembelian",
                "StatusNota":"selesai",
                "TanggalNota":"21-01-2023",
            },
        ]
    }
    structProperty={
        "maxLength":50,
        "flag":0
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
    alertYaorBatalkan=[
        TextButton(
            "Batalkan",
            style=style_selectable,
            width=page.window_width/100*40/100*20
        ),
        TextButton(
            "Ya",
            style=style_selectable,
            width=page.window_width/100*40/100*20
        ),
    ]
    def listDictToTableRowAndCol(data,Cellwidth=None,deleteFunction=None,editFunction=None):
        if Cellwidth is None:
            Cellwidth=[(page.window_width-170)/(len(data[0])+3) for _ in range(len(data[0])+2)]
        tableColumn=[]
        tableColumn.append(DataColumn(Text("No",width=Cellwidth[0])))
        for i in enumerate(data[0],1):
            tableColumn.append(DataColumn(Text(i[1],width=Cellwidth[i[0]])))
        tableColumn.append(DataColumn(Text("aksi",width=Cellwidth[-1])))
        tableRow=[]
        for i in enumerate(data):
            temprow=[]
            temprow.append(DataCell(Text(i[0]+1,width=Cellwidth[0])))
            for z in enumerate(i[1],1):
                temprow.append(DataCell(Text("{}".format(i[1][z[1]]),width=Cellwidth[z[0]])))
            temprow.append(
                DataCell(
                    Row(
                        controls=[
                            IconButton(icon=icons.DELETE,on_click=deleteFunction),
                            IconButton(icon=icons.EDIT,on_click=editFunction)
                        ]
                    )
                )
            )
            tableRow.append(DataRow(temprow))
        return tableRow,tableColumn
    def createPopUpCard(title,content,button):
        return AlertDialog(
            modal=True,
            title=title,
            content=content,
            actions=button,
            actions_alignment=MainAxisAlignment.END,
        )   
    def notaPulangHapusKasirPopUpActionBatal(e):
        page.dialog.open=False
        page.update()
    def notaPulangHapusKasirPopUpButtonActionYa(e):
        page.dialog.open=False
        page.update()
    def alertDialogHapusKasirPopUp(e):
        card=createPopUpCard(Text("Hapus Kasir?"),Text("Apakah Anda yakin ingin menghapus Made Putra Teguh Pramana C. P? Data yang sudah dihapus tidak bisa dikembalikan."),alertYaorBatalkan)
        page.dialog=card
        card.open=True
        alertYaorBatalkan[0].on_click=notaPulangHapusKasirPopUpActionBatal
        alertYaorBatalkan[1].on_click=notaPulangHapusKasirPopUpButtonActionYa
        page.update()  
    def notaPulangHapusSalesPopUpButtonActionBatal(e):
        page.dialog.open=False
        page.update()
    def notaPulangHapusSalesPopUpButtonActionYa(e):
        page.dialog.open=False
        page.update()
    def alertDialogHapusSalesPopUp(e):
        card=createPopUpCard(Text("Hapus Sales?"),Text("Apakah Anda yakin ingin menghapus Made Putra Teguh Pramana C. P? Data yang sudah dihapus tidak bisa dikembalikan."),alertYaorBatalkan)
        page.dialog=card
        card.open=True
        alertYaorBatalkan[0].on_click=notaPulangHapusSalesPopUpButtonActionBatal
        alertYaorBatalkan[1].on_click=notaPulangHapusSalesPopUpButtonActionYa
        page.update()  
    def notaPulangEditSalesPopUpButtonActionBatal(e):
        page.dialog.open=False
        page.update()
    def notaPulangEditSalesPopUpButtonActionYa(e):
        page.dialog.open=False
        page.update()
    def alertDialogEditSalesPopUp(e):
        content=Container(
            content=Column(
                controls=[
                    Column(
                        controls=[
                            Text("ID Sales"),
                            TextField()
                        ]
                    ),
                    Column(
                        controls=[
                            Text("Nama Sales"),
                            TextField()
                        ]
                    ),
                    Column(
                        controls=[
                            Text("Alamat Sales"),
                            TextField()
                        ]
                    ),
                    Row(
                        controls=[
                            Column(
                                controls=[
                                    Text("Status"),
                                    TextField()
                                ]
                            ),
                            Column(
                                controls=[
                                    Text("No.Hp"),
                                    TextField()
                                ]
                            ),
                        ]
                    )
                ]
            ),
            width=page.window_width/100*50,
            height=page.window_height/100*80
        )
        card=createPopUpCard(Text("Edit Sales?"),content,alertYaorBatalkan)
        page.dialog=card
        card.open=True
        alertYaorBatalkan[0].on_click=notaPulangEditSalesPopUpButtonActionBatal
        alertYaorBatalkan[1].on_click=notaPulangEditSalesPopUpButtonActionYa
        page.update()  

    def notaPulangHapusNotaPopUpButtonActionBatal(e):
        page.dialog.open=False
        page.update()
    def notaPulangHapusNotaPopUpButtonActionYa(e):
        page.dialog.open=False
        page.update()
    def alertDialogHapusNotaPopUp(e):
        card=createPopUpCard(Text("Hapus Sales?"),Text("Apakah Anda yakin ingin menghapus Made Putra Teguh Pramana C. P? Data yang sudah dihapus tidak bisa dikembalikan."),alertYaorBatalkan)
        page.dialog=card
        card.open=True
        alertYaorBatalkan[0].on_click=notaPulangHapusNotaPopUpButtonActionBatal
        alertYaorBatalkan[1].on_click=notaPulangHapusNotaPopUpButtonActionYa
        page.update()  
    def buttonActionManajemenKasirTable(e):
        adminMainButton[structProperty["flag"]].style=style_unselected
        structProperty["flag"]=0
        adminMainButton[structProperty["flag"]].style=style_selected
        row,colheader=listDictToTableRowAndCol(dummy_data["ManajemenKasir"],deleteFunction=alertDialogHapusKasirPopUp,editFunction=alertDialogEditKasir)
        table.columns=colheader
        table.rows=row
        filterControlRow.clear()
        filterControlRow.extend(kasirSalesFilterRowControl)
        page.update()
    def buttonActionManajemenSalesTable(e):
        adminMainButton[structProperty["flag"]].style=style_unselected
        structProperty["flag"]=1
        adminMainButton[structProperty["flag"]].style=style_selected
        row,colheader=listDictToTableRowAndCol(dummy_data["ManajemenSales"],deleteFunction=alertDialogHapusSalesPopUp,editFunction=alertDialogEditSalesPopUp)
        table.columns=colheader
        table.rows=row
        filterControlRow.clear()
        filterControlRow.extend(kasirSalesFilterRowControl)
        page.update()
    def buttonActionManajemenNotaTable(e):
        adminMainButton[structProperty["flag"]].style=style_unselected
        structProperty["flag"]=2
        adminMainButton[structProperty["flag"]].style=style_selected
        row,colheader=listDictToTableRowAndCol(dummy_data["ManajemenNota"],deleteFunction=alertDialogHapusNotaPopUp,editFunction=lambda e : page.go("/DaftarNota"))
        table.columns=colheader
        table.rows=row
        filterControlRow.clear()
        filterControlRow.extend(manajemenNotaFilterRowControls)
        page.update()
    adminMainButton=[
        TextButton(
            "Manajemen Kasir",
            style=style_selected,
            width=page.window_width/100*40/100*50,
            on_click=buttonActionManajemenKasirTable
        ),
        TextButton(
            "Manajemen Sales",
            style=style_unselected,
            width=page.window_width/100*40/100*50,
            on_click=buttonActionManajemenSalesTable
        ),
        TextButton(
            "Manajemen Nota",
            style=style_unselected,
            width=page.window_width/100*40/100*50,
            on_click=buttonActionManajemenNotaTable
        )
    ]
    filterDropDownTipe=Dropdown(
        options=[
            dropdown.Option("Sales(Pulang)"),
            dropdown.Option("Sales(ambil)"),
            dropdown.Option("beli"),
            dropdown.Option("None"),
        ],
        label="Filter berdasarkan tipe"
    )
    filterDropDownStatus=Dropdown(
        options=[
            dropdown.Option("Selesai"),
            dropdown.Option("progess"),
            dropdown.Option("None"),
        ],
        label="Filter berdasarkan Status"
    )
    # def alertDialogTanggalDari(e):
    def changeDateDari(e):
        manajemenNotaFilterRowControls[1].text=datePickerDari.value.strftime("%d/%m/%Y")
        structProperty["dari"]=datePickerDari.value
        page.update()

    def date_picker_dismissed(e):
        pass
    datePickerDari = DatePicker(
        on_change=changeDateDari,
        on_dismiss=date_picker_dismissed,
        last_date=datetime.datetime.now(),
    )
    page.overlay.append(datePickerDari)

    def changeDateSampai(e):
        manajemenNotaFilterRowControls[3].text=datePickerSampai.value.strftime("%d/%m/%Y")
        structProperty["Sampai"]=datePickerSampai.value
        page.update()

    def date_picker_dismissed(e):
        pass
    datePickerSampai = DatePicker(
        on_change=changeDateSampai,
        on_dismiss=date_picker_dismissed,
        last_date=datetime.datetime.now(),
    )
    page.overlay.append(datePickerSampai)
    def buttonActionDialogEditBatalkan(e):
        page.dialog.open=False
        page.update()
    def buttonActionDialogEditYa(e):
        page.dialog.open=False
        page.update()
    def alertDialogEditKasir(e):
        content=Container(
            content=Column(
                controls=[
                    Column(
                        controls=[
                            Text("ID Kasir"),
                            TextField()
                        ]
                    ),
                    Column(
                        controls=[
                            Text("Nama Kasir"),
                            TextField()
                        ]
                    ),
                    Row(
                        controls=[
                            Column(
                                controls=[
                                    Text("Status"),
                                    TextField()
                                ]
                            ),
                            TextButton("Reset Password",on_click=lambda e : alertDialogPasswordGenerator(e,card))
                        ]
                    ),
                ]
            ),
            width=page.window_width/100*50,
            height=page.window_height/100*80
        )
        card=createPopUpCard(Text("Edit Kasir"),content,alertYaorBatalkan)
        page.dialog=card
        card.open=True
        alertYaorBatalkan[0].on_click=buttonActionDialogEditBatalkan
        alertYaorBatalkan[1].on_click=buttonActionDialogEditYa
        page.update()  
    def buttonActionDialogPasswordGeneratorBatalkan(e,card,pastContent,pastfunction,pastbutton):
        card.content=pastContent
        card.title=Text("Edit Kasir")
        for i in zip(pastfunction,pastbutton):
            i[1].on_click=i[0]
        page.update()
    def alertDialogPasswordGenerator(e,card):
        pastContent=card.content
        pastfunction=[alertYaorBatalkan[0].on_click,alertYaorBatalkan[1].on_click]
        content=Container(
            content=Column(
                controls=[
                    Text("Reset password untuk user Made Putra Teguh Pramana C. P"),
                    Row(
                        controls=[
                            Column(
                                controls=[
                                    Text("Password"),
                                    TextField()
                                ]
                            ),
                            TextButton("Randomize")
                        ]
                    )
                ]
            ),
            width=page.window_width/100*50,
            height=page.window_height/100*80
        )
        card.content=content
        card.title=Text("Reset Password")
        alertYaorBatalkan[0].on_click=lambda e: buttonActionDialogPasswordGeneratorBatalkan(e,card,pastContent,pastfunction,alertYaorBatalkan)
        alertYaorBatalkan[1].on_click=lambda e : alertDialogResetPasswordConfirm(e,card)
        page.update()  
    def buttonActionDialogResetPasswordConfirmBatalkan(e,card,pastContent,pastfunction,pastbutton):
        card.content=pastContent
        card.title=Text("Reset Password")
        for i in zip(pastfunction,pastbutton):
            i[1].on_click=i[0]
        page.update()
    def buttonActionDialogResetPasswordConfirmYa(e):
        page.dialog.open=False
        page.update()
    def alertDialogResetPasswordConfirm(e,card):
        pastContent=card.content
        pastfunction=[alertYaorBatalkan[0].on_click,alertYaorBatalkan[1].on_click]
        content=Container(
            content=Column(
                controls=[Text("Apakah anda yakin ingin melakukan reset password untuk user Made Putra Teguh Pramana C. P")]
            ),
            width=page.window_width/100*50,
            height=page.window_height/100*80
        )
        card.title=Text("Reset Password")
        card.content=content
        alertYaorBatalkan[0].on_click=lambda e: buttonActionDialogResetPasswordConfirmBatalkan(e,card,pastContent,pastfunction,alertYaorBatalkan)
        alertYaorBatalkan[1].on_click=buttonActionDialogResetPasswordConfirmYa
        page.update()
    
    manajemenNotaFilterRowControls=[
        Text("dari:"),
        TextButton("Tanggal",on_click=lambda _ : datePickerDari.pick_date()),
        Text("sampai:"),
        TextButton("Tanggal",on_click=lambda _ : datePickerSampai.pick_date()),
        filterDropDownTipe,
        filterDropDownStatus

    ]
    filterDropDownKasirSales=Dropdown(
        options=[
            dropdown.Option("Aktif"),
            dropdown.Option("Berhenti"),
            dropdown.Option("None"),
        ],
        label="Filter berdasarkan Status"
    )
    kasirSalesFilterRowControl=[
        filterDropDownKasirSales
    ]
    filterControlRow=[]
    filterControlRow.extend(kasirSalesFilterRowControl)
    dataRowTable,dataColumnTable=listDictToTableRowAndCol(dummy_data["ManajemenKasir"],deleteFunction=alertDialogHapusKasirPopUp,editFunction=alertDialogEditKasir)
    table=DataTable(
        columns=dataColumnTable,
        rows=dataRowTable
    )
    lowValue=min(structProperty["maxLength"],5)
    optionDropdownShowing=[dropdown.Option("{}".format(i+1)) for i in range(structProperty["maxLength"])]
    showingData=Dropdown(
        options=optionDropdownShowing
    )
    showingData.value=lowValue
    tableBottomSlider=[]
    tableBottomSlider.append(IconButton(icon=icons.ARROW_LEFT))
    for i in range(lowValue):
        tableBottomSlider.append(TextButton("{}".format(i+1)))
    tableBottomSlider.append(IconButton(icon=icons.ARROW_RIGHT))
    
    filterRow=[]
    body=Container(
            content=Column(
                controls=[
                    Text("Halaman Admin"),
                    Row(
                        controls=adminMainButton,
                        spacing=0
                    ),
                    Row(
                        controls=[
                            Row(
                                controls=filterControlRow
                            ),
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
                                controls=tableBottomSlider
                            )
                        ],
                        alignment=MainAxisAlignment.SPACE_BETWEEN
                    )
                ]
            ),
            bgcolor=COLOUR_JSON["White"],
            padding=padding.all(20),
            
        )
                
    view.controls.append(body)
    view.scroll=ScrollMode.AUTO