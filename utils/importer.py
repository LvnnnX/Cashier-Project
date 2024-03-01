from utils.libs import *
from utils.converter import *

def load_colors(Path=JSONPATH) -> dict:
    f = open(f"{Path}/bgcolors.json")
    colors = json.load(f)
    return colors

#very computationaly heavy
def loadNotaHeaderByTime(date:datetime.datetime,daysBehind,Path=DATAPATH):
    timeStart=date+relativedelta(days=-daysBehind)
    Year=timeStart.strftime("%Y")
    Month=HASHMONTH[int(timeStart.strftime("%m"))-1]
    Day=timeStart.strftime("%d")
    monthDifference=date.month-timeStart.month+(date.year-timeStart.year)*12
    if not os.path.exists(DATAPATH / "Nota" / Year / Month / "nota_header.csv"):
        while (0<monthDifference) and (not os.path.exists(DATAPATH / "Nota" / Year / Month / "nota_header.csv")):
            Year=timeStart.strftime("%Y")
            Month=HASHMONTH[int(timeStart.strftime("%m"))-1]
            timeStart=timeStart+relativedelta(months=1)
            monthDifference-=1
        Year=timeStart.strftime("%Y")
        Month=HASHMONTH[int(timeStart.strftime("%m"))-1]
        if not os.path.exists(DATAPATH / "Nota" / Year / Month / "nota_header.csv"):
            print("nota_header path don't exist")
            return None
        mainDF=pd.read_csv(DATAPATH / "Nota" / Year / Month / "nota_header.csv")
    else:
        mainDF=pd.read_csv(DATAPATH / "Nota" / Year / Month / "nota_header.csv")
        timestamp=[]
        for i in mainDF["tanggal"]:
            timestamp.append(datetime.datetime.strptime(i,"%d/%m/%Y %H:%M").timestamp())
        timestamp=pd.Series(timestamp)
        mainDF=mainDF.loc[timestamp>=timeStart.timestamp()]
    for i in range(1,monthDifference+1):
        timeitter=timeStart+relativedelta(months=i)
        Year=timeitter.strftime("%Y")
        Month=HASHMONTH[int(timeitter.strftime("%m"))-1]
        Day=timeitter.strftime("%d")
        if not os.path.exists(DATAPATH / "Nota" / Year / Month / "nota_header.csv"):
            print("nota_header path don't exist")
        else:
            detail=pd.read_csv(DATAPATH / "Nota" / Year / Month / "nota_header.csv")
            mainDF=pd.concat([mainDF,detail])
    return mainDF

    
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

def getTokoById(Idtoko):
    tokoCsv=pd.read_csv(DATAPATH / "Toko" / "toko.csv")
    toko=tokoCsv.loc[tokoCsv["id_toko"]==Idtoko]
    return toko

def getAmbilById(idAmbil,date:datetime.datetime):
    Year=date.strftime("%Y")
    Month=HASHMONTH[int(date.strftime("%m"))-1]
    Day=date.strftime("%d")
    ambilCsv=pd.read_csv(DATAPATH / "Coffee" / Year / Month / "ambil.csv")  
    ambil=ambilCsv.loc[ambilCsv["id_ambil"]==idAmbil]
    # stringStrip='%d/%m/%Y %H:%M'
    # ambil["tanggal_stok"]=ambil["tanggal_stok"].apply(lambda x : datetime.datetime.strptime(x,stringStrip))
    return ambil.reset_index()

def getAndJoinStokById(dataFrame:pd.DataFrame):
    dataFrame.astype({"id_stok":'str'})
    df=dataFrame.set_index("id_stok")
    stokCsv=pd.read_csv(DATAPATH / "Coffee" / "stok.csv")
    stokCsv.astype({"id_stok":'str'})
    stokCsv.set_index("id_stok",inplace=True)
    stok=df.join(stokCsv,how='inner',rsuffix="_stok")
    return stok.reset_index()

#listStokQuery(id_ambil,id_stok,tanggal,rowStok)
#listOfQuery(id_stok,stok)
def getPossibleStokResolver(idKopi,jumlahPesanan,listOfQuery:list):
    listOfQueryCopy=listOfQuery.copy()
    timeNow=datetime.datetime.now()
    monthStart=datetime.datetime(2024,1,1)
    diference=relativedelta(timeNow,monthStart).months
    length_month=min(18,diference)
    monthIterate=timeNow+relativedelta(months=-length_month)
    Year=monthIterate.strftime("%Y")
    Month=HASHMONTH[int(monthIterate.strftime("%m"))-1]
    bulan=monthIterate
    pastStok=pd.read_csv(DATAPATH / "Coffee" / Year / Month / "stok.csv")
    pastStok=pastStok.loc[pastStok["id_kopi"].astype(str)==str(idKopi)]  
    #berat banget di komputasi mungkin perlu di adjust
    #karena aku pengen buat kode nya ku run pas selesai jadi aku perlu nge redo perubahan yang terjadi sebelum kodenya jalan
    #listOfQuery itu query perubahaan yang terjadi sebelumnya
    removeList=[]
    for z in listOfQueryCopy:
        if len(pastStok.loc[pastStok["id_stok"]==z[0]])>0:
            pastStok.loc[pastStok["id_stok"]==z[0],"stok"]=pastStok.loc[pastStok["id_stok"]==z[0],"stok"]+z[1]
            removeList.append(z)
    for k in removeList:
        listOfQueryCopy.remove(k)
    #filtered 0 stok
    pastStok=pastStok.loc[pastStok["stok"]>0]
    stok=pastStok.groupby('id_kopi')["stok"].transform(pd.Series.cumsum)
    pastStok["tanggal"]=bulan
    pastStok["stok_cum"]=stok
    #nge buat query untuk neglakuin add data ambil dan stok biar tanggal dan etc bener
    removeList.clear()
    if len(pastStok.loc[pastStok["stok_cum"]>=jumlahPesanan])>0:
        minValue=pastStok.loc[pastStok["stok_cum"]>=jumlahPesanan,"stok_cum"].min()
        returnedRows=pastStok.loc[pastStok["stok_cum"]<=minValue].drop(["stok_cum"],axis=1)
        pastStok.sort_values("tanggal_exp",inplace=True)
        queryOfChange=[]
        for index,row in returnedRows.iterrows():
            if jumlahPesanan-row["stok"]>0:
                jumlahPesanan=jumlahPesanan-row["stok"]
                rowStok=row["stok"]
                queryOfChange.append((row["id_stok"],row["tanggal"],rowStok))
            else:
                rowStok=jumlahPesanan
                queryOfChange.append((row["id_stok"],row["tanggal"],rowStok))
                return queryOfChange
    for i in range(length_month-1,-1,-1):
        monthIterate=timeNow+relativedelta(months=-i)
        Year=monthIterate.strftime("%Y")
        Month=HASHMONTH[int(monthIterate.strftime("%m"))-1]
        bulan=monthIterate
        stokCsv=pd.read_csv(DATAPATH / "Coffee" / Year / Month / "stok.csv") 
        stokCsv=stokCsv.loc[stokCsv["id_kopi"]==idKopi]
        #berat banget di komputasi mungkin perlu di adjust
        for z in listOfQueryCopy:
            if len(stokCsv.loc[stokCsv["id_stok"]==z[0]])>0:
                stokCsv.loc[stokCsv["id_stok"]==z[0],"stok"]=stokCsv.loc[stokCsv["id_stok"]==z[0],"stok"]+z[1]

                removeList.append(z)
        for k in removeList:
            listOfQueryCopy.remove(k)
        removeList.clear()
        #filtered 0 stok
        stokCsv=stokCsv.loc[stokCsv["stok"]>0]  
        stokCsv["tanggal"]=bulan
        stokCsv["stok_cum"]=0
        pastStok=pd.concat([pastStok,stokCsv])
        stok=pastStok.groupby('id_stok')["stok"].transform(pd.Series.cumsum)  
        pastStok["stok_cum"]=stok 
        if len(pastStok.loc[pastStok["stok_cum"]>=jumlahPesanan])>0:
            returnedRows=pastStok.loc[pastStok["stok_cum"]>=jumlahPesanan].drop(["stok_cum"],axis=1)
            queryOfChange=[]
            pastStok.sort_values("tanggal_exp",inplace=True)
            for index,row in returnedRows.iterrows():
                if jumlahPesanan-row["stok"]>0:
                    jumlahPesanan=jumlahPesanan-row["stok"]
                    rowStok=row["stok"]
                    queryOfChange.append((row["id_stok"],row["tanggal"],rowStok))
                else:
                    rowStok=jumlahPesanan
                    queryOfChange.append((row["id_stok"],row["tanggal"],rowStok))
                    return queryOfChange
    return []
    


def getAndJoinSalesById(dataFrame:pd.DataFrame):
    df=dataFrame.set_index("id_sales")
    salesCsv=pd.read_csv(DATAPATH / "Employee" / "sales.csv")
    salesCsv.set_index("id_sales",inplace=True)
    sales=df.join(salesCsv,how='inner',rsuffix="_sales")
    return sales.reset_index()

def getAndJoinTokoById(dataFrame:pd.DataFrame):
    dataFrame["id_toko"]=dataFrame["id_toko"].astype(str)
    df=dataFrame.set_index("id_toko")
    tokoCsv=pd.read_csv(DATAPATH / "Toko" / "toko.csv")
    tokoCsv["id_toko"]=tokoCsv["id_toko"].astype(str)
    tokoCsv.set_index("id_toko",inplace=True)
    toko=df.join(tokoCsv,how='inner',rsuffix="_toko")
    return toko.reset_index()

def getAndJoinAmbilById(dataFrame:pd.DataFrame,date:datetime.datetime):
    Year=date.strftime("%Y")
    Month=HASHMONTH[int(date.strftime("%m"))-1]
    Day=date.strftime("%d")
    dataFrame["id_ambil"]=dataFrame["id_ambil"].astype(str)
    ambilCsv=pd.read_csv(DATAPATH/ "Coffee" / Year / Month / "ambil.csv")
    ambilCsv["id_ambil"]=ambilCsv["id_ambil"].astype(str)
    ambil=pd.merge(ambilCsv,dataFrame,right_on="id_ambil",left_on="id_ambil",how='inner',suffixes=("_ambil","_detail"))
    return ambil.reset_index()


def getIdTokoByName(nama:str):
    tokoCsv=pd.read_csv(DATAPATH / "Toko" / "toko.csv")
    tokoCsv.set_index("nama",inplace=True)
    id_toko=tokoCsv.T[nama]["id_toko"]
    return id_toko




# listStokQuery([[id_ambil,id_stok,tanggal,rowStok],[...]...])
def removeAndAddAmbil(listOfQuery, date: datetime.datetime):
    Year = date.strftime("%Y")
    Month = HASHMONTH[int(date.strftime("%m")) - 1]
    Day = date.strftime("%d")
    ambilCsv = pd.read_csv(DATAPATH / "Coffee" / Year / Month / "ambil.csv")
    changeCsv = ambilCsv
    for singleQuery in listOfQuery:
        changeCsv = changeCsv.loc[changeCsv["id_ambil"] != singleQuery[0][0]]
        for k in singleQuery:
            changeCsv.loc[len(changeCsv)] = {
                "id_ambil": k[0],
                "id_stok": k[1],
                "tanggal_stok": k[2].strftime("%d/%m/%Y %H:%M"),
                "jumlah": float(k[3]),
            }
    changeCsv.to_csv(DATAPATH / "Coffee" / Year / Month / "ambil.csv", index=False)


def getAndJoinKopiById(dataFrame: pd.DataFrame):
    dataFrame["id_kopi"] = dataFrame["id_kopi"].astype(str)
    df = dataFrame.set_index("id_kopi")
    kopiCsv = pd.read_csv(DATAPATH / "Coffee" / "kopi.csv")
    kopiCsv["id_kopi"] = kopiCsv["id_kopi"].astype(str)
    kopiCsv.set_index("id_kopi", inplace=True)
    kopi = df.join(kopiCsv, how="inner", rsuffix="_kopi")
    return kopi.reset_index()


def getFullStok(date: datetime.datetime):
    Year = date.strftime("%Y")
    Month = HASHMONTH[int(date.strftime("%m")) - 1]
    Day = date.strftime("%d")
    stokCsv = pd.read_csv(DATAPATH / "Coffee" / Year / Month / "stok.csv")
    return stokCsv

def getJoinedStokKopi(df1:pd.DataFrame,df2:pd.DataFrame):
    # df1 = df1[['id_kopi', 'stok']]
    # df2 = df2[['id_kopi', 'nama']]
    # df1["id_kopi"] = df1["id_kopi"].astype(str)
    # df2["id_kopi"] = df2["id_kopi"].astype(str)
    df1 = df1.copy()
    df2 = df2.copy()
    df1.set_index("id_kopi",inplace=True)
    df2.set_index("id_kopi",inplace=True)
    joined = df1.join(df2,how="inner",rsuffix="_kopi")
    return joined.reset_index()


def getIdKopiByName(nama: str):
    kopiCsv = pd.read_csv(DATAPATH / "Coffee" / "kopi.csv")
    kopiCsv.set_index("nama", inplace=True)
    id_kopi = kopiCsv.T[nama]["id_kopi"]
    return id_kopi


def getSeriesIdAndNamaSales():
    df = pd.read_csv(DATAPATH / "Employee" / "sales.csv")
    uniqueSalesName = df[["id_sales", "nama"]]
    return uniqueSalesName


def getSeriesIdAndNamaKopi():
    df = pd.read_csv(DATAPATH / "Coffee" / "kopi.csv")
    uniqueBarangName = df[["id_kopi", "nama"]]
    return uniqueBarangName


def getSeriesIdAndNamaToko():
    df = pd.read_csv(DATAPATH / "toko" / "toko.csv")
    uniqueTokoName = df[["id_toko", "nama"]]
    return uniqueTokoName


def getSeriesFullKopi():
    kopiCsv = pd.read_csv(DATAPATH / "Coffee" / "kopi.csv")
    return kopiCsv


def getKaryawanDataById(IdKaryawan):
    df = pd.read_csv(DATAPATH / "Employee" / "Karyawan.csv").set_index("id_karyawan")
    return df.iloc[IdKaryawan].reset_index()


def get_screen_size():
    monitor = get_monitors()[0]
    return monitor.width, monitor.height

#(id_nota,status,tanggal,tanggal_pair,jenis_transaksi)
#status jenis transaksi di pakai untuk indexingnya
def updateNotaHeaderStatusAndTanggalPairByIdAndDate(listOfQuery):
    for i in listOfQuery:
        Year=i[2].strftime("%Y")
        Month=HASHMONTH[int(i[2].strftime("%m"))-1]
        Day=i[2].strftime("%d")
        headerCsv=pd.read_csv(DATAPATH / "Nota" / Year / Month / "nota_header.csv")
        headerCsv.loc[(headerCsv["id_nota"]==i[0]) & (headerCsv["jenis_transaksi"]==i[4]),"status_nota"]=i[1]
        if pd.isna(i[3]):
            headerCsv.loc[(headerCsv["id_nota"]==i[0]) & (headerCsv["jenis_transaksi"]==i[4]),"tanggal_pair"]=pd.NA
        else:
            headerCsv.loc[(headerCsv["id_nota"]==i[0]) & (headerCsv["jenis_transaksi"]==i[4]),"tanggal_pair"]=i[3].strftime("%d/%m/%Y %H:%M")
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


#(id_stok,stok,tanggal) listQueryInput
#id_stok,stok
def updateStokAvailableByIdMultiple(listOfQuery):
    monthPath=set([])
    for i in listOfQuery:
        monthPath.add(i[2])
    dictionaryCsv={}
    for i in monthPath:
        dictionaryCsv[i]=pd.read_csv(DATAPATH / "Coffee" / i / "stok.csv").set_index("id_stok")
    for query in listOfQuery:
        dictionaryCsv[query[2]]["stok"][query[0]]=query[1]+dictionaryCsv[query[2]]["stok"][query[0]]
    for i in monthPath:
        dictionaryCsv[i].reset_index(inplace=True)
        dictionaryCsv[i].to_csv(DATAPATH / "Coffee" / i / "stok.csv",index=False)


#(id_nota_detail,id_nota,id_ambil,qty,disc,harga_satuan,id_toko,id_kopi)
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
            "id_ambil":i[2],
            "qty":i[3],
            "disc":i[4],
            "harga_satuan":i[5],
            "id_toko":i[6],
            "id_kopi":i[7]
        }
        PulangCsv.loc[len(PulangCsv)]=row
    PulangCsv.reset_index(drop=True,inplace=True)
    PulangCsv.to_csv(DATAPATH / "Nota" / Year / Month / "nota_detail_pulang.csv",index=False)

#id_nota,total,status_nota,id_karyawan,jenis_transaksi,namapelanngan,id_sales,tanggal
def addNotaHeader(listQuery):
    for i in listQuery:
        Year=i[7].strftime("%Y")
        Month=HASHMONTH[int(i[7].strftime("%m"))-1]
        Day=i[7].strftime("%d")
        headerCsv=pd.read_csv(DATAPATH / "Nota" / Year / Month / "nota_header.csv")
        row={
            "id_nota":i[0],
            "total":i[1],
            "status_nota":i[2],
            "id_karyawan":i[3],
            "jenis_transaksi":i[4],
            "namapelangan":i[5],
            "id_sales":i[6],
            "tanggal":i[7].strftime("%d/%m/%Y %H:%M"),
            "tanggal_pair":i[8].strftime("%d/%m/%Y %H:%M")
        }
        headerCsv.loc[len(headerCsv)]=row
        headerCsv.reset_index(drop=True,inplace=True)
        headerCsv.to_csv(DATAPATH / "Nota" / Year / Month / "nota_header.csv",index=False)

#listofQuery(id_nota_detail,id_ambil,harga_satuan,id_toko,id_kopi,tanggal,stok)
def updateDetailNotaPulangIdStok(listOfQuery):
    for i in listOfQuery:
        Year=i[5].strftime("%Y")
        Month=HASHMONTH[int(i[5].strftime("%m"))-1]
        Day=i[5].strftime("%d")
        pulangCsv=pd.read_csv(DATAPATH / "Nota" / Year / Month / "nota_detail_pulang.csv")
        pulangCsv["id_ambil"]=pulangCsv["id_ambil"].astype(str)
        pulangCsv.loc[pulangCsv["id_nota_detail"]==str(i[0]),"id_ambil"]=str(i[1])
        pulangCsv.loc[pulangCsv["id_nota_detail"]==str(i[0]),"harga_satuan"]=str(i[2])
        pulangCsv.loc[pulangCsv["id_nota_detail"]==str(i[0]),"id_toko"]=str(i[3])
        pulangCsv.loc[pulangCsv["id_nota_detail"]==str(i[0]),"id_kopi"]=str(i[4])
        pulangCsv.loc[pulangCsv["id_nota_detail"]==str(i[0]),"qty"]=str(i[6])
        pulangCsv.to_csv(DATAPATH / "Nota" / Year / Month / "nota_detail_pulang.csv",index=False)

def getLatestStokIdByKopiId(IdKopi):
    stokCsv=pd.read_csv(DATAPATH / "Coffee" / "stok.csv")
    stokFilteredSort=stokCsv.loc[stokCsv["id_kopi"]==int(IdKopi)].sort_values(by="tanggal_exp", ascending=False).reset_index()
    return stokFilteredSort["id_kopi"][0]

def createListofUUID(ranges):
    listOfId=[ uuid.uuid4().hex for _ in range(ranges)]
    return listOfId

def datetimeToHashYearMonth(date:datetime.datetime):
    month=date.strftime('%m')
    year=date.strftime('%Y')
    hashedMonth=HASHMONTH[int(month)-1]
    return os.path.join(year,hashedMonth)


# #(id_nota,tanggal)
#yang perlu di delete row nota header nota, ambil
def deleteNotaHeaderBelangsung(listOfQuery):
    for i in listOfQuery:
        Year=i[1].strftime("%Y")
        Month=HASHMONTH[int(i[1].strftime("%m"))-1]
        Day=i[1].strftime("%d")
        #delete row di header
        headerCsv=pd.read_csv(DATAPATH / "Nota" / Year / Month / "nota_header.csv")
        headerCsv=headerCsv.loc[headerCsv["id_nota"].astype(str)!=str(i[0])]
        headerCsv.to_csv(DATAPATH / "Nota" / Year / Month / "nota_header.csv",index=False)


# #(id_nota,tanggal)
def deleteAmbilTableNotaById(listOfQuery):
    for i in listOfQuery:
        Year=i[1].strftime("%Y")
        Month=HASHMONTH[int(i[1].strftime("%m"))-1]
        Day=i[1].strftime("%d")
        ambilCsv=pd.read_csv(DATAPATH / "Coffee" / Year / Month / "ambil.csv")
        ambilCsv=ambilCsv.loc[ambilCsv["id_ambil"].astype(str)!=str(i[0])]
        ambilCsv.to_csv(DATAPATH / "Coffee" / Year / Month / "ambil.csv",index=False)

def deleteNotaDetailAmbilBelangsung(listOfQuery):
    for i in listOfQuery:
        Year=i[1].strftime("%Y")
        Month=HASHMONTH[int(i[1].strftime("%m"))-1]
        Day=i[1].strftime("%d")
        #delete row di header
        detailCsv=pd.read_csv(DATAPATH / "Nota" / Year / Month / "nota_detail_ambil.csv")
        detailCsv["id_nota"]=detailCsv["id_nota"].astype(str)
        detailCsv=detailCsv.loc[detailCsv["id_nota"]!=str(i[0])]
        detailCsv.to_csv(DATAPATH / "Nota" / Year / Month / "nota_detail_ambil.csv",index=False)


def deleteNotaDetailAmbilSelesai(listOfQuery):
    for i in listOfQuery:
        Year=i[1].strftime("%Y")
        Month=HASHMONTH[int(i[1].strftime("%m"))-1]
        Day=i[1].strftime("%d")
        #delete row di header
        detailrCsv=pd.read_csv(DATAPATH / "Nota" / Year / Month / "nota_detail_pulang.csv")
        detailrCsv["id_nota"]=detailrCsv["id_nota"].astype(str)
        detailrCsv=detailrCsv.loc[detailrCsv["id_nota"]!=str(i[0])]
        detailrCsv.to_csv(DATAPATH / "Nota" / Year / Month / "nota_detail_pulang.csv",index=False)


# #(id_nota,tanggal)
def deleteNotaHeaderSelesai(listOfQuery):
    for i in listOfQuery:
        Year=i[1].strftime("%Y")
        Month=HASHMONTH[int(i[1].strftime("%m"))-1]
        Day=i[1].strftime("%d")
        #delete row di header
        headerCsv=pd.read_csv(DATAPATH / "Nota" / Year / Month / "nota_header.csv")
        headerCsv=headerCsv.loc[(headerCsv["id_nota"].astype(str)!=str(i[0])) | (headerCsv["jenis_transaksi"]!=1)]
        headerCsv.to_csv(DATAPATH / "Nota" / Year / Month / "nota_header.csv",index=False)

# #lakuin secara bersamaan karena lebih mudah dia.
# #{jumlah,stok_id,tanggal}
# def getStokStatusAvailable(listOfQuery):
#     dataFrame=pd.DataFrame(columns=["id_stok","id_kopi","tanggal_exp","tanggal_masuk","stok"])
#     dictonary={}
#     for i in listOfQuery:
#         if i[2] in dictonary.keys():
#             dictonary[i[2]].append((i[1],i[0]))
#         else:
#             dictonary[i[2]]=[]
#     for i in dictonary:
#         Year=i.strftime("%Y")
#         Month=HASHMONTH[int(i.strftime("%m"))-1]
#         Day=i.strftime("%d")
#         #delete row di header
#         stokCsv=pd.read_csv(DATAPATH / "Coffee" / Year / Month / "stok.csv")
#         rowValue=[]
#         for z in dictonary[i]:
#             if stokCsv[]

# def getStokIdAmountByNotaId(id_nota,tanggal:datetime.datetime):
#     stringStrip='%d/%m/%Y %H:%M'
#     Year=tanggal.strftime("%Y")
#     Month=HASHMONTH[int(tanggal.strftime("%m"))-1]
#     Day=tanggal.strftime("%d")
#     headerCsv=pd.read_csv(DATAPATH / "Nota" / Year / Month / "nota_header.csv")
#     headerCsv=headerCsv.loc[headerCsv["id_nota"].astype(str)==id_nota]
#     ambilCsv=pd.DataFrame(columns=["id_ambil","id_stok","tanggal_stok","jumlah"],dtype=[str,str,str,np.int128])
#     for index,row in headerCsv.iterrows():
#         tanggalRow=datetime.datetime.strptime(row["tanggal"])
#         Year=tanggalRow.strftime("%Y")
#         Month=HASHMONTH[int(tanggalRow.strftime("%m"))-1]
#         tempCsv=pd.read_csv(DATAPATH / "Coffee" / Year / Month / "ambil.csv")
#         tempCsv=tempCsv.loc[tempCsv["id_stok"].astype(str)==row["id_nota"]]
#         ambilCsv=pd.concat([ambilCsv,tempCsv])
#     stok=pd.DataFrame(columns=["id_ambil","id_stok","tanggal_stok","jumlah"],dtype=[str,str,str,np.int128])
#     for index,row in ambilCsv.iterrows():
#         tanggalRow=datetime.datetime.strptime(row["tanggal"])
#         Year=tanggalRow.strftime("%Y")
#         Month=HASHMONTH[int(tanggalRow.strftime("%m"))-1]
#         tempCsv=pd.read_csv(DATAPATH / "Coffee" / Year / Month / "ambil.csv")
#         tempCsv=tempCsv.loc[tempCsv["id_stok"].astype(str)==row["id_nota"]]
#         ambilCsv=pd.concat([ambilCsv,tempCsv])
def addKopiData(listofData, df, PATH=DATAPATH, saveImage=False, imgfrom=None, imgto=None):
    """"id_kopi,nama,harga,biaya_produksi,foto
        1,robusta,15000,10000,dummy-order1.png"""
    # print(listofData, " - ", df, " - ", PATH)
    df.loc[len(df)] = listofData
    df.to_csv(PATH / "Coffee" / "kopi.csv", index=False)
    # print('saved')
    if saveImage:
        # print('run')
        
        shutil.copyfile(imgfrom, imgto / listofData['foto'])
        print('copied')
        
        # copyImagesToPath(
        #         imgfrom, imgto, f"{listofData['foto']}"
        #     )
    


# (id_nota,status)
def updateNotaHeaderStatusById(listOfQuery, date: datetime.datetime):
    Year = date.strftime("%Y")
    Month = HASHMONTH[int(date.strftime("%m")) - 1]
    Day = date.strftime("%d")
    headerCsv = pd.read_csv(DATAPATH / "Nota" / Year / Month / "nota_header.csv")
    for i in listOfQuery:
        headerCsv.loc[headerCsv["id_nota"] == i[0], "status_nota"] = i[1]
    headerCsv.reset_index(drop=True, inplace=True)
    headerCsv.to_csv(DATAPATH / "Nota" / Year / Month / "nota_header.csv", index=False)


def copyImagesToPath(uploadFromPath, CopiedToPath, name):
    # print('copying image running')
    # print(uploadFromPath, " -=========- ", CopiedToPath)
    # img1 = PILImage.open(r"{}".format(uploadFromPath))
    # img1.save(CopiedToPath / name)
    
    #cara 2
    # shutil.copy(uploadFromPath, CopiedToPath / name)
    try:
        shutil.copyfile(uploadFromPath, CopiedToPath / name)
        print('copied')
    except Exception as e:
        print(e)
    
    #cara 3
    # file = open(CopiedToPath / name, 'rb')
    # with open(uploadFromPath, 'wb') as new_file:
    #     while True:
    #         byte = new_file.read(1)
    #         if not byte:
    #             break
    #         file.write(byte[0])
