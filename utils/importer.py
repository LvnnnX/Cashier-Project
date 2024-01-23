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
    
def loadNotaDetailbyIdNotaPrimary(NotaPrimaryId:str,date:datetime.datetime,path=DATAPATH):
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