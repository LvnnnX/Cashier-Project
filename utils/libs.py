from flet import *
import json
from pathlib import Path
from screeninfo import get_monitors
import flet.canvas as cv
from collections import namedtuple
import datetime
import locale
import re
import pandas as pd
from PIL import Image as PILImage
import os
import numpy as np
from dateutil.relativedelta import relativedelta
import shutil

BASEDIR = Path(__file__).parent.parent
JSONPATH = BASEDIR / 'json'
DATAPATH = BASEDIR / 'data'
IMGPATH = DATAPATH / 'img'
