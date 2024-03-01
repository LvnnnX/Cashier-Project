from flet import *
import json
from pathlib import Path
from screeninfo import get_monitors
import flet.canvas as cv
from collections import namedtuple
import datetime
import re
import pandas as pd
from PIL import Image as PILImage
import os
import locale
import numpy as np
import uuid
from dateutil.relativedelta import relativedelta
import shutil

print(os.path.join(Path(__file__).parent.parent))
with open(os.path.join(Path(__file__).parent.parent,"assets/dir.txt")) as file:
    BASEDIR=Path(file.readline()[:-1])
JSONPATH = BASEDIR / 'json'
DATAPATH = BASEDIR / 'data'
IMGPATH = DATAPATH / 'img'

