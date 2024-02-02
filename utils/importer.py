from utils.libs import *
from utils.converter import *
def load_colors(Path=JSONPATH) -> dict:
    f = open(f"{Path}/bgcolors.json")
    colors = json.load(f)
    return colors

def loadNotaHeaderByTime(filter:str,date:datetime.datetime,Path=DATAPATH):
    Year=date.strftime("%Y")
    Month=HASHMONTH[int(date.strftime("%m"))-1]
    Day=date.strftime("%d")
    if not os.path.exists(DATAPATH / "Nota" / Year / Month / "nota_header.csv"):
        print("nota_header path don't exist")
    detail=pd.read_csv(DATAPATH / "Nota" / Year / Month / "nota_header.csv")
    return detail
    
def loadNotaDetailAmbilbyIdNota(NotaPrimaryId,date:datetime.datetime,path=DATAPATH):
    Year=date.strftime("%Y")
    Month=HASHMONTH[int(date.strftime("%m"))-1]
    Day=date.strftime("%d")
    if not os.path.exists(DATAPATH / "Nota" / Year / Month / "nota_detail_ambil.csv"):
        print("nota_detail path don't exist")
    header=pd.read_csv(DATAPATH / "Nota" / Year / Month / "nota_detail_ambil.csv")
    NotaDetail=header.loc[header["id_nota"]==NotaPrimaryId]
    return NotaDetail

def loadNotaDetailPulangbyIdNota(NotaPrimaryId,date:datetime.datetime,path=DATAPATH):
    Year=date.strftime("%Y")
    Month=HASHMONTH[int(date.strftime("%m"))-1]
    Day=date.strftime("%d")
    if not os.path.exists(DATAPATH / "Nota" / Year / Month / "nota_detail_pulang.csv"):
        print("nota_detail path don't exist")
    header=pd.read_csv(DATAPATH / "Nota" / Year / Month / "nota_detail_pulang.csv")
    NotaDetail=header.loc[header["id_nota"]==NotaPrimaryId]
    return NotaDetail
    
def getSalesBySalesId(SalesId:str,path=DATAPATH):
    salesCsv=pd.read_csv(DATAPATH / "Employee" / "sales.csv")
    sales=salesCsv.loc[salesCsv["id_sales"]==SalesId]
    return sales

def getKaryawanByIdKaryawan(IdKaryawan,path=DATAPATH):
    karyawanCsv=pd.read_csv(DATAPATH / "Employee" / "karyawan.csv")
    karyawan=karyawanCsv.loc[karyawanCsv["id_karyawan"]==IdKaryawan]
    return karyawan

def getStokById(IdStok):
    stokCsv=pd.read_csv(DATAPATH / "Coffee" / "stok.csv")
    stok=stokCsv.loc[stokCsv["id_stok"]==IdStok]
    return stok

def getKopiById(IdKopi):
    kopiCsv=pd.read_csv(DATAPATH / "Coffee" / "kopi.csv")
    kopi=kopiCsv.loc[kopiCsv["id_kopi"]==IdKopi]
    return kopi

def getAndJoinStokById(dataFrame:pd.DataFrame):
    dataFrame.astype({"id_stok":'str'})
    df=dataFrame.set_index("id_stok")
    stokCsv=pd.read_csv(DATAPATH / "Coffee" / "stok.csv")
    stokCsv.astype({"id_stok":'str'})
    stokCsv.set_index("id_stok",inplace=True)
    stok=df.join(stokCsv,how='inner',rsuffix="_stok")
    return stok.reset_index()

def getAndJoinKopiById(dataFrame:pd.DataFrame):
    df=dataFrame.set_index("id_kopi")
    kopiCsv=pd.read_csv(DATAPATH / "Coffee" / "kopi.csv")
    kopiCsv.set_index("id_kopi",inplace=True)
    kopi=df.join(kopiCsv,how='inner',rsuffix="_kopi")
    return kopi.reset_index()

def getAndJoinSalesById(dataFrame:pd.DataFrame):
    df=dataFrame.set_index("id_sales")
    salesCsv=pd.read_csv(DATAPATH / "Employee" / "sales.csv")
    salesCsv.set_index("id_sales",inplace=True)
    sales=df.join(salesCsv,how='inner',rsuffix="_sales")
    return sales.reset_index()

def getAndJoinTokoById(dataFrame:pd.DataFrame):
    df=dataFrame.set_index("id_toko")
    tokoCsv=pd.read_csv(DATAPATH / "Toko" / "toko.csv")
    tokoCsv.set_index("id_toko",inplace=True)
    toko=df.join(tokoCsv,how='inner',rsuffix="_toko")
    return toko.reset_index()


def getIdTokoByName(nama:str):
    tokoCsv=pd.read_csv(DATAPATH / "Toko" / "toko.csv")
    tokoCsv.set_index("nama",inplace=True)
    id_toko=tokoCsv.T[nama]["id_toko"]
    return id_toko

def getIdKopiByName(nama:str):
    kopiCsv=pd.read_csv(DATAPATH / "Coffee" / "kopi.csv")
    kopiCsv.set_index("nama",inplace=True)
    id_kopi=kopiCsv.T[nama]["id_kopi"]
    return id_kopi

def getSeriesIdAndNamaSales():
    df=pd.read_csv(DATAPATH / "Employee" / "sales.csv")
    uniqueSalesName=df[["id_sales","nama"]]
    return uniqueSalesName

def getSeriesIdAndNamaKopi():
    df=pd.read_csv(DATAPATH / "Coffee" / "kopi.csv")
    uniqueBarangName=df[["id_kopi","nama"]]
    return uniqueBarangName

def getSeriesIdAndNamaToko():
    df=pd.read_csv(DATAPATH / "toko" / "toko.csv")
    uniqueTokoName=df[["id_toko","nama"]]
    return uniqueTokoName

def get_screen_size():
    monitor = get_monitors()[0]
    return monitor.width, monitor.height

#(id_nota,status)
def updateNotaHeaderStatusById(listOfQuery,date:datetime.datetime):
    Year=date.strftime("%Y")
    Month=HASHMONTH[int(date.strftime("%m"))-1]
    Day=date.strftime("%d")
    headerCsv=pd.read_csv(DATAPATH / "Nota" / Year / Month / "nota_header.csv")
    for i in listOfQuery:
        headerCsv.loc[headerCsv["id_nota"]==i[0],"status_nota"]=i[1]
    headerCsv.reset_index(drop=True,inplace=True)
    headerCsv.to_csv(DATAPATH / "Nota" / Year / Month / "nota_header.csv",index=False)


#(id_nota_detail,stok,harga_satuan) listQueryInput
def updateNotaDetailAmbilByIdMultiple(listOfQuery,date:datetime.datetime):
    Year=date.strftime("%Y")
    Month=HASHMONTH[int(date.strftime("%m"))-1]
    Day=date.strftime("%d")
    ambilCsv=pd.read_csv(DATAPATH / "Nota" / Year / Month / "nota_detail_pulang.csv").set_index("id_nota_detail")
    for i in listOfQuery:
        ambilCsv["harga_satuan"][i[0]]=i[2]
        ambilCsv["stok"][i[0]]=i[1]
    ambilCsv.reset_index(inplace=True)
    ambilCsv.to_csv(DATAPATH / "Nota" / Year / Month / "nota_detail_pulang.csv",index=False)


#(id_stok,stok) listQueryInput
#id_stok,stok
def updateStokAvailableByIdMultiple(listOfQuery,date:datetime.datetime):
    stokCsv=pd.read_csv(DATAPATH / "Coffee" / "stok.csv").set_index("id_stok")
    for i in listOfQuery:
        stokCsv["stok"][i[0]]=i[1]+stokCsv["stok"][i[0]]
    stokCsv.reset_index(inplace=True)
    stokCsv.to_csv(DATAPATH / "Coffee" / "stok.csv",index=False)


#(id_nota_detail,id_nota,id_stok,qty,disc,harga_satuan,id_toko)
def addNotaDetailPulang(listOfQuery,date:datetime.datetime):
    Year=date.strftime("%Y")
    Month=HASHMONTH[int(date.strftime("%m"))-1]
    Day=date.strftime("%d")
    PulangCsv=pd.read_csv(DATAPATH / "Nota" / Year / Month / "nota_detail_pulang.csv")
    # PulangCsv["id_nota_detail"].astype('str')
    for i in listOfQuery:
        row={
            "id_nota_detail":i[0],
            "id_nota":i[1],
            "id_stok":i[2],
            "qty":i[3],
            "disc":i[4],
            "harga_satuan":i[5],
            "id_toko":i[6]
        }
        PulangCsv.loc[len(PulangCsv)]=row
    PulangCsv.reset_index(drop=True,inplace=True)
    PulangCsv.to_csv(DATAPATH / "Nota" / Year / Month / "nota_detail_pulang.csv",index=False)

#id_nota,total,status_nota,id_karyawan,jenis_transaksi,namapelanngan,id_sales,tanggal
def addNotaHeader(listQuery,date:datetime.datetime):
    Year=date.strftime("%Y")
    Month=HASHMONTH[int(date.strftime("%m"))-1]
    Day=date.strftime("%d")
    headerCsv=pd.read_csv(DATAPATH / "Nota" / Year / Month / "nota_header.csv")
    for i in listQuery:
        row={
            "id_nota":i[0],
            "total":i[1],
            "status_nota":i[2],
            "id_karyawan":i[3],
            "jenis_transaksi":i[4],
            "namapelangan":i[5],
            "id_sales":i[6],
            "tanggal":i[7].strftime("%d/%m/%Y %H:%M")
        }
        headerCsv.loc[len(headerCsv)]=row
    headerCsv.reset_index(drop=True,inplace=True)
    headerCsv.to_csv(DATAPATH / "Nota" / Year / Month / "nota_header.csv",index=False)


def updateDetailNotaPulangIdStok(listOfQuery,date:datetime.datetime):
    Year=date.strftime("%Y")
    Month=HASHMONTH[int(date.strftime("%m"))-1]
    Day=date.strftime("%d")
    pulangCsv=pd.read_csv(DATAPATH / "Nota" / Year / Month / "nota_detail_pulang.csv")
    for i in listOfQuery:
        temp=pulangCsv.loc[pulangCsv["id_nota_detail"]==i[0]]
        temp["id_stok"]=i[1]
        temp["harga_satuan"]=i[2]
        temp["id_toko"]=i[3]
        pulangCsv.loc[pulangCsv["id_nota_detail"]==i[0]]=temp
    pulangCsv.to_csv(DATAPATH / "Nota" / Year / Month / "nota_detail_pulang.csv",index=False)

def getLatestStokIdByKopiId(IdKopi):
    stokCsv=pd.read_csv(DATAPATH / "Coffee" / "stok.csv")
    stokFilteredSort=stokCsv.loc[stokCsv["id_kopi"]==int(IdKopi)].sort_values(by="tanggal_exp", ascending=False).reset_index()
    return stokFilteredSort["id_kopi"][0]

def createListofUUID(ranges):
    listOfId=[ uuid.uuid4().hex for _ in range(ranges)]
    return listOfId