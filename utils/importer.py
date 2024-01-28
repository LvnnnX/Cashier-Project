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
    
def loadNotaDetailbyIdNotaPrimary(NotaPrimaryId,date:datetime.datetime,path=DATAPATH):
    Year=date.strftime("%Y")
    Month=HASHMONTH[int(date.strftime("%m"))-1]
    Day=date.strftime("%d")
    if not os.path.exists(DATAPATH / "Nota" / Year / Month / "nota_detail.csv"):
        print("nota_detail path don't exist")
    header=pd.read_csv(DATAPATH / "Nota" / Year / Month / "nota_detail.csv")
    NotaDetail=header.loc[header["id_nota_primary"]==NotaPrimaryId]
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
    df=dataFrame.set_index("id_stok")
    stokCsv=pd.read_csv(DATAPATH / "Coffee" / "stok.csv")
    stokCsv.set_index("id_stok",inplace=True)
    stok=df.join(stokCsv,how='inner')
    return stok.reset_index()

def getAndJoinKopiById(dataFrame:pd.DataFrame):
    df=dataFrame.set_index("id_kopi")
    kopiCsv=pd.read_csv(DATAPATH / "Coffee" / "kopi.csv")
    kopiCsv.set_index("id_kopi",inplace=True)
    kopi=df.join(kopiCsv,how='inner')
    return kopi.reset_index()

def getAndJoinSalesById(dataFrame:pd.DataFrame):
    df=dataFrame.set_index("id_sales")
    salesCsv=pd.read_csv(DATAPATH / "Employee" / "sales.csv")
    salesCsv.set_index("id_sales",inplace=True)
    sales=df.join(salesCsv,how='inner')
    return sales.reset_index()

def getUniqueSalesName():
    df=pd.read_csv(DATAPATH / "Employee" / "sales.csv")
    uniqueSalesName=df["nama"].unique()
    return uniqueSalesName

def getUniqueBarangName():
    df=pd.read_csv(DATAPATH / "Coffee" / "kopi.csv")
    uniqueBarangName=df["nama"].unique()
    return uniqueBarangName

def getUniqueTokoName():
    df=pd.read_csv(DATAPATH / "toko" / "toko.csv")
    uniqueTokoName=df["nama"].unique()
    return uniqueTokoName

def get_screen_size():
    monitor = get_monitors()[0]
    return monitor.width, monitor.height
