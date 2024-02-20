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

import re

def find_substring(text, substring):
  # Create a regular expression pattern to match the substring, ignoring case.
  pattern = re.compile(rf"\b{substring}\b", re.IGNORECASE)

  # Search for the substring in the text.
  match = pattern.search(text)

  # Return True if the substring is found, False otherwise.
  return match is not None