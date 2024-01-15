import sys
sys.path.append('../')
from utils.libs import *
from utils.importer import load_colors

def main(view:View):
    view.controls.append(Text("test"))