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
        "updateHeaderData":[],
        "addDetailPulang":[],
        "addAmbilPulang":[],
        "hapusNotaHeaderBerlangsung":[],
        "hapusNotaHeaderSelesai":[],
        "hapusDetailNotaBerlangsung":[],
        "hapusDetailNotaSelesai":[],
        "hapusAmbilTableNotaBerlangsung":[],
        "hapusAmbilTableNotaSelesai":[]
    }
    #buat fungsi untuk bersihin log nya
    def clearStuctProperty():
        structProperty["changes"]["changeAmbil"].clear()
        structProperty["changes"]["changeStokAvailable"].clear()
        structProperty["changes"]["changeDetailPulang"].clear()
        structProperty["changes"]["deleteAmbil"].clear()
        structProperty["changes"]["deletePulang"].clear()
        structProperty["changes"]["addNotaHeader"].clear()
        structProperty["changes"]["updateHeaderData"].clear()
        structProperty["changes"]["addDetailPulang"].clear()
        structProperty["changes"]["addAmbilPulang"].clear()
        structProperty["changes"]["hapusNotaHeaderBerlangsung"].clear()
        structProperty["changes"]["hapusNotaHeaderSelesai"].clear()
        structProperty["changes"]["hapusDetailNotaBerlangsung"].clear()
        structProperty["changes"]["hapusDetailNotaSelesai"].clear()
        structProperty["changes"]["hapusAmbilTableNotaBerlangsung"].clear()
        structProperty["changes"]["hapusAmbilTableNotaSelesai"].clear()
    def saveChanges():
        date=datetime.datetime.now()
        addNotaHeader(structProperty["changes"]["addNotaHeader"])
        addNotaDetailPulang(structProperty["changes"]["addDetailPulang"],date)
        updateStokAvailableByIdMultiple(structProperty["changes"]["changeStokAvailable"])
        updateNotaHeaderStatusAndTanggalPairByIdAndDate(structProperty["changes"]["updateHeaderData"])
        updateDetailNotaPulangIdStok(structProperty["changes"]["changeDetailPulang"])
        removeAndAddAmbil(structProperty["changes"]["addAmbilPulang"],date)
        deleteNotaHeaderBelangsung(structProperty["changes"]["hapusNotaHeaderBerlangsung"])
        deleteNotaDetailAmbilBelangsung(structProperty["changes"]["hapusDetailNotaBerlangsung"])
        deleteNotaHeaderSelesai(structProperty["changes"]["hapusNotaHeaderSelesai"])
        deleteNotaDetailAmbilSelesai(structProperty["changes"]["hapusDetailNotaSelesai"])
        deleteAmbilTableNotaById(structProperty["changes"]["hapusAmbilTableNotaBerlangsung"])
        deleteAmbilTableNotaById(structProperty["changes"]["hapusAmbilTableNotaSelesai"])

    structProperty["headerData"]=loadNotaHeaderByTime(datetime.datetime.now(),31)
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
                dropdown.Option(text="Hari ini",key=1),
                dropdown.Option(text="Bulan ini",key=31),
                dropdown.Option(text="Tahun ini",key=365),
            ],
            width=super_page.window_width/100*40/100*25
        ),
        Dropdown(
            options=salesDropOption,
            width=super_page.window_width/100*40/100*25
        )
    ]
    searchButton=TextField(
        label="Cari nota",
        bgcolor=COLOUR_JSON["Primary/100"],
        border_radius=border_radius.all(25),
        border_color=COLOUR_JSON["Primary/100"],
        prefix_icon=icons.SEARCH,
        color=COLOUR_JSON["Primary/900"],
    )
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
    def listToTableV2(DataFrame,icon_flag,pulang,jenis_transaksi,tanggal):
        tempDataFrame=[]
        icon_row=[]
        rowWidth=super_page.window_width/100*40/100*16
        harga=0
        hargaCells=DataCell(Text("",width=rowWidth))
        for index,row in DataFrame.iterrows():
            if jenis_transaksi==0:
                harga+=row["harga_satuan"]*row["qty"]*(1-row["disc"]/100)
            else:
                harga+=row["harga_satuan"]*row["qty"]
            temp = alertDialogEditingCellCard(row,index,DataFrame,jenis_transaksi,tanggal)
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
                    DataCell(Text("Rp.{}".format(harga),width=super_page.window_width/100*40/100*15)),
                    DataCell(Text(row["nama_toko"],width=super_page.window_width/100*40/100*15))
                ]
            else :
                temp.cells=[
                    DataCell(Text(str(index+1),width=super_page.window_width/100*40/100*4)),
                    DataCell(Text(row["nama"],width=super_page.window_width/100*40/100*22)),
                    DataCell(Text(str(row["qty"]),width=super_page.window_width/100*40/100*12)),
                    DataCell(Text("{}%".format(row["disc"]),width=super_page.window_width/100*40/100*12)),
                    DataCell(Text("Rp.{}".format(harga),width=super_page.window_width/100*40/100*15)),
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
    def TambahEditDataYes(e,data,tableRow,tanggal,flag_icon,icon_row):
        newNotaId=uuid.uuid4().hex
        newAmbilId=uuid.uuid4().hex
        # data["namaBarang"]=dropdownNamaBarang.value
        # data["namaToko"]=dropdownNamaToko.value
        # data["hargaPerenceng"]=tambahDialogHargaPerRenceng.value
        # data["jumlahLaku"]=tambahAlertDialogJumlahLaku.value
        data["namaBarang"]=data["value"]["barang"].value.split(" - ")
        data["namaToko"]=data["value"]["toko"].value.split(" - ")
        data["jumlahLaku"]=data["value"]["jumlah"].value
        data["hargaPerenceng"]=data["value"]["harga"].value
        # structProperty["changes"]["changeStokAvailable"]
        listQuery=getPossibleStokResolver(data["namaBarang"][0],int(data["jumlahLaku"]),[])
        barangDetail=getKopiById(data["namaBarang"][0])
        tokoDetail=getTokoById(data["namaToko"][0])
        for i in range(len(listQuery)):
            listQuery[i]=tuple([newAmbilId])+listQuery[i]
        structProperty["changes"]["addAmbilPulang"].append(listQuery)
        #true berati nota berlangsung
        if not super_page.flagDaftarNota:
            #ngambil 1 id_nota,disc header dari data ini karena semua datanya sama
            notaId=structProperty["pulangdata"]["id_nota"][0]
            disc=structProperty["pulangdata"]["disc"][0]
            row={
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
                "nama_toko":tokoDetail["nama"][0],
                "alamat":tokoDetail["alamat"],
            }
            structProperty["changes"]["addDetailPulang"].append((
                newNotaId,
                notaId,
                newAmbilId,
                int(data["jumlahLaku"]),
                disc,
                int(data["hargaPerenceng"]),
                data["namaToko"][0],
                data["namaBarang"][0]
            ))
            temp=alertDialogEditingCellCard(row,len(tableRow),structProperty["pulangdata"],1,tanggal)
            structProperty["pulangdata"].loc[len(structProperty["pulangdata"])]=row
            hargaIndex=3
            harga=structProperty["pulangdata"]["harga_satuan"]*structProperty["pulangdata"]["qty"]
            harga=harga.sum()
        else:
            #ngambil 1 id_nota,disc header dari data ini karena semua datanya sama
            notaId=structProperty["detailnew"]["id_nota"][0]
            disc=structProperty["detailnew"]["disc"][0]
            row={
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
                "nama_toko":tokoDetail["nama"][0],
                "alamat":tokoDetail["alamat"],
            }
            structProperty["detailnew"].loc[len(structProperty["detailnew"])]=row
            temp=alertDialogEditingCellCard(row,len(tableRow),structProperty["detailnew"],1,tanggal)
            hargaIndex=3
            harga=structProperty["detailnew"]["harga_satuan"]*structProperty["detailnew"]["qty"]
            harga=harga.sum()
        temp.cells=[
            DataCell(Text(str(len(tableRow)),width=super_page.window_width/100*40/100*4)),
            DataCell(Text(row["nama"],width=super_page.window_width/100*40/100*22)),
            DataCell(Text(str(row["qty"]),width=super_page.window_width/100*40/100*12)),
            DataCell(Text("Rp.{}".format(row["harga_satuan"]*row["qty"]),width=super_page.window_width/100*40/100*15)),
            DataCell(Text(row["nama_toko"],width=super_page.window_width/100*40/100*15))
        ]
        icon_cells=[
            IconButton(icon=icons.DELETE,disabled=flag_icon),
            IconButton(icon=icons.EDIT,disabled=flag_icon,on_click=temp.alert)
        ]
        tableRow.insert(len(tableRow)-1,
            DataRow(
                cells=[
                    *(temp.cells),
                    DataCell(Row(
                        controls=icon_cells
                    ))
                ]
            )
        )
        finalRow=tableRow[-1].cells[hargaIndex]
        temp.hargaCells=tableRow[-1].cells[hargaIndex]
        #true karena fungsinya ini bakalan di pake di nota pulang aja (sementara)
        temp.jenisNotaPulang=True
        finalRow.content=Text("Rp.{}".format(harga))
        icon_row.append(icon_cells)
        super_page.dialog.open=False
        super_page.update()
    def batalkanEditActionEdit(e):
        super_page.dialog.open=False
        super_page.update()
    class alertDialogEditingCellCard():
        def __init__(self,i,index,DataFrame,jenisTransaksi,tanggal):
            #important
            #kalok misal ada yang error karena ada Nonetype di alertDialog biasanya masalahnya karena belom di assign manual tanpa make initnya
            self.i=i
            self.index=index
            #variable cells dipake nanti untuk nge refrence row yang ada di tablenya biar bisa diubah 
            self.cells=None
            #variable hargaCell ku pake nanti assign cell di table pas total nota pulang/ambil jadi harus di assgin manual
            self.hargaCells=None
            #variablenya jenisNotaPulang buat nentuin apa nota pulang atau ngak kalok misal nota ambil mau di ubah bisa di ubah caranyimpennya. 
            self.jenisNotaPulang=None
            self.dataFrame=DataFrame
            self.jenisTransaksi=jenisTransaksi
            self.tanggal=tanggal
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
            formatTanggal="%d/%m/%Y %H:%M"
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
                dataAmbil=getAmbilById(self.i["id_ambil"],datetime.datetime.strptime(self.tanggal,formatTanggal))
                for _,row in dataAmbil.iterrows():
                    newQuery.append((row["id_stok"],int(row["jumlah"]),datetimeToHashYearMonth(datetime.datetime.strptime(row["tanggal_stok"],formatTanggal))))
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
                structProperty["changes"]["changeDetailPulang"].append((self.i["id_nota_detail"],str(self.i["id_ambil"]),int(harga_satuan),self.dataFrame["id_toko"][self.index],barang[0],datetime.datetime.strptime(self.tanggal,formatTanggal),int(stok)))
            self.dataFrame["total"]=harga
            self.hargaCells.content.value="Rp.{}".format(harga)
            structProperty["changes"]["addAmbilPulang"].append(listOfAmbilTable)
            for k in listOfAmbilTable:
                structProperty["changes"]["changeStokAvailable"].append((k[1],-k[3],datetimeToHashYearMonth(k[2])))
            super_page.dialog.open=False
            super_page.update()
    tambahDialogHargaPerRenceng=TextField()
    tambahAlertDialogJumlahLaku=TextField()
    def alertDialogTambahRowNotaPulang(e,tableRow,tanggal,flag_icon,icon_row):
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
            data["value"]={
                "barang":dropdownNamaBarang,
                "toko":dropdownNamaToko,
                "harga":tambahDialogHargaPerRenceng,
                "jumlah":tambahAlertDialogJumlahLaku
            }
            card=createPopUpCard(Text("Tambah Barang"),content,alertYaorBatalkan)
            super_page.dialog=card
            card.open=True
            alertYaorBatalkan[0].on_click=batalkanEditActionEdit
            alertYaorBatalkan[1].on_click=lambda e : TambahEditDataYes(e,data,tableRow,tanggal,flag_icon,icon_row)
            super_page.update()
    def createNotaTableCard(header,data,button,tableRow,pulang,icon_flag,icon_row):
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
            # if super_page.flagDaftarNota:
            buttonTambahBarangNotaPulang.on_click=lambda e : alertDialogTambahRowNotaPulang(e,tableRow,data["tanggal"],icon_flag,icon_row)
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
    def notaPulangSelesaikanNotaPopUpButtonActionYa(e,bottomCard,icon_row,data):
        for i in icon_row:
            i[1].disabled=True
        saveChanges()
        clearStuctProperty()
        bottomCard.controls=detailNotaPulangSelesaiButton
        detailNotaPulangSelesaiButton[0].on_click=lambda e : ChangeCardToeditTable(e,bottomCard,icon_row,data)
        detailNotaPulangSelesaiButton[1].on_click=lambda e : alertDialogNotaPulangSelesaiHapus(e,data)
        super_page.dialog.open=False
        super_page.update()
    def notaPulangEditingActionbatalkan(e,bottomCard,icon_row,data):
        for i in icon_row:
            i[1].disabled=True
        clearStuctProperty()
        bottomCard.controls=detailNotaPulangSelesaiButton
        detailNotaPulangSelesaiButton[0].on_click=lambda e : ChangeCardToeditTable(e,bottomCard,icon_row,data)
        detailNotaPulangSelesaiButton[1].on_click=lambda e : alertDialogNotaPulangSelesaiHapus(e,data)
        # super_page.dialog.open=False
        super_page.update()
    def ChangeCardToeditTable(e,bottomCard,icon_row,data):
        clearStuctProperty()
        for i in icon_row:
            i[1].disabled=False
        bottomCard.controls=notaPulangEditingButton
        notaPulangEditingButton[0].on_click=lambda e : alertDialogNotaPulangSelesai(e,bottomCard,icon_row,data)
        notaPulangEditingButton[1].on_click=lambda e : notaPulangEditingActionbatalkan(e,bottomCard,icon_row,data)
        super_page.update()
    #function di call untuk ngeluarin pop up di nota pulang yang selesai 
    def alertDialogNotaPulangSelesai(e,bottomCard,icon_row,data):
        card=createPopUpCard(Text("Simpan Nota Pulang"),Text("Apakah Anda yakin ingin menyimpan perubahan pada nota pulang?"),alertYaorBatalkan)
        super_page.dialog=card
        card.open=True
        alertYaorBatalkan[1].on_click=lambda e : notaPulangSelesaikanNotaPopUpButtonActionYa(e,bottomCard,icon_row,data)
        alertYaorBatalkan[0].on_click= notaPulangSelesaikanNotaPopUpButtonActionBatal
        super_page.update()
    def notaPulangSelesaiHapusNotaPopUpButtonActionBatal(e):
        super_page.dialog.open=False
        super_page.update()
    def notaPulangSelesaiHapusNotaPopUpButtonActionYa(e,data):
        clearStuctProperty()
        # "changeAmbil":[],
        # "changeStokAvailable":[],
        # "changeDetailPulang":[],
        # "deleteAmbil":[],
        # "deletePulang":[],
        # "addNotaHeader":[],
        # "updateHeaderData":[],
        # "addDetailPulang":[],
        # "addAmbilPulang":[],
        # "hapusNotaHeaderBerlangsung":[],
        # "hapusNotaHeaderSelesai":[],
        # "hapusDetailNotaBerlangsung":[],
        # "hapusDetailNotaSelesai":[],
        # "hapusAmbilTableNotaBerlangsung":[],
        # "hapusAmbilTableNotaSelesai":[]
        formatTanggal="%d/%m/%Y %H:%M"
        tanggal=datetime.datetime.strptime(data["pulang"]["tanggal"],formatTanggal)
        structProperty["changes"]["hapusNotaHeaderSelesai"].append((data["pulang"]["id_nota"],tanggal))
        structProperty["changes"]["hapusDetailNotaSelesai"].append((data["pulang"]["id_nota"],tanggal))
        structProperty["changes"]["updateHeaderData"].append((data["pulang"]["id_nota"],0,tanggal,pd.NA,0))
        detailAmbil=loadNotaDetailPulangbyIdNota(data["pulang"]["id_nota"],tanggal)
        detailAmbil=getAndJoinAmbilById(detailAmbil,tanggal)
        for index,row in detailAmbil.iterrows(): 
            structProperty["changes"]["hapusAmbilTableNotaSelesai"].append((row["id_ambil"],tanggal))
            structProperty["changes"]["changeStokAvailable"].append((row["id_stok"],int(row["jumlah"]),datetimeToHashYearMonth(tanggal)))
        saveChanges()
        clearStuctProperty()
        if filterDetailNotaBerlangsung[0].value is None:
            time=31
        else :
            time=int(filterDetailNotaBerlangsung[0].value)
        structProperty["headerData"]=loadNotaHeaderByTime(datetime.datetime.now(),time)
        structProperty["headerData"]=getAndJoinSalesById(structProperty["headerData"])
        daftarNotaListToContainer(structProperty["headerData"])
        detailNotaContainer.clear()
        detailNotaContainer.append(NONEDATA)
        super_page.dialog.open=False
        super_page.update()
    def alertDialogNotaPulangSelesaiHapus(e,data):
        card=createPopUpCard(Text("Hapus Nota Pulang?"),Text("Apakah Anda yakin ingin menghapus Nota Pulang? Nota yang sudah dihapus tidak bisa dikembalikan.\n\nStatus nota akan kembali menjadi “Nota Berlangsung”!"),alertYaorBatalkan)
        super_page.dialog=card
        card.open=True
        alertYaorBatalkan[0].on_click=notaPulangSelesaiHapusNotaPopUpButtonActionBatal
        alertYaorBatalkan[1].on_click=lambda e : notaPulangSelesaiHapusNotaPopUpButtonActionYa(e,data)
        super_page.update()
    #hapusNotaBerlangsung
    def detailNotaBerlangsungHapusPopUpButtonActionYa(e,data):
        clearStuctProperty()
        formatTanggal="%d/%m/%Y %H:%M"
        tanggal=datetime.datetime.strptime(data["tanggal"],formatTanggal)
        structProperty["changes"]["hapusNotaHeaderBerlangsung"].append((data["id_nota"],tanggal))
        structProperty["changes"]["hapusDetailNotaBerlangsung"].append((data["id_nota"],tanggal))
        detailAmbil=loadNotaDetailAmbilbyIdNota(data["id_nota"],tanggal)
        detailAmbil=getAndJoinAmbilById(detailAmbil,tanggal)
        for index,row in detailAmbil.iterrows(): 
            structProperty["changes"]["hapusAmbilTableNotaBerlangsung"].append((row["id_ambil"],tanggal))
            structProperty["changes"]["changeStokAvailable"].append((row["id_stok"],int(row["jumlah"]),datetimeToHashYearMonth(tanggal)))
        saveChanges()
        clearStuctProperty()
        if filterDetailNotaBerlangsung[0].value is None:
            time=31
        else :
            time=int(filterDetailNotaBerlangsung[0].value)
        structProperty["headerData"]=loadNotaHeaderByTime(datetime.datetime.now(),time)
        structProperty["headerData"]=getAndJoinSalesById(structProperty["headerData"])
        daftarNotaListToContainer(structProperty["headerData"])
        detailNotaContainer.clear()
        detailNotaContainer.append(NONEDATA)
        super_page.dialog.open=False
        super_page.update()
    def detailNotaBerlangsungHapusPopUpButtonActionBatal(e):
        super_page.dialog.open=False
        super_page.update()
    def alertDialogDetailNotaBerlangsungHapus(e,data):
        card=createPopUpCard(Text("Hapus Nota?"),Text("Apakah Anda yakin ingin menghapus Nota? Nota yang sudah dihapus tidak bisa dikembalikan."),alertYaorBatalkan)
        super_page.dialog=card
        card.open=True
        alertYaorBatalkan[0].on_click=detailNotaBerlangsungHapusPopUpButtonActionBatal
        alertYaorBatalkan[1].on_click=lambda e : detailNotaBerlangsungHapusPopUpButtonActionYa(e,data)
        super_page.update()
    def alertDialogNotaPulangSimpanActionYa(e,data):
        formatTanggal="%d/%m/%Y %H:%M"
        for index,row in structProperty["detailnew"].iterrows():
            structProperty["changes"]["addDetailPulang"].append(
                (
                    row["id_nota_detail"]
                    ,row["id_nota"],
                    row["id_ambil"],
                    row["qty"],
                    row["disc"],
                    row["harga_satuan"],
                    row["id_toko"]
                    ,row["id_kopi"],
                    row["id_kopi"]
                    )
                )
        #inget rubah id sales kalok udah ada system auth nya
        structProperty["changes"]["addNotaHeader"].append((data["id_nota"],data["total"],1,data["id_karyawan"],1,data["namapelangan"],data["id_sales"],datetime.datetime.now(),datetime.datetime.strptime(data["tanggal"],formatTanggal)))
        structProperty["changes"]["updateHeaderData"].append((data["id_nota"],1,datetime.datetime.strptime(data["tanggal"],formatTanggal),datetime.datetime.now(),0))
        saveChanges()
        clearStuctProperty()
        #reload the data
        if filterDetailNotaBerlangsung[0].value is None:
            time=31
        else :
            time=int(filterDetailNotaBerlangsung[0].value)
        structProperty["headerData"]=loadNotaHeaderByTime(datetime.datetime.now(),time)
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
        formatTanggal="%d/%m/%Y %H:%M"
        disableNotaButton([0,1])
        #bersihin log query buat nanti nyimpen perubahannya
        clearStuctProperty()
        structProperty["detailnew"]=loadNotaDetailAmbilbyIdNota(data["id_nota"],datetime.datetime.strptime(data["tanggal"],formatTanggal)).reset_index(drop=True)
        # structProperty["detailnew"]=getAndJoinStokById(structProperty["detailnew"])
        structProperty["detailnew"]=getAndJoinKopiById(structProperty["detailnew"])
        #alertDialogEditingCellCard editing action ya mengisi nama_toko,id_toko bakalan 
        structProperty["detailnew"]=structProperty["detailnew"].loc[structProperty["detailnew"]["id_nota"]==data["id_nota"]]
        structProperty["detailnew"]["nama_toko"]=""
        structProperty["detailnew"]["id_toko"]=""
        columnOfid=createListofUUID(len(structProperty["detailnew"]))
        structProperty["detailnew"]["id_nota_detail"]=columnOfid
        structProperty["detaildata"]["tanggal_pair"]=datetime.datetime.strftime(datetime.datetime.now(),formatTanggal)
        structProperty["detailnew"]["tanggal"]=datetime.datetime.strftime(datetime.datetime.now(),formatTanggal)
        # structProperty["detailnew"]=getAndJoinTokoById(structProperty["detailnew"])
        notaPulangRow,icon_row=listToTableV2(structProperty["detailnew"],False,True,data["jenis_transaksi"],data["tanggal"])
        NotaPulang,cardBottom=createNotaTableCard("Nota Pulang",data,notaPulangButton,notaPulangRow,True,False,icon_row)
        for i in icon_row:
            i[0].visible=False
        detailNotaContainer.append(NotaPulang)
        notaPulangButton[0].on_click=lambda e : alertDialogNotaPulangSimpan(e,data)
        notaPulangButton[1].on_click=batalkanNotaPulang
        super_page.update()
    def dataToDetailNotaBerlangsung(data):
        formatTanggal="%d/%m/%Y %H:%M"
        enableNotaButton([0,1])
        structProperty["detaildata"]=loadNotaDetailAmbilbyIdNota(data["id_nota"],datetime.datetime.strptime(data["tanggal"],formatTanggal)).reset_index(drop=True)
        # structProperty["detaildata"]=getAndJoinStokById(structProperty["detaildata"])
        structProperty["detaildata"]=getAndJoinKopiById(structProperty["detaildata"])
        # structProperty["detaildata"]=getAndJoinTokoById(structProperty["detaildata"])
        rows_table,icon_row=listToTableV2(structProperty["detaildata"].loc[structProperty["detaildata"]["id_nota"]==data["id_nota"]],True,False,data["jenis_transaksi"],data["tanggal"])
        detailNotaContainer.clear()
        DetailNota,cardBottom=createNotaTableCard("DetailNota",data,detailNotaButton,rows_table,False,True,icon_row)
        detailNotaContainer.append(DetailNota)
        detailNotaButton[1].on_click=lambda e : createNotaBerlangsungPulang(e,data)
        detailNotaButton[2].on_click=lambda e : alertDialogDetailNotaBerlangsungHapus(e,data)
    def dataToDetailNotaSelesai(data):
        formatTanggal="%d/%m/%Y %H:%M"
        dataselesaipulang=structProperty["headerData"].loc[(structProperty["headerData"]["id_nota"]==data["id_nota"]) & (structProperty["headerData"]["jenis_transaksi"]==1) ]
        dataDetailAmbilHeader=loadNotaHeaderByTime(date=datetime.datetime.strptime(dataselesaipulang.iloc[0]["tanggal_pair"],formatTanggal),daysBehind=1)
        dataselesaiambil=dataDetailAmbilHeader.loc[(dataDetailAmbilHeader["id_nota"]==data["id_nota"]) & (dataDetailAmbilHeader["jenis_transaksi"]==0) ]
        structProperty["detaildata"]=loadNotaDetailAmbilbyIdNota(dataselesaiambil.iloc[0]["id_nota"],datetime.datetime.strptime(dataselesaiambil.iloc[0]["tanggal"],formatTanggal)).reset_index(drop=True)
        structProperty["pulangdata"]=loadNotaDetailPulangbyIdNota(dataselesaipulang.iloc[0]["id_nota"],datetime.datetime.strptime(dataselesaipulang.iloc[0]["tanggal"],formatTanggal)).reset_index(drop=True)
        # structProperty["detaildata"]=getAndJoinStokById(structProperty["detaildata"])
        # structProperty["pulangdata"]=getAndJoinStokById(structProperty["pulangdata"])
        structProperty["detaildata"]=getAndJoinKopiById(structProperty["detaildata"])
        structProperty["pulangdata"]=getAndJoinKopiById(structProperty["pulangdata"])
        # structProperty["detaildata"]=getAndJoinTokoById(structProperty["detaildata"])
        structProperty["pulangdata"]=getAndJoinTokoById(structProperty["pulangdata"])
        rows_tableDetail,icon_rowDetail=listToTableV2(structProperty["detaildata"],True,False,0,dataselesaiambil.iloc[0]["tanggal"])
        rows_tablePulang,icon_rowPulang=listToTableV2(structProperty["pulangdata"],True,True,1,dataselesaipulang.iloc[0]["tanggal"])
        detailNotaContainer.clear()
        DetailNota,cardBottomDetail=createNotaTableCard("DetailNota",data,[],rows_tableDetail,False,True,icon_rowDetail)
        detailNotaContainer.append(DetailNota)
        NotePulang,cardBottomPulang=createNotaTableCard("Nota Pulang",data,detailNotaPulangSelesaiButton,rows_tablePulang,True,True,icon_rowPulang)
        detailNotaContainer.append(NotePulang)
        for i in icon_rowPulang:
            i[0].visible=False
        detailNotaPulangSelesaiButton[0].on_click=lambda e : ChangeCardToeditTable(e,cardBottomPulang,icon_rowPulang,{"pulang":dataselesaipulang.iloc[0],"ambil":dataselesaiambil.iloc[0]})
        detailNotaPulangSelesaiButton[1].on_click=lambda e : alertDialogNotaPulangSelesaiHapus(e,{"pulang":dataselesaipulang.iloc[0],"ambil":dataselesaiambil.iloc[0]} )

    def filterWaktuNotaDanCashierNota(e):
        detailNotaContainer.clear()
        clearStuctProperty()
        detailNotaContainer.append(NONEDATA)
        if filterDetailNotaBerlangsung[0].value is None:
            time=31
        else :
            time=int(filterDetailNotaBerlangsung[0].value)
        structProperty["headerData"]=loadNotaHeaderByTime(datetime.datetime.now(),time)
        structProperty["headerData"]=getAndJoinSalesById(structProperty["headerData"])
        if not filterDetailNotaBerlangsung[1].value is None:
            value=filterDetailNotaBerlangsung[1].value.split(" - ")
            structProperty["headerData"]=structProperty["headerData"].loc[structProperty["headerData"]["id_karyawan"].astype(str)==value[0]]
        structProperty["headerData"]=structProperty["headerData"].loc[structProperty["headerData"]["id_nota"].astype(str).str.contains(searchButton.value)]
        # find_substring
        daftarNotaListToContainer(structProperty["headerData"])
        super_page.update()

    filterDetailNotaBerlangsung[0].on_change=filterWaktuNotaDanCashierNota
    filterDetailNotaBerlangsung[1].on_change=filterWaktuNotaDanCashierNota
    searchButton.on_submit=filterWaktuNotaDanCashierNota

    def hapusNotaHeaderBerlangsung(data):
        #nerima (row header)
        pass
        

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
        for index,row in data.loc[(data["status_nota"]==1) & (data["jenis_transaksi"]==1)].iterrows():
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
                            searchButton,
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