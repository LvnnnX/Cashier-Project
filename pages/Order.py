import sys

sys.path.append("../")
from utils.libs import *
from utils.importer import *

def main(view: View, super_page : Page):
    colors = load_colors()
    # page.title = "Home"
    # page.
    # view.bgcolor = colors["Gray/50"]
    
    toko_dummy_data = [
        {
            'id_toko' : 1,
            'nama' : 'Toko Rizky',
            'alamat' : 'Jl. Raya Bogor',
        },
        {
            'id_toko' : 2,
            'nama' : 'Toko Rizky',
            'alamat' : 'Jl. Raya Bogor',
        }
    ]
    
    karyawan_dummy_data = [{
        'id_sales' : 1,
        'nama' : 'Rizky',
        'alamat' : 'Jl. Raya Bogor',
        'no_hp' : '081234567890',
        'status' : 1,
        'role' : 0,
        'gaji_default' : 1000000,
    },{
        'id_sales' : 2,
        'nama' : 'Rizky',
        'alamat' : 'Jl. Raya Bogor',
        'no_hp' : '081234567890',
        'status' : 1,
        'role' : 0,
        'gaji_default' : 1000000, 
    }]
    
    nota_header_dummy_data = [
        {
            'id_nota' : 1,
            'total' : 100000,
            'status_nota' : 1,
            'id_kasir' : 1,
            'id_nota_primary' : 1,
            'jenis_transaksi' : 'ambil',
            'nama_pelanggan' : 'Rizky',
            'id_sales' : 1,
            'tanggal' : '2021-08-31 00:00:00', 
        },
        {
            'id_nota' : 2,
            'total' : 100000,
            'status_nota' : 1,
            'id_kasir' : 1,
            'id_nota_primary' : 2,
            'jenis_transaksi' : 'ambil',
            'nama_pelanggan' : 'Rizky',
            'id_sales' : 1,
            'tanggal' : '2021-08-31 00:00:00',
        }
    ]
    
    nota_detail_dummy_data = [
        {
            'id_kopi' : 1,
            'id_nota_primary' : 1,
            'id_nota_detail' : 1,
            'harga_satuan' : 100000,
            'discount' : 0,
            'kuantitas' : 1,
            'id_toko' : 1,
        },
        {
            'id_kopi' : 2,
            'id_nota_primary' : 1,
            'id_nota_detail' : 2,
            'harga_satuan' : 100000,
            'discount' : 0,
            'kuantitas' : 1,
            'id_toko' : 1,
        }
    ]
    
    stok_dummy_data = [
        {
            'id_stok' : 1,
            'id_kopi' : 1,
            'tanggal_exp' : '2021-08-31 00:00:00',
            'stok' : 100,
            'tanggal_masuk' : '2021-08-31 00:00:00',
        },
        {
            'id_stok' : 2,
            'id_kopi' : 2,
            'tanggal_exp' : '2021-08-31 00:00:00',
            'stok' : 100,
            'tanggal_masuk' : '2021-08-31 00:00:00',
        }
    ]

    kopi_dummy_data = [
        {
            'id_kopi' : 1,
            'nama' : 'Kopi Rizky',
            'harga' : 100000,
            'biaya_produksi' : 100000,
            'stok' : 100,
        },
        {
            'id_kopi' : 2,
            'nama' : 'Kopi Fajar',
            'harga' : 50000,
            'biaya_produksi' : 200,
            'stok' : 150,
        }
    ]
    
    sales_dummy_data = [
        {
            'id_sales' : 1,
            'nama' : 'Rizky',
            'alamat' : 'Jl. Raya Bogor',
            'no_hp' : '081234567890',
            'status' : 1,
        }
    ]
    
    stok_data = pd.DataFrame(stok_dummy_data)
    kopi_data = pd.DataFrame(kopi_dummy_data)
    
    notaContainer = []
    
    def changeCurrency(harga):
        str_harga = ''
        harga=str(harga)
        try:
            harga_lebih = harga.split('.')[1]
            harga = harga.split('.')[0]
            start_ = len(harga) % 3 if len(harga) % 3 != 0 else 3
            str_harga += harga[:start_] + '.'
            harga = harga[start_:]
            while len(harga):
                if len(harga) >= 3:
                    str_harga += harga[:3] + '.'
                    harga=harga[3:]
                else:
                    str_harga += harga
                    harga=''
            if(str_harga[-1]=='.'):
                str_harga=str_harga[:-1]
            return str_harga + ',' + harga_lebih[:2]
        except:
            start_ = len(harga) % 3 if len(harga) % 3 != 0 else 3
            str_harga += harga[:start_] + '.'
            harga = harga[start_:]
            while len(harga):
                if len(harga) >= 3:
                    str_harga += harga[:3] + '.'
                    harga=harga[3:]
                else:
                    str_harga += harga
                    harga=''
            if(str_harga[-1]=='.'):
                str_harga=str_harga[:-1]
            return str_harga
    # OS_SIZE = get_monitors()[0]
    # OS_WIDTH, OS_HEIGHT = OS_SIZE.width, OS_SIZE.height
    OS_WIDTH = super_page.window_width
    OS_HEIGHT = super_page.window_height

    # page.window_width = OS_WIDTH
    # page.window_height = OS_HEIGHT
    # # page.window_full_screen = True
    # page.window_focused = True
    
    style_JenisNota_selectable=ButtonStyle(
        shape=RoundedRectangleBorder(radius=0),
        color={
            MaterialState.DEFAULT:colors["Primary/500"],
            MaterialState.FOCUSED:colors["White"],
            MaterialState.HOVERED:colors["White"],
        },
        side = BorderSide(1,colors["Primary/500"]),
        overlay_color='transparent',
        bgcolor={
            MaterialState.DEFAULT:colors["White"],
            MaterialState.FOCUSED:colors["Primary/500"],
            MaterialState.HOVERED:colors["Primary/500"],
        }
    )
    
    style_JenisNota_selected=ButtonStyle(
        shape=RoundedRectangleBorder(radius=0),
        color={
            MaterialState.DEFAULT:colors["White"],
            MaterialState.FOCUSED:colors["White"],
            MaterialState.HOVERED:colors["White"],
        },
        side=BorderSide(1, colors["Primary/500"]),
        bgcolor={
            MaterialState.DEFAULT:colors["Primary/500"],
            MaterialState.FOCUSED:colors["Primary/500"],
            MaterialState.HOVERED:colors["Primary/700"],
        }
    )
    
    style_selectable=ButtonStyle(
        shape=RoundedRectangleBorder(radius=10),
        color={
            MaterialState.DEFAULT:colors["Primary/500"],
            MaterialState.FOCUSED:colors["White"],
            MaterialState.HOVERED:colors["White"],
        },
        side=BorderSide(1,colors["Primary/500"]),
        overlay_color='transparent',
        bgcolor={
            MaterialState.DEFAULT:colors["White"],
            MaterialState.FOCUSED:colors["Primary/500"],
            MaterialState.HOVERED:colors["Primary/500"],
        }
    )

    style_focus_selected=ButtonStyle(
        shape=RoundedRectangleBorder(radius=10),
        color={
            MaterialState.DEFAULT:colors["White"],
            MaterialState.FOCUSED:colors["White"],
            MaterialState.HOVERED:colors["White"],
        },
        side=BorderSide(1, colors["Primary/500"]),
        bgcolor={
            MaterialState.DEFAULT:colors["Primary/500"],
            MaterialState.FOCUSED:colors["Primary/500"],
            MaterialState.HOVERED:colors["Primary/700"],
        }
    )

    alertYaorBatalkan=[
        TextButton(
            "Batalkan",
            style=style_selectable,
            width=super_page.window_width/100*40/100*20,
            # on_click=lambda e: batalkanEditActionEdit(e)
        ),
        TextButton(
            "Ya",
            style=style_focus_selected,
            width=super_page.window_width/100*40/100*20,
            # on_click=lambda e: yaActionYes(e)
            # on_click=
        ),
    ]

    PopUp_JumlahBarangField = TextField(
                            input_filter=NumbersOnlyInputFilter(),
                            border_color=colors['Primary/300'],
                            border_radius=8,
                            # height=super_page.window_height/100*4,
                            # icon=icons.ADD,
                            # padding=padding.all(10)
                        )
    
    PopUp_DiskonField = TextField(
                            input_filter=NumbersOnlyInputFilter(),
                            border_color=colors['Primary/300'],
                            border_radius=8,
                            # height=super_page.window_height/100*4,
                        )


    daftar_nota_button=[
        TextButton(
            "Nota Sales",
            style=style_JenisNota_selected,
            width=super_page.window_width/100*40/100*25,
            disabled=True

        ),
        TextButton(
            "Nota Pembelian",
            style=style_JenisNota_selectable,
            width=super_page.window_width/100*40/100*25,
            # disabled=True
        )
    ]


    def TambahBarangPopUp_Card(e,i):
        content = Container(
            content=Column(
                controls=[
                    Container(
                        Text(
                            "Masukkan Jumlah Barang (kg)",
                            size=16,
                            # weight="bold",
                            color=colors['Black'],
                        )
                    ),
                    Container(
                        PopUp_JumlahBarangField
                    ),
                    Container(
                        Text(
                            "Masukkan Diskon (%)",
                            size=16,
                            # weight="bold",
                            color=colors['Black'],
                        )
                    ),
                    Container(
                        PopUp_DiskonField
                    ),
                ]
            ),
            width=super_page.window_width/100*30,
            height=super_page.window_height/100*20,
            # bgcolor=colors['White']
        )
        return AlertDialog(
            modal=True,
            title=Text("Tambah Barang“{}”?".format(i), weight='bold'),
            content=content,
            actions=[*alertYaorBatalkan],
            actions_alignment=MainAxisAlignment.END,
            # on_dismiss=lambda e: getPopUpData(e),
            # on_dismiss=print('Dismissed!'),
        )
        
    def EditPopUp_Card(e,i):
        content = Container(
            content=Column(
                controls=[
                    Container(
                        Text(
                            "Masukkan Jumlah Barang (kg)",
                            size=16,
                            # weight="bold",
                            color=colors['Black'],
                        )
                    ),
                    Container(
                        PopUp_JumlahBarangField
                    ),
                    Container(
                        Text(
                            "Masukkan Diskon (%)",
                            size=16,
                            # weight="bold",
                            color=colors['Black'],
                        )
                    ),
                    Container(
                        PopUp_DiskonField
                    ),
                ]
            ),
            width=super_page.window_width/100*50,
            height=super_page.window_height/100*20,
            # bgcolor=colors['White']
        )
        return AlertDialog(
            modal=True,
            title=Text("Edit Barang“{}”".format(i), weight='bold'),
            content=content,
            actions=[*alertYaorBatalkan],
            actions_alignment=MainAxisAlignment.END,
            # on_dismiss=lambda e: getPopUpData(e),
            # on_dismiss=print('Dismissed!'),
        )

    def PopUp_HapusNota_Card(e):
        return AlertDialog(
            modal=True,
            title=Text("Hapus Nota?", weight='bold'),
            content=Text("Apakah Anda yakin ingin menghapus nota ini?"),
            actions=alertYaorBatalkan,
            actions_alignment=MainAxisAlignment.END,
            # on_dismiss=lambda e: getPopUpData(e),
            # on_dismiss=print('Dismissed!'),
        )
    

    class PopUp_Tambah():
        def __init__(self, data):
            self.data = data
        
        def make_data(self):
            return {
                'Barang' : self.data['nama'],
                'Kuantitas' : int(PopUp_JumlahBarangField.value),
                'Diskon' : int(PopUp_DiskonField.value),
                'Harga' : int(self.data['harga']),
            }
        
        def yaActionYes(self, e):
        # print('Running')
            if PopUp_JumlahBarangField.value != '' and PopUp_DiskonField.value != '':
                data = self.make_data()
                # total_harga = isi_column.rows[:,4].sum()
                
                # if(isi_column.rows!=[]):
                #     total_harga=0
                #     # total_harga = isi_column.rows[0].sum()
                #     print(isi_column.rows[0].cells[4])
                #     for i in isi_column.rows[:-1]:
                #         total_harga+=int(i.cells[4].content.value[3:])
                # else:
                #     total_harga = 0
                
                isi_column.rows, iconRow=createNotaRow([data], False, isi_column.rows)
                
                # print(PopUp_JumlahBarangField.value, PopUp_DiskonField.value, self.data)
                # isi_column.rows=createNotaRow([makeData(data)], False)[0]
                # print(e.values)
                PopUp_JumlahBarangField.value=''
                PopUp_DiskonField.value=''
                # super_page.update()
                
            super_page.dialog.open=False
            super_page.update()
            
                    
        def batalkanEditActionEdit(self, e):
            PopUp_DiskonField.value=''
            PopUp_JumlahBarangField.value=''
            super_page.dialog.open=False
            super_page.update()
            
        def alert(self, e):
            Container(
            content=Column(
                controls=[
                    Container(
                        Text(
                            "Masukkan Jumlah Barang (kg)",
                            size=16,
                            # weight="bold",
                            color=colors['Black'],
                        )
                    ),
                    Container(
                        PopUp_JumlahBarangField
                    ),
                    Container(
                        Text(
                            "Masukkan Diskon (%)",
                            size=16,
                            # weight="bold",
                            color=colors['Black'],
                        )
                    ),
                    Container(
                        PopUp_DiskonField
                    ),
                ]
            ),
            width=super_page.window_width/100*50,
            height=super_page.window_height/100*20,
            # bgcolor=colors['White']
        )
            
            card = TambahBarangPopUp_Card(e, self.data['nama'])
            super_page.dialog=card
            card.open=True
            alertYaorBatalkan[0].on_click=self.batalkanEditActionEdit
            alertYaorBatalkan[1].on_click=self.yaActionYes
            super_page.update()

    class PopUp_Edit():
        def __init__(self, data):
            self.data=data

        def yaActionYes(self, e):
        # print('Running')
            if PopUp_JumlahBarangField.value != '' and PopUp_DiskonField.value != '':
                data = self.make_data()
                isi_column.rows, iconRow=createNotaRow([data], False)
                for i in iconRow:
                    i[0].visible=False
                    
                # print(PopUp_JumlahBarangField.value, PopUp_DiskonField.value, self.data)
                # isi_column.rows=createNotaRow([makeData(data)], False)[0]
                # print(e.values)
                PopUp_JumlahBarangField.value=''
                PopUp_DiskonField.value=''
                # super_page.update()
                
            super_page.dialog.open=False
            super_page.update()
            
                    
        def batalkanEditActionEdit(self, e):
            PopUp_DiskonField.value=''
            PopUp_JumlahBarangField.value=''
            super_page.dialog.open=False
            super_page.update()


        def alert(self, e):
            Container(
                content=Column(
                    controls=[
                        Container(
                            Text(
                                "Masukkan Jumlah Barang (kg)",
                                size=16,
                                # weight="bold",
                                color=colors['Black'],
                            )
                        ),
                        Container(
                            PopUp_JumlahBarangField
                        ),
                        Container(
                            Text(
                                "Masukkan Diskon (%)",
                                size=16,
                                # weight="bold",
                                color=colors['Black'],
                            )
                        ),
                        Container(
                            PopUp_DiskonField
                        ),
                    ]
                ),
                width=super_page.window_width/100*50,
                height=super_page.window_height/100*20,
                # bgcolor=colors['White']
            )
            
            card = EditPopUp_Card(e, self.data['nama'])
            super_page.dialog=card
            card.open=True
            alertYaorBatalkan[0].on_click=self.batalkanEditActionEdit
            alertYaorBatalkan[1].on_click=self.yaActionYes
            super_page.update()
            
    class PopUp_HapusNota():
        def yaActionYes(self, e):
            isi_column.rows = []
            super_page.dialog.open=False
            super_page.update()
            
        def batalkanEditActionEdit(self, e):
            super_page.dialog.open=False
            super_page.update()
        
        def alert(self, e):
            card = PopUp_HapusNota_Card(e)
            super_page.dialog=card
            card.open=True
            alertYaorBatalkan[0].on_click=self.batalkanEditActionEdit
            alertYaorBatalkan[1].on_click=self.yaActionYes
            super_page.update()
            


    # for each item, width 250, height 250
    def get_items(N: int = 10, window_width=750, window_height=600):
        items_list = []
        for key,value in stok_data.iterrows():
            # print(i)
            kopi_now = kopi_data[kopi_data['id_kopi'] == value['id_kopi']]
            nama = kopi_now['nama'].values[0]
            harga = kopi_now['harga'].values[0]
            stok = kopi_now['stok'].values[0]
            # def TambahBarangPopUp(e,nama):
            #     card=TambahBarangPopUp_Card(e,nama)
            #     # print(nama)
            #     super_page.dialog=card
            #     card.open=True
            #     alertYaorBatalkan[0].on_click=batalkanEditActionEdit
            #     alertYaorBatalkan[1].on_click=yaActionYes
            #     super_page.update()
            # print(nama)
            temp = PopUp_Tambah(kopi_now.iloc[0])
            
            tambah_button = Container(
                            alignment=alignment.center,
                            data=key,
                            content=ElevatedButton(
                                "Tambah Barang",
                                # width=200,
                                # height=40,
                                # border_radius=0,
                                bgcolor=colors["Primary/500"],
                                color=colors["White"],
                                on_click=temp.alert,
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
                        )
            
            # print(tambah_button.control.data)
            items_list.append(
                Container(
                    width=window_width/2 * 0.8,
                    height=window_height/4.8,
                    bgcolor=colors["Primary/100"],
                    margin=margin.only(left=10, right=10),
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
                                                            value=nama,
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
                                                            value=f"Stok: {changeCurrency(stok)}",
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
                                                            value=f"Rp{changeCurrency(str(harga))}",
                                                            weight="bold",
                                                            color=colors["Black"],
                                                        ),
                                                    ),
                                                ]
                                            ),
                                        ),
                                    ]
                                ),
                                #was here
                                tambah_button
                            ]
                        ),
                    ),
                ),
            )
            
        return items_list

    searchbar = Container(
        # bgcolor=colors['Black'],
        width=super_page.window_width/100*40-140,
        content=Column(
            controls=[
                Container(
                    # bgcolor=colors['Black'],
                    content=
                    Row(
                    alignment=MainAxisAlignment.SPACE_BETWEEN,
                    # vertical_alignment=CrossAxisAlignment.START,
                    controls=[
                        Text(
                            "Varian Kopi",
                            weight=FontWeight.BOLD,
                            size=30,
                            color=colors['Black'],
                        ),

                            Text(
                            "2 Varian Tersedia",
                            weight=FontWeight.W_500,
                            size=16,
                            color=colors['blackAlpha/500'],
                            )
                        
                    ]
                )
                )
                
                
            ]
        )
    )

    dummy_data = Container(
        width=super_page.window_width/100*40,
        height=super_page.window_height*90/100-(super_page.window_height*35/100),
        # height=OS_HEIGHT - OS_HEIGHT / 3,
        # margin=margin.only(top=10, left=0),
        # bgcolor=colors["Black"],
        border_radius=10,
        content=Row(
            # spacing=40,  # kesamping
            run_spacing=20,  # kebawah
            alignment=MainAxisAlignment.SPACE_BETWEEN,
            wrap=True,
            scroll=ScrollMode.AUTO,
            controls=[
                # Container(
                #     width=275,
                #     height=275,
                #     bgcolor=colors["Accent"],
                #     content=Text(
                #         value='1'
                #     )
                # ),
                *get_items(20, super_page.window_width/100*40, super_page.window_height-150),
            ],
        ),
    )

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
        # TextButton(
        #     "Hapus Nota",
        #     style=style_selectable,
        #     width=super_page.window_width/100*40/100*32
        # )
    ]   
        
    detailNotaButton[1].on_click=PopUp_HapusNota().alert
        
    isi_column=DataTable(
                columns=[
                    DataColumn(Text("No",size=12,width=super_page.window_width/100*40/100*8,color=colors["Gray/400"])),
                    DataColumn(Text("Barang",size=12,width=super_page.window_width/100*40/100*20,color=colors["Gray/400"])),
                    DataColumn(Text("Kuantitas",size=12,width=super_page.window_width/100*40/100*16,color=colors["Gray/400"])),
                    DataColumn(Text("Diskon",size=12,width=super_page.window_width/100*40/100*14,color=colors["Gray/400"])),
                    DataColumn(Text("Harga",size=12,width=super_page.window_width/100*40/100*18,color=colors["Gray/400"])),
                    DataColumn(Text("Aksi",size=12,width=super_page.window_width/100*40/100*16,color=colors["Gray/400"])),
                ],
                width=super_page.window_width/100*40,
                column_spacing=0,
                
        )
    
    
        
    def convertbackCurrency(harga):
        try:
            return harga.split[0].replace('.','')
        except:
            return harga.replace('.','')
        
    def createNotaRow(data, icon_flag, tempList=[], total_harga=0):
        # print(data)
        # tempList=[]
        flag_add=False
        flag_stop=False
        if tempList!=[]:
            tempList=tempList[:-1]
            flag_add=True
            # total_harga=0
            for i in tempList:
                harga = convertbackCurrency(i.cells[4].content.value[2:])
                discount = i.cells[3].content.value[:-1]
                kuantitas = i.cells[2].content.value
                barang = i.cells[1].content.value
                if barang == str(data[0]['Barang']) and discount == str(data[0]['Diskon']):
                    kuantitas = int(kuantitas) + data[0]['Kuantitas']
                    flag_stop=True
                    # i.cells[4].content.value = "Rp{}".format(int(i.cells[4].content.value[2:]) + data[0]['Harga']*data[0]['Kuantitas']*(1-(data[0]['Diskon']/100)))
                    # return tempList, iconRow
                # print(i)
                
                total_harga+=int(harga) * int(kuantitas) * (1-(int(discount)/100))
        else:
            total_harga=data[0]['Harga']*data[0]['Kuantitas']*(1-(data[0]['Diskon']/100))
        iconRow=[]
        rowWidth=super_page.window_width/100*40/100
        # total_harga=0
        if(not flag_stop):
            for num,i in enumerate(data):
                temp = PopUp_Edit(i)
                icon_cells=[
                    IconButton(icon=icons.DELETE, disabled=icon_flag),
                    IconButton(icon=icons.EDIT,disabled=icon_flag, on_click=temp.alert),
                ]
                iconRow.append(icon_cells)
                tempList.append(
                    DataRow(
                        cells=[
                            DataCell(Text(str(len(tempList)+1), width=rowWidth*8)),
                            DataCell(Text(str(i["Barang"]), width=rowWidth*20)),
                            DataCell(Text(str(i["Kuantitas"]), width=rowWidth*16)),
                            DataCell(Text(f"{i['Diskon']}%", width=rowWidth*14)),
                            DataCell(Text(f"Rp{changeCurrency(i['Harga'])}", width=rowWidth*18)),
                            DataCell(Row(controls=icon_cells, alignment=alignment.center_left, width=rowWidth*16))
                        ]
                    )
                )
                if(flag_add):
                    total_harga+= i['Harga']*i['Kuantitas']*(1-(i['Diskon']/100))
        tempList.append(
            DataRow(
                cells=[
                    DataCell(Text("Total")),
                    DataCell(Text("")),
                    DataCell(Text("")),
                    DataCell(Text("")),
                    DataCell(Text("Rp{}".format(changeCurrency(total_harga)),width=rowWidth*24)),
                    DataCell(Text(""))
                ]
            )
        )
        return tempList, iconRow

    rowDesc=[
            Text(
                "Detail Nota",
                weight=FontWeight.BOLD,
                size=20,
                color=colors['Black']
            ),
            Container(
                content=Row(
                    controls=[
                        Text(
                            "ID Nota : {}".format("id_nota"),
                            color=colors["blackAlpha/500"]
                        ),
                        Text(
                            "Kasir : {}".format('id_kasir'),
                            color=colors["blackAlpha/500"]
                        )
                    ],
                    alignment=MainAxisAlignment.SPACE_BETWEEN
                ),
                width=super_page.window_width/100*40,
            )
        ]


    
    detail_nota_button =Container(
                        content=Row(
                        controls=detailNotaButton,
                        alignment=MainAxisAlignment.CENTER,
                        spacing=5
        ),
        width=super_page.window_width/100*40,
    )
    
    notaContainer.append([Container(content=isi_column,alignment=alignment.center,),detail_nota_button])
    
    def Nota_sales_clicked(e):
        daftar_nota_button[0].style=style_JenisNota_selected
        daftar_nota_button[0].disabled=True
        daftar_nota_button[1].style=style_JenisNota_selectable
        daftar_nota_button[1].disabled=False
        super_page.flagNotaSales = True
        notaContainer.clear()
        notaContainer.append([])
        super_page.update()
        
    def Nota_pembelian_clicked(e):
        daftar_nota_button[1].style=style_JenisNota_selected
        daftar_nota_button[1].disabled=True
        daftar_nota_button[0].style=style_JenisNota_selectable
        daftar_nota_button[0].disabled=False
        super_page.flagNotaSales = False
        notaContainer.clear()
        notaContainer.append([Container(content=isi_column,alignment=alignment.center,),detail_nota_button])
        super_page.update()

    daftar_nota_button[0].on_click=Nota_sales_clicked
    daftar_nota_button[1].on_click=Nota_pembelian_clicked




    body=Container(
        content=Row(
            controls=[
                Container(
                    # expand=True,
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
                                color=colors['Black'],
                            ),
                                    Text(
                                "2 Varian Tersedia",
                                weight=FontWeight.W_500,
                                size=16,
                                color=colors['blackAlpha/500'],
                                    )
                                ]
                                
                            ),
                            
                            TextField(
                                label="Cari produk",
                                bgcolor=colors["Primary/100"],
                                border_radius=border_radius.all(25),
                                border_color=colors["Primary/100"],
                                prefix_icon=icons.SEARCH,
                                color=colors["Primary/900"],
                            ),
                            # Text("NANTI DISINI ADA FILTER COMING SOON!"),
                            dummy_data
                        ],
                        spacing=30
                    ),
                    bgcolor="White",
                    width=super_page.window_width/100*40,
                    padding=padding.all(20),
                    height=super_page.window_height*90/100-150
                ),
                Container(
                    # bgcolor=colors['Black']
                    content=Column(
                        controls=[
                            Container(
                                content=Column(
                                    controls=[
                                        Row(
                                            controls=daftar_nota_button,
                                            spacing=0,
                                            ),
                                        *rowDesc,
                                        *notaContainer[0]],
                                        alignment=MainAxisAlignment.START,
                                        spacing=10,
                                    ),
                                    bgcolor="White",
                                    # width=super_page.window_width/100*40,
                                    # height=super_page.window_height/100*40,
                                    padding=padding.all(20)
                                )
                                                    ],
                                                    scroll=ScrollMode.AUTO,
                                                ),
                                            )
                                        ],
                                        alignment=MainAxisAlignment.SPACE_EVENLY,
                                        vertical_alignment=CrossAxisAlignment.START
                                    )
                                    ,bgcolor=colors["Gray/50"],
                                    width=super_page.window_width,
                                    height=super_page.window_height-150,
                                    padding=padding.only(top=20)
        )

    # page.add(mainpage)
    view.controls.append(body)

if __name__ == "__main__":
    app(target=main)  
