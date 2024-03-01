from utils.libs import *
from utils.converter import *

HASHMONTH=[
    "Januari",
    "Februari",
    "Maret",
    "April",
    "Mei",
    "Juni",
    "Juli",
    "Agustus",
    "September",
    "Oktober",
    "November",
    "Desember"
]
HASHJENISTRANSAKSI=[
    "Ambil",
    "Pulang",
    "Beli"
]

def hashJenisTransaksi(data):
    return HASHJENISTRANSAKSI(data)
