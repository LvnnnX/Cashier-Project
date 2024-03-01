import sys

sys.path.append("../")
from utils.libs import *
from utils.importer import *
from utils.converter import *

def main(view: View, super_page: Page):
    global modebarang
    colors = load_colors()

    listNamaSales = getSeriesIdAndNamaSales()
    listNamaBarang = getSeriesIdAndNamaKopi()
    listNamaToko = getSeriesIdAndNamaToko()
    stok_data = getFullStok(datetime.datetime.now())
    kopi_data = getSeriesFullKopi()

    style_selectable_round0 = ButtonStyle(
        shape=RoundedRectangleBorder(radius=0),
        color={
            MaterialState.DEFAULT: colors["Primary/500"],
            MaterialState.FOCUSED: colors["White"],
            MaterialState.HOVERED: colors["White"],
        },
        side=BorderSide(1, colors["Primary/500"]),
        overlay_color="transparent",
        bgcolor={
            MaterialState.DEFAULT: colors["White"],
            MaterialState.FOCUSED: colors["Primary/500"],
            MaterialState.HOVERED: colors["Primary/500"],
        },
    )

    style_selected_round0 = ButtonStyle(
        shape=RoundedRectangleBorder(radius=0),
        color={
            MaterialState.DEFAULT: colors["White"],
            MaterialState.FOCUSED: colors["White"],
            MaterialState.HOVERED: colors["White"],
        },
        side=BorderSide(1, colors["Primary/500"]),
        bgcolor={
            MaterialState.DEFAULT: colors["Primary/500"],
            MaterialState.FOCUSED: colors["Primary/500"],
            MaterialState.HOVERED: colors["Primary/700"],
        },
    )

    style_selectable_round8 = ButtonStyle(
        shape=RoundedRectangleBorder(radius=8),
        color={
            MaterialState.DEFAULT: colors["Primary/500"],
            MaterialState.FOCUSED: colors["White"],
            MaterialState.HOVERED: colors["White"],
        },
        side=BorderSide(1, colors["Primary/500"]),
        bgcolor={
            MaterialState.DEFAULT: colors["White"],
            MaterialState.FOCUSED: colors["Primary/500"],
            MaterialState.HOVERED: colors["Primary/500"],
        },
    )

    style_selected_round8 = ButtonStyle(
        shape=RoundedRectangleBorder(radius=8),
        color={
            MaterialState.DEFAULT: colors["White"],
            MaterialState.FOCUSED: colors["White"],
            MaterialState.HOVERED: colors["White"],
        },
        side=BorderSide(1, colors["Primary/500"]),
        bgcolor={
            MaterialState.DEFAULT: colors["Primary/500"],
            MaterialState.FOCUSED: colors["Primary/500"],
            MaterialState.HOVERED: colors["Primary/700"],
        },
    )

    jenis_stok_button = [
        TextButton(
            "Manajemen Barang",
            style=style_selected_round0,
            width=super_page.window_width / 100 * 40 / 100 * 25,
            disabled=True,
        ),
        TextButton(
            "Manajemen Stok",
            style=style_selectable_round0,
            width=super_page.window_width / 100 * 40 / 100 * 25,
            # disabled=True
        ),
    ]

    barang_baru_button = TextButton(
        "Barang Baru",
        width=super_page.window_width / 100 * 40 / 100 * 20,
        style=ButtonStyle(
            shape=RoundedRectangleBorder(radius=8),
            color={
                MaterialState.DEFAULT: colors["White"],
                MaterialState.FOCUSED: colors["White"],
                MaterialState.HOVERED: colors["White"],
            },
            side=BorderSide(1, colors["Primary/500"]),
            bgcolor={
                MaterialState.DEFAULT: colors["Primary/500"],
                MaterialState.FOCUSED: colors["Primary/500"],
                MaterialState.HOVERED: colors["Primary/700"],
            },
        ),
    )

    pencarian_field = [
        Text(
            "Pencarian:",
            color=colors["Black"],
        ),
        TextField(
            hint_text="cari sesuatu",
            hint_style=TextStyle(
                color=colors["Gray/300"],
            ),
            text_size=12,
            text_align=TextAlign.LEFT,
            color=colors["Black"],
            content_padding=padding.only(
                top=super_page.window_height / 100 * 0.5,
                left=super_page.window_width / 100 * 0.5,
            ),
            width=super_page.window_width / 100 * 40 / 100 * 20,
            height=super_page.window_height / 100 * 4,
            border_color=colors["Gray/400"],
        ),
    ]

    alertSimpanBarang = [
        TextButton(
            "Simpan Barang",
            style=style_selected_round8,
            width=super_page.window_width / 100 * 40 / 100 * 20,
        ),
        TextButton(
            "Batal",
            style=style_selectable_round8,
            width=super_page.window_width / 100 * 40 / 100 * 20,
        ),
    ]

    PopUp_EditBarang_textfield_namabarang = TextField()

    PopUp_EditBarang_textfield_harga = TextField(input_filter=NumbersOnlyInputFilter())

    PopUp_EditBarang_idBarang = TextField()

    PopUp_TambahBaru_textfield_namabarang = TextField(error_text="Nama barang tidak boleh kosong")

    PopUp_TambahBaru_textfield_harga = TextField(input_filter=NumbersOnlyInputFilter(), error_text="Harga tidak boleh kosong")

    def popUp_editbarang_check(e):
        """
        Fungsi ini akan dijalankan saat ada perubahan pada form edit barang
        """
        if PopUp_EditBarang_textfield_namabarang.value != "" and PopUp_EditBarang_textfield_harga.value != "":
            alertSimpanBarang[0].disabled = False
        else:
            alertSimpanBarang[0].disabled = True
        super_page.update()

    PopUp_EditBarang_textfield_namabarang.on_change = popUp_editbarang_check
    PopUp_EditBarang_textfield_harga.on_change = popUp_editbarang_check

    def popUp_tambahbaru_check(e):
        """
        Fungsi ini akan dijalankan saat ada perubahan pada form tambah barang baru
        """
        if PopUp_TambahBaru_textfield_namabarang.value != "" and PopUp_TambahBaru_textfield_harga.value != "":
            alertSimpanBarang[0].disabled = False
        else:
            alertSimpanBarang[0].disabled = True
        super_page.update()

    PopUp_TambahBaru_textfield_namabarang.on_change = popUp_tambahbaru_check
    PopUp_TambahBaru_textfield_harga.on_change = popUp_tambahbaru_check

    class UploadFile:
        """
        Class ini digunakan untuk membuat form upload file
        """
        def __init__(self):
            self.selected_files = Text()
            self.UploadFile_PhotoDummy = Image(
                src=IMGPATH / "dummy-order1.png",
                width=super_page.window_width / 100 * 10,
                height=super_page.window_width / 100 * 10,
                expand=True,
                # fit=ImageFit.NONE,
                # repeat=ImageRepeat.NO_REPEAT,
                border_radius=border_radius.all(8),
                # margin=margin.only(left=super_page.window_width/100 * 5)
                # left=super_page.window_width/100 * 5
            )
            self.pick_files_dialog = FilePicker(on_result=self.pick_files_result)

            super_page.overlay.append(self.pick_files_dialog)

            self.PopUp_UploadButton = Row(
                [
                    ElevatedButton(
                        "Upload Picture",
                        icon=icons.UPLOAD_FILE,
                        on_click=lambda _: self.pick_files_dialog.pick_files(
                            allow_multiple=False
                        ),
                    )
                ]
            )

        def pick_files_result(self, e):
            """
            Fungsi ini akan dijalankan saat file berhasil diupload dan mengembalikan hasil upload file
            """
            self.selected_files.value = (
                ", ".join(map(lambda f: f.name, e.files)) if e.files else "Cancelled!"
            )

            self.UploadFile_PhotoDummy.src = e.files[0].path
            super_page.update()

    class PopUp_EditBarang:
        """
        Class ini digunakan untuk membuat pop-up saat menekan tombol edit barang
        Memerlukan initial data barang yang akan diubah {nama, harga, id_kopi, foto}
        
        """
        def __init__(self, data):
            
            self.data = data
            self.PopUp_EditBarang_textfield_namabarang = TextField(
                value=self.data["nama"]
            )
            self.PopUp_EditBarang_textfield_harga = TextField(value=self.data["harga"])
            self.PopUp_EditBarang_idBarang = TextField(value=self.data["id_kopi"])
            self.initUpload = UploadFile()
            self.initUpload.UploadFile_PhotoDummy.src = (
                IMGPATH / "coffee" / self.data["foto"]
            )

        def changeData(self, nama, harga, id_kopi, img_path):
            """
            Fungsi ini akan mengubah data barang yang ada di database
            """
            findIndex = kopi_data[kopi_data["id_kopi"] == id_kopi].index[0]
            kopi_data.at[findIndex, "nama"] = nama
            kopi_data.at[findIndex, "harga"] = harga
            kopi_data.at[findIndex, "img_path"] = img_path
            # kopi_data.at[findIndex, "id_kopi"] = id_kopi

        def simpanBarang_clicked(self, e):
            """
            Fungsi ini akan dijalankan saat tombol simpan barang ditekan
            """
            nama = self.PopUp_EditBarang_textfield_namabarang.value
            harga = self.PopUp_EditBarang_textfield_harga.value
            id_kopi = self.PopUp_EditBarang_idBarang.value
            img = PILImage.open(self.initUpload.UploadFile_PhotoDummy.src)
            img_ext = self.initUpload.UploadFile_PhotoDummy.src.split(".")[-1]

            self.changeData(nama, harga, id_kopi, f"{id_kopi}.{img_ext}")

            img.save(IMGPATH / "coffee" / f"{self.data['id_kopi']}.{img_ext}")
            super_page.dialog.open = False
            # data_body.update()
            super_page.update()

        def batalSimpan_clicked(self, e):
            """
            Fungsi ini akan dijalankan saat tombol batal ditekan
            """
            super_page.dialog.open = False
            super_page.update()

        def EditBarang_PopUp(self, e):
            """
            Fungsi ini akan mengembalikan AlertDialog yang berisi form untuk mengubah barang
            """
            content = Container(
                width=super_page.window_width / 100 * 40,
                content=Column(
                    controls=[
                        Container(
                            content=Text(
                                "Edit ?",
                                weight=FontWeight.NORMAL,
                                size=12,
                                color=colors["blackAlpha/500"],
                            )
                        ),
                        Container(
                            content=Text(
                                "ID Barang",
                                weight=FontWeight.NORMAL,
                                size=16,
                                color=colors["Black"],
                            )
                        ),
                        Container(self.PopUp_EditBarang_idBarang),
                        Container(
                            content=Text(
                                "Nama Barang",
                                weight=FontWeight.NORMAL,
                                size=16,
                                color=colors["Black"],
                            )
                        ),
                        Container(content=self.PopUp_EditBarang_textfield_namabarang),
                        Container(
                            content=Text(
                                "Harga",
                                weight=FontWeight.NORMAL,
                                size=16,
                                color=colors["Black"],
                            )
                        ),
                        Container(content=self.PopUp_EditBarang_textfield_harga),
                        Container(
                            content=Text(
                                "Foto Item",
                                weight=FontWeight.NORMAL,
                                size=16,
                                color=colors["Black"],
                            )
                        ),
                        Container(
                            content=self.initUpload.UploadFile_PhotoDummy,
                            margin=margin.only(left=0),
                        ),
                        Container(content=self.initUpload.PopUp_UploadButton),
                        Container(content=self.initUpload.selected_files),
                    ]
                ),
            )

            alertSimpanBarang[0].on_click = self.simpanBarang_clicked
            alertSimpanBarang[1].on_click = self.batalSimpan_clicked

            return AlertDialog(
                modal=True,
                title=Text(f"Edit Barang {self.data['nama']}", weight="bold"),
                content=content,
                actions=alertSimpanBarang,
                actions_alignment=MainAxisAlignment.END,
            )

        def alert(self, e):
            """
            Fungsi ini akan menampilkan pop-up edit barang
            """
            card = self.EditBarang_PopUp(e)
            super_page.dialog = card
            card.open = True
            super_page.update()

    class PopUp_TambahBaru:
        """
        Class ini digunakan untuk membuat pop-up saat menekan tombol tambah barang baru
        """
        def __init__(self):
            self.initUpload = UploadFile()

        def simpanBarang_clicked(self, e):
            """
            Fungsi ini akan dijalankan saat tombol simpan barang ditekan
            
            Mengirim data barang baru ke database (id_kopi, nama, harga, foto, biaya_produksi)
            
            
            """
            id_kopi = int(kopi_data["id_kopi"].max()) + 1
            nama = PopUp_TambahBaru_textfield_namabarang.value
            harga = PopUp_TambahBaru_textfield_harga.value
            try:
                foto = self.initUpload.UploadFile_PhotoDummy.src.split("\\")[-1]
                imgfrom = self.initUpload.UploadFile_PhotoDummy.src
                saveImage=True
            except:
                foto = "dummy-order1.png"
                saveImage=False
                imgfrom = None
                # imgfrom = IMGPATH / "dummy-order1.png"
            biaya_produksi = 0
            listofData = {
                "id_kopi": id_kopi,
                "nama": nama,
                "harga": harga,
                "foto": f"{foto}",
                "biaya_produksi": biaya_produksi,
            }

            addKopiData(listofData=listofData, df=kopi_data, PATH=DATAPATH, saveImage=saveImage, imgfrom=imgfrom, imgto=IMGPATH / "coffee")
            super_page.dialog.open = False
            super_page.update()

        def batalSimpan_clicked(self, e):
            """
            Fungsi ini akan dijalankan saat tombol batal ditekan
            """
            super_page.dialog.open = False
            super_page.update()

        def TambahBarang_PopUp(self, e):
            """
            Fungsi ini akan mengembalikan AlertDialog yang berisi form untuk menambahkan barang baru
            """
            # initUpload = UploadFile()
            content = Container(
                width=super_page.window_width / 100 * 40,
                content=Column(
                    controls=[
                        Container(
                            content=Text(
                                "Isi data barang di bawah",
                                weight=FontWeight.NORMAL,
                                size=12,
                                color=colors["blackAlpha/500"],
                            )
                        ),
                        Container(
                            content=Text(
                                "Nama Barang",
                                weight=FontWeight.NORMAL,
                                size=16,
                                color=colors["Black"],
                            )
                        ),
                        PopUp_TambahBaru_textfield_namabarang,
                        Container(
                            content=Text(
                                "Harga",
                                weight=FontWeight.NORMAL,
                                size=16,
                                color=colors["Black"],
                            )
                        ),
                        PopUp_TambahBaru_textfield_harga,
                        Container(
                            content=Text(
                                "Foto Item",
                                weight=FontWeight.NORMAL,
                                size=16,
                                color=colors["Black"],
                            )
                        ),
                        Container(
                            self.initUpload.UploadFile_PhotoDummy,
                            margin=margin.only(left=0),
                        ),
                        Container(content=self.initUpload.PopUp_UploadButton),
                        Container(content=self.initUpload.selected_files),
                        # PopUp_UploadButton,
                        # selected_files,
                    ]
                ),
            )

            alertSimpanBarang[0].on_click = self.simpanBarang_clicked
            alertSimpanBarang[1].on_click = self.batalSimpan_clicked

            return AlertDialog(
                modal=True,
                title=Text("Tambah Barang Baru", weight="bold"),
                content=content,
                actions=alertSimpanBarang,
                actions_alignment=MainAxisAlignment.END,
            )

        def alert(self, e):
            """
            Fungsi ini akan menampilkan pop-up tambah barang baru
            """
            card = self.TambahBarang_PopUp(e)
            super_page.dialog = card
            card.open = True
            super_page.update()

    barang_baru_button.on_click = PopUp_TambahBaru().alert

    def changeCurrency(harga):
        """
        Fungsi ini akan mengubah harga menjadi format mata uang rupiah
        Contoh: 1000000 -> 1.000.000,00
        """
        str_harga = ""
        harga = str(harga)
        try:
            harga_lebih = harga.split(".")[1]
            harga = harga.split(".")[0]
            start_ = len(harga) % 3 if len(harga) % 3 != 0 else 3
            str_harga += harga[:start_] + "."
            harga = harga[start_:]
            while len(harga):
                if len(harga) >= 3:
                    str_harga += harga[:3] + "."
                    harga = harga[3:]
                else:
                    str_harga += harga
                    harga = ""
            if str_harga[-1] == ".":
                str_harga = str_harga[:-1]
            return str_harga + "," + harga_lebih[:2]
        except:
            start_ = len(harga) % 3 if len(harga) % 3 != 0 else 3
            str_harga += harga[:start_] + "."
            harga = harga[start_:]
            while len(harga):
                if len(harga) >= 3:
                    str_harga += harga[:3] + "."
                    harga = harga[3:]
                else:
                    str_harga += harga
                    harga = ""
            if str_harga[-1] == ".":
                str_harga = str_harga[:-1]
            return str_harga

    def get_items(N: int = 10, window_width=750, window_height=600):
        """
        Fungsi ini mengembalikan list item yang akan ditampilkan pada halaman stok dan produk (default 10 item)
        
        N (int) : jumlah item yang akan ditampilkan
        window_width (int) : lebar window (layar)
        window_height (int) : tinggi window (layar)
        """
        items_list = []
        joinedData = getJoinedStokKopi(stok_data, kopi_data)
        for key, value in kopi_data.iterrows():
            # print(i)
            # kopi_now = kopi_data[kopi_data["id_kopi"] == value["id_kopi"]]
            stok = joinedData[joinedData["id_kopi"] == value["id_kopi"]]["stok"].sum()
            # print(stok)
            nama = value["nama"]
            harga = value["harga"]

            temp = PopUp_EditBarang(value)

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
                            MaterialState.FOCUSED: RoundedRectangleBorder(radius=2),
                            MaterialState.HOVERED: RoundedRectangleBorder(radius=8),
                            MaterialState.DEFAULT: RoundedRectangleBorder(radius=2),
                        }
                    ),
                ),
            )

            items_list.append(
                Container(
                    width=window_width / 2 * 0.8,
                    height=window_height / 4.8,
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
                                                src=IMGPATH / "coffee" / value["foto"]
                                            ),
                                            border_radius=border_radius.all(8),
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
                                # was here
                                tambah_button,
                            ]
                        ),
                    ),
                ),
            )

        return items_list

    def get_manajemen_stok(N: int = 10, window_width=750, window_height=600):
        """
        Fungsi ini mengembalikan list item yang akan ditampilkan pada halaman manajemen stok (default 10 item)

        N (int) : jumlah item yang akan ditampilkan
        window_width (int) : lebar window (layar)
        window_height (int) : tinggi window (layar)
        """
        # items_list = []
        isi_column = []
        joinedData = getJoinedStokKopi(stok_data, kopi_data)
        for key, value in joinedData.iterrows():
            # print(value)
            if key + 1 == N:
                break
            icon_cells = [IconButton(icon=icons.DELETE), IconButton(icon=icons.EDIT)]
            isi_column.append(
                DataRow(
                    cells=[
                        DataCell(Text(str(key + 1))),  # No
                        DataCell(Text(value["nama"].capitalize())),  # Barang
                        DataCell(Text(changeCurrency(value["stok"]))),  # Jumlah
                        DataCell(Text(str("status"))),  # Status
                        DataCell(Text(str(value["tanggal_exp"]))),  # Tanggal Expired
                        DataCell(
                            Row(controls=icon_cells, alignment=alignment.top_center)
                        ),  # action button
                    ],
                    
                )
            )
        return isi_column

    data_body = Container(
        width=super_page.window_width / 100 * 90,
        height=super_page.window_height * 90 / 100
        - (super_page.window_height * 35 / 100),
        border_radius=10,
        content=Row(
            # spacing=40,  # kesamping
            run_spacing=super_page.window_height / 100 * 1,  # kebawah
            alignment=MainAxisAlignment.START,
            wrap=True,
            scroll=ScrollMode.AUTO,
            controls=[
                *get_items(
                    super_page.window_width / 100 * 40,
                    super_page.window_height - 150,
                ),
            ],
        ),
    )

    def ManageBarang_clicked(e):
        """
        Fungsi ini akan dijalankan saat tombol Manajemen Barang ditekan
        """
        jenis_stok_button[0].style = style_selected_round0
        jenis_stok_button[0].disabled = True
        jenis_stok_button[1].style = style_selectable_round0
        jenis_stok_button[1].disabled = False
        data_body.content = Row(
            # spacing=40,  # kesamping
            run_spacing=super_page.window_height / 100 * 1,  # kebawah
            alignment=MainAxisAlignment.START,
            wrap=True,
            scroll=ScrollMode.AUTO,
            controls=[
                *get_items(
                    super_page.window_width / 100 * 40,
                    super_page.window_height - 150,
                ),
            ],
        )
        super_page.update()

    def ManageStok_clicked(e):
        """
        Fungsi ini akan dijalankan saat tombol Manajemen Stok ditekan
        """
        jenis_stok_button[0].style = style_selectable_round0
        jenis_stok_button[0].disabled = False
        jenis_stok_button[1].style = style_selected_round0
        jenis_stok_button[1].disabled = True
        data_body.content = Column(
            controls=[
                DataTable(
                    width=super_page.window_width / 100 * 90,
                    columns=[
                        DataColumn(
                            Text(
                                "No",
                                size=12,
                                width=super_page.window_width / 100 * 8,
                            # color=colors["Gray/400"],
                            ),
                        ),
                        DataColumn(
                            Text(
                                "Barang",
                                size=12,
                                # width=super_page.window_width / 100 * 40 / 100 * 20,
                            ),
                            # color=colors["Gray/400"],
                        ),
                        DataColumn(
                            Text(
                                "Jumlah",
                                size=12,
                                # width=super_page.window_width / 100 * 40 / 100 * 8,
                            ),
                            # color=colors["Gray/400"],
                        ),
                        DataColumn(
                            Text(
                                "Status",
                                size=12,
                                # width=super_page.window_width / 100 * 40 / 100 * 8,
                            ),
                            # color=colors["Gray/400"],
                        ),
                        DataColumn(
                            Text(
                                "Tanggal Exp",
                                size=12,
                                # width=super_page.window_width / 100 * 40 / 100 * 12,
                            ),
                            # color=colors["Gray/400"],
                        ),
                        DataColumn(
                            Text(
                                "Aksi",
                                size=12,
                                # width=super_page.window_width / 100 * 40 / 100 * 8,
                                # color=colors["Gray/400"],
                            )
                        ),
                    ],
                    rows=[*get_manajemen_stok(10)],
                )
            ]
        )

        super_page.update()

    jenis_stok_button[0].on_click = ManageBarang_clicked
    jenis_stok_button[1].on_click = ManageStok_clicked

    body = Container(
        content=Container(
            content=Column(
                controls=[
                    Text(
                        "Stok dan Produk",
                        weight=FontWeight.BOLD,
                        size=24,
                        color=colors["Black"],
                    ),
                    Row(controls=jenis_stok_button, spacing=0),
                    Row(
                        controls=[barang_baru_button, Row(controls=pencarian_field)],
                        alignment=MainAxisAlignment.SPACE_BETWEEN,
                    ),
                    data_body,
                ],
                spacing=super_page.window_height / 100 * 2,
            ),
            bgcolor="White",
            padding=padding.only(
                left=super_page.window_width / 100 * 1,
                top=super_page.window_height / 100 * 2,
                right=super_page.window_width / 100 * 1,
            ),
        ),
        bgcolor=colors["Gray/50"],
        width=super_page.window_width,
        height=super_page.window_height - 150,
        padding=padding.only(
            top=super_page.window_height / 100 * 2,
            left=super_page.window_width / 100 * 5,
            right=super_page.window_width / 100 * 5,
        ),
    )

    view.controls.append(body)
