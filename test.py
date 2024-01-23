import sys
sys.path.append('../')
from utils.libs import *
from utils.importer import *


# for m in get_monitors():
#     print(m.width, m.height)



detail=loadNotaDetailbyIdNotaPrimary(0,datetime.datetime.now(),1)
print(detail)