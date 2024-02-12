import sys
sys.path.append('../')
from utils.libs import *
from utils.importer import *


def main(view:View,super_page:Page):
    detailNotaContainer=[]
    daftarNotaList={
        "berlangsung":[],
        "selesai":[]
    }
    super_page.flagDaftarNota=True
    structProperty={}
    #buat 
    structProperty["changes"]={
        "changeAmbil":[],
        "changeStokAvailable":[],
        "changeDetailPulang":[],
        "deleteAmbil":[],
        "deletePulang":[],
        "addNotaHeader":[],
        "changeHeaderStatus":[],
        "addDetailPulang":[],
        "addAmbilPulang":[]
    }
    #buat fungsi untuk bersihin log nya
    def clearStuctProperty():
        structProperty["changes"]["changeAmbil"].clear()
        structProperty["changes"]["changeStokAvailable"].clear()
        structProperty["changes"]["changeDetailPulang"].clear()
        structProperty["changes"]["deleteAmbil"].clear()
        structProperty["changes"]["deletePulang"].clear()
        structProperty["changes"]["addNotaHeader"].clear()
        structProperty["changes"]["changeHeaderStatus"].clear()
        structProperty["changes"]["addDetailPulang"].clear()
        structProperty["changes"]["addAmbilPulang"].clear()
    def saveChanges():
        date=datetime.datetime.now()
        addNotaHeader(structProperty["changes"]["addNotaHeader"],date)
        addNotaDetailPulang(structProperty["changes"]["addDetailPulang"],date)
        updateStokAvailableByIdMultiple(structProperty["changes"]["changeStokAvailable"])
        updateNotaHeaderStatusById(structProperty["changes"]["changeHeaderStatus"],date)
        updateDetailNotaPulangIdStok(structProperty["changes"]["changeDetailPulang"],date)
        removeAndAddAmbil(structProperty["changes"]["addAmbilPulang"],date)
        
    structProperty["headerData"]=loadNotaHeaderByTime(None,datetime.datetime.now())
    structProperty["headerData"]=getAndJoinSalesById(structProperty["headerData"])
    listNamaSales=getSeriesIdAndNamaSales()
    listNamaBarang=getSeriesIdAndNamaKopi()
    listNamaToko=getSeriesIdAndNamaToko()
    namaBarangOption=[ dropdown.Option("{} - {}".format(x["id_kopi"],x["nama"])) for _,x in listNamaBarang.iterrows()]
    namaTokoOption=[ dropdown.Option("{} - {}".format(x["id_toko"],x["nama"])) for _,x in listNamaToko.iterrows()]
    dropdownNamaBarang=Dropdown(
        options=namaBarangOption
    )
    dropdownNamaToko=Dropdown(
        options=namaTokoOption
    )
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
    buttonTambahBarangNotaPulang=TextButton(
        "Tambah Barang",
        style=style_selectable,
    )
    salesDropOption=[ dropdown.Option("{} - {}".format(x["id_sales"],x["nama"])) for _,x in listNamaSales.iterrows()]
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
    def listToTableV2(DataFrame,icon_flag,pulang,jenis_transaksi):
        tempDataFrame=[]
        icon_row=[]
        rowWidth=super_page.window_width/100*40/100*16
        harga=0
        hargaCells=DataCell(Text("",width=rowWidth))
        for index,row in DataFrame.iterrows():
            temp = alertDialogEditingCellCard(row,index,DataFrame,jenis_transaksi)
            temp.hargaCells=hargaCells
            temp.jenisNotaPulang=pulang
            icon_cells=[
                IconButton(icon=icons.DELETE,disabled=icon_flag),
                IconButton(icon=icons.EDIT,disabled=icon_flag,on_click=temp.alert)
            ]
            icon_row.append(icon_cells)
            if pulang :
                temp.cells=[
                    DataCell(Text(str(index+1),width=super_page.window_width/100*40/100*4)),
                    DataCell(Text(row["nama"],width=super_page.window_width/100*40/100*22)),
                    DataCell(Text(str(row["qty"]),width=super_page.window_width/100*40/100*12)),
                    DataCell(Text("Rp.{}".format(row["harga_satuan"]*row["qty"]*(1-row["disc"]/100)),width=super_page.window_width/100*40/100*15)),
                    DataCell(Text(row["nama_toko"],width=super_page.window_width/100*40/100*15))
                ]
            else :
                temp.cells=[
                    DataCell(Text(str(index+1),width=super_page.window_width/100*40/100*4)),
                    DataCell(Text(row["nama"],width=super_page.window_width/100*40/100*22)),
                    DataCell(Text(str(row["qty"]),width=super_page.window_width/100*40/100*12)),
                    DataCell(Text("{}%".format(row["disc"]),width=super_page.window_width/100*40/100*12)),
                    DataCell(Text("Rp.{}".format(row["harga_satuan"]*row["qty"]*(1-row["disc"]/100)),width=super_page.window_width/100*40/100*15)),
                ]
            tempDataFrame.append(
                DataRow(
                    cells=[
                        *(temp.cells),
                        DataCell(Row(
                            controls=icon_cells
                        ))
                    ]
                )
            )
            if jenis_transaksi!=2:
                harga+=row["harga_satuan"]*row["qty"]*(1-row["disc"]/100)
            else:
                harga+=row["harga_satuan"]*row["qty"]
        hargaCells.content.value="Rp.{}".format(harga)
        if pulang:
            tempDataFrame.append(
                DataRow(
                    cells=[
                        DataCell(Text("")),
                        DataCell(Text("Total")),
                        DataCell(Text("")),
                        hargaCells,
                        DataCell(Text("")),
                        DataCell(Text(""))
                    ]
                )
            )
        else:
                        tempDataFrame.append(
                DataRow(
                    cells=[
                        DataCell(Text("")),
                        DataCell(Text("Total")),
                        DataCell(Text("")),
                        DataCell(Text("")),
                        hargaCells,
                        DataCell(Text(""))
                    ]
                )
            )
        return tempDataFrame,icon_row
    def batalkanNotaPulang(e):
        enableNotaButton([0,1])
        detailNotaContainer.pop()
        super_page.update()
    def selesaikanNotaPulang(e):
        enableNotaButton([0,1])        
        detailNotaContainer.clear()
        detailNotaContainer.append(NONEDATA)
        super_page.update()
    def TambahEditDataYes(e,data,tableRow):
        newNotaId=uuid.uuid4().hex
        newAmbilId=uuid.uuid4().hex
        #ngambil 1 id_nota,disc header dari data ini karena semua datanya sama
        notaId=structProperty["pulangdata"]["id_nota"][0]
        disc=structProperty["pulangdata"]["disc"][0]
        # data["namaBarang"]=dropdownNamaBarang.value
        # data["namaToko"]=dropdownNamaToko.value
        # data["hargaPerenceng"]=tambahDialogHargaPerRenceng.value
        # data["jumlahLaku"]=tambahAlertDialogJumlahLaku.value
        listQuery=getPossibleStokResolver(data["namaBarang"][0],int(data["jumlahLaku"]),[])
        barangDetail=getKopiById(data["namaBarang"][0])
        tokoDetail=getTokoById(data["namaToko"][0])
        for i in range(len(listQuery)):
            listQuery[i]=tuple(newAmbilId)+listQuery[i]
        tableRow.append()
        structProperty["changes"]["addAmbilPulang"].append(listQuery)
        #true berati nota berlangsung
        if not super_page.flagDaftarNota:
            structProperty["pulangdata"].loc[len(structProperty["pulangdata"])]={
                "id_toko":data["namaToko"][0],
                "id_kopi":data["namaBarang"][0],
                "index":len(structProperty["pulangdata"]),
                "id_nota_detail":newNotaId,
                "id_nota":notaId,
                "id_ambil":newAmbilId,
                "qty":int(data["jumlahLaku"]),
                "disc":disc,
                "harga_satuan":int(data["hargaPerenceng"]),
                "nama":barangDetail["nama"][0],
                "harga":barangDetail["harga"][0],
                "biaya_produksi":barangDetail["biaya_produksi"][0],
                "foto":barangDetail["foto"][0],
                "nama_toko":tokoDetail["nama"],
                "alamat":tokoDetail["alamat"],
            }
        else:
            structProperty["detailnew"].loc[len(structProperty["detailnew"])]={
                "id_toko":data["namaToko"][0],
                "id_kopi":data["namaBarang"][0],
                "index":len(structProperty["detailnew"]),
                "id_nota_detail":newNotaId,
                "id_nota":notaId,
                "id_ambil":newAmbilId,
                "qty":int(data["jumlahLaku"]),
                "disc":disc,
                "harga_satuan":int(data["hargaPerenceng"]),
                "nama":barangDetail["nama"][0],
                "harga":barangDetail["harga"][0],
                "biaya_produksi":barangDetail["biaya_produksi"][0],
                "foto":barangDetail["foto"][0],
                "nama_toko":tokoDetail["nama"],
                "alamat":tokoDetail["alamat"],
            }
        super_page.dialog.open=False
        super_page.update()
    def batalkanEditActionEdit(e):
        super_page.dialog.open=False
        super_page.update()
    class alertDialogEditingCellCard():
        def __init__(self,i,index,DataFrame,jenisTransaksi):
            self.i=i
            self.index=index
            self.cells=None
            self.hargaCells=None
            self.jenisNotaPulang=None
            self.dataFrame=DataFrame
            self.jenisTransaksi=jenisTransaksi
        def alert(self,e):
            self.hargaPerRenceng=TextField()
            self.jumlahLaku=TextField()
            content=Container(
                content=Column(
                    controls=[
                        Container(
                            content=Row(
                                controls=[
                                    Column(
                                        controls=[
                                            Text("Nama Barang"),
                                            dropdownNamaBarang
                                        ],
                                        width=super_page.window_width/100*50/100*45
                                    ),
                                    Column(
                                        controls=[
                                            Text("Harga Per Renceng"),
                                            self.hargaPerRenceng
                                        ],
                                        width=super_page.window_width/100*50/100*45,
                                    )
                                ],
                                spacing=10
                            )
                        ),
                        Container(
                                content=Row(
                                    controls=[
                                    Column(
                                        controls=[
                                            Text("Nama Toko"),
                                            dropdownNamaToko
                                        ],
                                        width=super_page.window_width/100*50/100*45
                                    ),
                                    Column(
                                        controls=[
                                            Text("Jumlah Laku"),
                                            self.jumlahLaku
                                        ],
                                        width=super_page.window_width/100*50/100*45
                                    )
                                ]
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
            alertYaorBatalkan[0].on_click=batalkanEditActionEdit
            alertYaorBatalkan[1].on_click=self.editDataActionYesRow
            super_page.update()
        def editDataActionYesRow(self,e):
            barang=dropdownNamaBarang.value.split(" - ")
            toko=dropdownNamaToko.value.split(" - ")
            harga_satuan=self.hargaPerRenceng.value
            stok=self.jumlahLaku.value
            #undo the latest changes of the same ambil id
            flagOfAvailableId=True
            newQuery=[]
            for k in range(len(structProperty["changes"]["addAmbilPulang"])-1,-1,-1):
                if str(structProperty["changes"]["addAmbilPulang"][k][0][0])==str(self.i["id_ambil"]):
                    dataAmbilList=structProperty["changes"]["addAmbilPulang"][k]
                    for z in dataAmbilList:
                        newQuery.append((z[1],z[3],datetimeToHashYearMonth(z[2])))
                    flagOfAvailableId=False
                    break
            if flagOfAvailableId:
                dataAmbil=getAmbilById(self.i["id_ambil"],datetime.datetime.now())
                for _,row in dataAmbil.iterrows():
                    newQuery.append((row["id_stok"],int(row["jumlah"]),datetimeToHashYearMonth(row["tanggal_stok"])))
            listOfAmbilTable=getPossibleStokResolver(int(barang[0]),int(stok),[*structProperty["changes"]["changeStokAvailable"],*newQuery])
            if listOfAmbilTable is None:
                print("tidak cukup stok")
                return
            for query in newQuery:
                structProperty["changes"]["changeStokAvailable"].append(query)
            #change the data in table for the gui
            self.dataFrame["nama"][self.index]=barang[1]
            self.dataFrame["id_kopi"][self.index]=barang[0]
            self.dataFrame["harga_satuan"][self.index]=int(harga_satuan)
            self.dataFrame["qty"][self.index]=int(stok)
            self.cells[1].content.value=barang[1]
            self.cells[2].content.value=stok
            # newPossibleStok=getLatestStokIdByKopiId(barang[0])
            # self.dataFrame["qty"][self.index]=stok
            for z in range(len(listOfAmbilTable)):
                #append the tuple
                listOfAmbilTable[z]=tuple([self.i["id_ambil"]])+listOfAmbilTable[z]
            # self.cells[3].content.value=barang[0]
            harga=0
            if self.jenisTransaksi!=2:
                self.cells[3].content.value="Rp.{}".format(int(harga_satuan)*int(stok))  
                for _,row in self.dataFrame.iterrows():
                    harga+=row["harga_satuan"]*row["qty"]
            else:
                self.cells[3].content.value="Rp.{}".format(int(harga_satuan)*int(stok)*(1-self.i["disc"]/100))  
                for _,row in self.dataFrame.iterrows():
                    harga+=row["harga_satuan"]*row["qty"]*(1-row["disc"]/100)
            if self.jenisNotaPulang:
                self.dataFrame["nama_toko"][self.index]=toko[1]
                self.dataFrame["id_toko"][self.index]=toko[0]
                self.cells[4].content.value=toko[1]
            if not super_page.flagDaftarNota:
                structProperty["changes"]["changeDetailPulang"].append((self.i["id_nota_detail"],int(self.i["id_ambil"]),int(harga_satuan),self.dataFrame["id_toko"][self.index],barang[0]))
            self.dataFrame["total"]=harga
            self.hargaCells.content.value="Rp.{}".format(harga)
            structProperty["changes"]["addAmbilPulang"].append(listOfAmbilTable)
            for k in listOfAmbilTable:
                structProperty["changes"]["changeStokAvailable"].append((k[1],-k[3],datetimeToHashYearMonth(k[2])))
            super_page.dialog.open=False
            super_page.update()
    tambahDialogHargaPerRenceng=TextField()
    tambahAlertDialogJumlahLaku=TextField()
    def alertDialogTambahRowNotaPulang(e,tableRow):
            data={}
            content=Container(
                content=Column(
                    controls=[
                        Container(
                            content=Row(
                                controls=[
                                    Column(
                                        controls=[
                                            Text("Nama Barang"),
                                            dropdownNamaBarang
                                        ],
                                        width=super_page.window_width/100*50/100*45
                                    ),
                                    Column(
                                        controls=[
                                            Text("Harga Per Renceng"),
                                            tambahDialogHargaPerRenceng
                                        ],
                                        width=super_page.window_width/100*50/100*45,
                                    )
                                ],
                                spacing=10
                            )
                        ),
                        Container(
                                content=Row(
                                    controls=[
                                    Column(
                                        controls=[
                                            Text("Nama Toko"),
                                            dropdownNamaToko
                                        ],
                                        width=super_page.window_width/100*50/100*45
                                    ),
                                    Column(
                                        controls=[
                                            Text("Jumlah Laku"),
                                            tambahAlertDialogJumlahLaku
                                        ],
                                        width=super_page.window_width/100*50/100*45
                                    )
                                ]
                            )
                        )
                    ],
                ),
            width=super_page.window_width/100*50,
            height=200,
            expand=True,
            padding=padding.all(0),
            )
            data["namaBarang"]=dropdownNamaBarang.value.split(" - ")
            data["namaToko"]=dropdownNamaToko.value.split(" - ")
            data["hargaPerenceng"]=tambahDialogHargaPerRenceng.value
            data["jumlahLaku"]=tambahAlertDialogJumlahLaku.value
            card=createPopUpCard(Text("Tambah Barang"),content,alertYaorBatalkan)
            super_page.dialog=card
            card.open=True
            alertYaorBatalkan[0].on_click=batalkanEditActionEdit
            alertYaorBatalkan[1].on_click=lambda e : TambahEditDataYes(e,data,tableRow)
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
            tableHeader=[
                DataColumn(Text("No",size=12,width=super_page.window_width/100*40/100*4,color=COLOUR_JSON["Gray/400"])),
                DataColumn(Text("Barang",size=12,width=super_page.window_width/100*40/100*22,color=COLOUR_JSON["Gray/400"])),
                DataColumn(Text("Kuantitas",size=12,width=super_page.window_width/100*40/100*12,color=COLOUR_JSON["Gray/400"])),
                # DataColumn(Text("Diskon",size=12,width=super_page.window_width/100*40/100*12,color=COLOUR_JSON["Gray/400"])),
                DataColumn(Text("Harga",size=12,width=super_page.window_width/100*40/100*15,color=COLOUR_JSON["Gray/400"])),
                DataColumn(Text("Toko",size=12,width=super_page.window_width/100*40/100*15,color=COLOUR_JSON["Gray/400"])),
                DataColumn(Text("Aksi",size=12,width=super_page.window_width/100*40/100*16,color=COLOUR_JSON["Gray/400"])),
            ]
            if super_page.flagDaftarNota:
                buttonTambahBarangNotaPulang.on_click=lambda e : alertDialogTambahRowNotaPulang(e,tableRow)
                rowDesc.append(
                    buttonTambahBarangNotaPulang
                )
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
                                "Sales : {}".format(data["nama"]),
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
            tableHeader=[
                DataColumn(Text("No",size=12,width=super_page.window_width/100*40/100*4,color=COLOUR_JSON["Gray/400"])),
                DataColumn(Text("Barang",size=12,width=super_page.window_width/100*40/100*22,color=COLOUR_JSON["Gray/400"])),
                DataColumn(Text("Kuantitas",size=12,width=super_page.window_width/100*40/100*12,color=COLOUR_JSON["Gray/400"])),
                DataColumn(Text("Diskon",size=12,width=super_page.window_width/100*40/100*12,color=COLOUR_JSON["Gray/400"])),
                DataColumn(Text("Harga",size=12,width=super_page.window_width/100*40/100*15,color=COLOUR_JSON["Gray/400"])),
                # DataColumn(Text("Toko",size=12,width=super_page.window_width/100*40/100*15,color=COLOUR_JSON["Gray/400"])),
                DataColumn(Text("Aksi",size=12,width=super_page.window_width/100*40/100*16,color=COLOUR_JSON["Gray/400"])),
            ]
        
        return Container(
            content=Column(
                controls=[
                        *rowDesc,
                        Container(
                            content=DataTable(
                                columns=tableHeader,
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
        saveChanges()
        clearStuctProperty()
        bottomCard.controls=detailNotaPulangSelesaiButton
        detailNotaPulangSelesaiButton[0].on_click=lambda e : ChangeCardToeditTable(e,bottomCard,icon_row)
        detailNotaPulangSelesaiButton[1].on_click=alertDialogNotaPulangSelesaiHapus
        super_page.dialog.open=False
        super_page.update()
    def notaPulangEditingActionbatalkan(e,bottomCard,icon_row):
        for i in icon_row:
            i[1].disabled=True
        clearStuctProperty()
        bottomCard.controls=detailNotaPulangSelesaiButton
        detailNotaPulangSelesaiButton[0].on_click=lambda e : ChangeCardToeditTable(e,bottomCard,icon_row)
        detailNotaPulangSelesaiButton[1].on_click=alertDialogNotaPulangSelesaiHapus
        super_page.dialog.open=False
        super_page.update()
    def ChangeCardToeditTable(e,bottomCard,icon_row):
        clearStuctProperty()
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
    def alertDialogNotaPulangSimpanActionYa(e,data):
        for index,row in structProperty["detailnew"].iterrows():
            structProperty["changes"]["addDetailPulang"].append((row["id_nota_detail"],row["id_nota"],row["id_ambil"],row["qty"],row["disc"],row["harga_satuan"],row["id_toko"],row["id_kopi"],row["id_kopi"]))
        #inget rubah id sales kalok udah ada system auth nya
        structProperty["changes"]["addNotaHeader"].append((data["id_nota"],data["total"],data["status_nota"],data["id_karyawan"],1,data["namapelangan"],data["id_sales"],datetime.datetime.now()))
        structProperty["changes"]["changeHeaderStatus"].append((data["id_nota"],1))
        saveChanges()
        clearStuctProperty()
        structProperty["headerData"]=loadNotaHeaderByTime(None,datetime.datetime.now())
        structProperty["headerData"]=getAndJoinSalesById(structProperty["headerData"])
        daftarNotaListToContainer(structProperty["headerData"])
        selesaikanNotaPulang(e)
        super_page.dialog.open=False
        super_page.update()
    def alertDialogNotaPulangSimpanActionBatal(e):
        super_page.dialog.open=False
        super_page.update()
    def alertDialogNotaPulangSimpan(e,data):
        card=createPopUpCard(Text("Simpan Perubahan? "),Text("Apakah Anda yakin ingin menyimpan perubahan pada nota?"),alertYaorBatalkan)
        alertYaorBatalkan[0].on_click=alertDialogNotaPulangSimpanActionBatal
        alertYaorBatalkan[1].on_click=lambda e : alertDialogNotaPulangSimpanActionYa(e,data)
        super_page.dialog=card
        card.open=True
        super_page.update()
    def createNotaBerlangsungPulang(e,data):
        disableNotaButton([0,1])
        #bersihin log query buat nanti nyimpen perubahannya
        clearStuctProperty()
        structProperty["detailnew"]=loadNotaDetailAmbilbyIdNota(data["id_nota"],datetime.datetime.now()).reset_index()
        # structProperty["detailnew"]=getAndJoinStokById(structProperty["detailnew"])
        structProperty["detailnew"]=getAndJoinKopiById(structProperty["detailnew"])
        #alertDialogEditingCellCard editing action ya mengisi nama_toko,id_toko bakalan 
        structProperty["detailnew"]=structProperty["detailnew"].loc[structProperty["detailnew"]["id_nota"]==data["id_nota"]]
        structProperty["detailnew"]["nama_toko"]=""
        structProperty["detailnew"]["id_toko"]=""
        columnOfid=createListofUUID(len(structProperty["detailnew"]))
        structProperty["detailnew"]["id_nota_detail"]=columnOfid
        # structProperty["detailnew"]=getAndJoinTokoById(structProperty["detailnew"])
        notaPulangRow,icon_row=listToTableV2(structProperty["detailnew"],False,True,data["jenis_transaksi"])
        for i in icon_row:
            i[0].visible=False
        NotaPulang,cardBottom=createNotaTableCard("Nota Pulang",data,notaPulangButton,notaPulangRow,True)
        detailNotaContainer.append(NotaPulang)
        notaPulangButton[0].on_click=lambda e : alertDialogNotaPulangSimpan(e,data)
        notaPulangButton[1].on_click=batalkanNotaPulang
        super_page.update()
    def dataToDetailNotaBerlangsung(data):
        enableNotaButton([0,1])
        structProperty["detaildata"]=loadNotaDetailAmbilbyIdNota(data["id_nota"],datetime.datetime.now()).reset_index()
        # structProperty["detaildata"]=getAndJoinStokById(structProperty["detaildata"])
        structProperty["detaildata"]=getAndJoinKopiById(structProperty["detaildata"])
        # structProperty["detaildata"]=getAndJoinTokoById(structProperty["detaildata"])
        rows_table,icon_row=listToTableV2(structProperty["detaildata"].loc[structProperty["detaildata"]["id_nota"]==data["id_nota"]],True,False,data["jenis_transaksi"])
        detailNotaContainer.clear()
        DetailNota,cardBottom=createNotaTableCard("DetailNota",data,detailNotaButton,rows_table,False)
        detailNotaContainer.append(DetailNota)
        detailNotaButton[1].on_click=lambda e : createNotaBerlangsungPulang(e,data)
        detailNotaButton[2].on_click=alertDialogDetailNotaBerlangsungHapus
    def dataToDetailNotaSelesai(data):
        dataselesaiambil=structProperty["headerData"].loc[(structProperty["headerData"]["id_nota"]==data["id_nota"]) & (structProperty["headerData"]["jenis_transaksi"]==0) ]
        dataselesaipulang=structProperty["headerData"].loc[(structProperty["headerData"]["id_nota"]==data["id_nota"]) & (structProperty["headerData"]["jenis_transaksi"]==1) ]
        structProperty["detaildata"]=loadNotaDetailAmbilbyIdNota(dataselesaiambil.iloc[0]["id_nota"],datetime.datetime.now()).reset_index()
        structProperty["pulangdata"]=loadNotaDetailPulangbyIdNota(dataselesaipulang.iloc[0]["id_nota"],datetime.datetime.now()).reset_index()
        # structProperty["detaildata"]=getAndJoinStokById(structProperty["detaildata"])
        # structProperty["pulangdata"]=getAndJoinStokById(structProperty["pulangdata"])
        structProperty["detaildata"]=getAndJoinKopiById(structProperty["detaildata"])
        structProperty["pulangdata"]=getAndJoinKopiById(structProperty["pulangdata"])
        # structProperty["detaildata"]=getAndJoinTokoById(structProperty["detaildata"])
        structProperty["pulangdata"]=getAndJoinTokoById(structProperty["pulangdata"])
        print(structProperty["pulangdata"].dtypes)
        rows_tableDetail,icon_rowDetail=listToTableV2(structProperty["detaildata"],True,False,0)
        rows_tablePulang,icon_rowPulang=listToTableV2(structProperty["pulangdata"],True,True,1)
        detailNotaContainer.clear()
        DetailNota,cardBottomDetail=createNotaTableCard("DetailNota",data,[],rows_tableDetail,False)
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
        daftarNotaList["berlangsung"].clear()
        daftarNotaList["selesai"].clear()
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
    daftarNotaListToContainer(structProperty["headerData"])
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