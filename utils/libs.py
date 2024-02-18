from flet import *
import json
from pathlib import Path
from screeninfo import get_monitors
import flet.canvas as cv
from collections import namedtuple
import datetime
import re
import pandas as pd
import os
import locale
import uuid
import numpy as np
from dateutil.relativedelta import relativedelta

BASEDIR = Path(__file__).parent.parent
JSONPATH = BASEDIR / 'json'
DATAPATH = BASEDIR / 'data'
IMGPATH = DATAPATH / 'img'

