# -*- coding: utf-8 -*-
"""
Created on Mon Sep  5 10:53:34 2022

@author: BEEMO
"""

import matplotlib.pyplot as plt 
from bs4 import BeautifulSoup as bs
from sqlalchemy import create_engine
import pandas as pd
import seaborn as sns
import pymysql
import requests
import numpy
import time
import regex
import re
import json

url = 'https://listofdeaths.fandom.com/wiki/Game_of_Thrones#Before_the_Series'

from sqlalchemy import create_engine


pymysql.install_as_MySQLdb()
# =============================================================================
# Connecting the database to the database credentials file
# =============================================================================
with open("/Users/BEEMO/.secret/mysql.json") as f:
    login = json.load(f)
login.keys()
# =============================================================================
# Connection to the database dashboard
# =============================================================================
connection_str  = f"mysql+pymysql://{login['username']}:{login['password']}@localhost:3307/"
engine = create_engine(connection_str)
