# -*- coding: utf-8 -*-
"""
Created on Sat Aug 27 10:19:44 2022

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

# =============================================================================
# BP: Which Team has most titles overall, top running streak in years in first division,
# which team has the most champions league and which league is the hardest? Hardest = 
# # of games per season, games played per team, average titles per games played, 
# =============================================================================

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
connection_str  = f"mysql+pymysql://{login['username']}:{login['password']}@localhost:3307/footballdatabase"
engine = create_engine(connection_str)

# =============================================================================
"""Football Database"""
# which is the best league ? business problem
# using wikipedia as a source - and using pandas as the main library (pandas.read_html)
# =============================================================================


# =============================================================================
# #premier league
# =============================================================================
premierleague = "https://en.wikipedia.org/wiki/Premier_League"
#extracting all tables in wikipedia link 
#match allows us to look for a specific string
premierleague2021 = pd.read_html(premierleague, match = "Position")
#since infotable is a list of table to call one specific table we use indexes
premierleague2021 = premierleague2021[0]

# =============================================================================
# laliga cleaning of the data 
# =============================================================================
#same process with other links
laliga = "https://en.wikipedia.org/wiki/La_Liga" 
dflaliga = pd.read_html(laliga)
# unnecessary since we can select from a list of datasets already parsed with pd.read_html
#but it is another way of selecting the dataframe with string "Location"
#laliga2021 = pd.read_html(laliga, match='Location')                        
laliga2021 = dflaliga[5]
barcelonarealmadrid = dflaliga[4]
# =============================================================================
# barcelona vs real madrid
# =============================================================================
barcelonarealmadrid = barcelonarealmadrid[['Season', 'RMA', 'BAR']]
barcelonarealmadrid = barcelonarealmadrid.drop(index=[24,22,23])
barcelonarealmadrid['RMA'] = barcelonarealmadrid['RMA'].astype(int)
barcelonarealmadrid['BAR'] = barcelonarealmadrid['BAR'].astype(int)


#TODO
def column_tie_win_loss(s):
    if (s['RMA'] > s['BAR']):
        return 1
    if (s['RMA'] < s['BAR']):
        return 0
    
# create a column for [win/loss/tie - binary rep /count plot], scored more than 5 goals, more than 4, more than 3
# create a dataset about the win rate for both, loss rate, mean goals scored, mean goals against

# =============================================================================
''' the reason we cannot rename columns like this although perfectly acceptable
is due to the fact that it turns them into Series and Arrays and usually stay as objects ''' 
# =============================================================================
# # columntranslation = [["Team Name",
# #                       "Location",
# #                       "20/21 Season Position",
# #                       "First Season in Top Division",
# #                       "Seasons in Top Division",
# #                       "First Season of Current Spell", 
# #                       "Seasons since Current Spell",
# #                       "Titles",
# #                       "Most Recent Winning Season"]]
# # laliga2021.columns = columntranslation
# # #this gets the values of every single column in the dataframe
# # def get_columns_and_values(df):
# #     for i in list(df):
# #         print(df[i].tolist)
# # #making thhe dataframe columns their correct datatype
# # laliga2021['Seasons in Top Division'] = laliga2021['Seasons in Top Division'].astype(int)
# # laliga2021['Seasons since Current Spell'] = laliga2021['Seasons since Current Spell'].astype(int)
# # laliga2021['Titles'] = laliga2021['Titles'].astype(int)
# # laliga2021['Team Name'] = laliga2021['Team Name'].astype(str)
# # laliga2021['20/21 Season Position'] = laliga2021['20/21 Season Position'].astype(str)
# # laliga2021['Most Recent Winning Season'] = laliga2021['Most Recent Winning Season'].astype(str)
# 
# =============================================================================
''' Plotting the teams with Titles '''
# sns.barplot(x = 'Team', y = 'Primera División titles', data=laligatitles)

#df.loc[:,df.columns.str.contains("titles")]
#making a sub dataset of teams whove won at least one title

#too crowded
laligatitles = laliga2021.loc[laliga2021['Primera División titles'] != 0]
sns.barplot(x = 'Team', y = 'Primera División titles', data=laligatitles)

#made it way nicer 
fig, ax = plt.subplots(figsize=(20, 10)) 
sns.barplot(x = 'Team', y = 'Primera División titles', data=laligatitles, ax=ax)
#filter that only keeps the column with the str in it
#laliga2021 = laliga2021[laliga2021.columns[laliga2021.columns.str.contains("titles")]]


                     
                       
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                            
                        
                            
                        
                            
                        
                            
