# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 14:05:43 2021

@author: gouri
"""
import pandas as pd
import tabula
#import pyodbc
#from sqlalchemy import create_engine, types
#import numpy as np
#import mysql.connector
#from mysql.connector import FieldType

project_dir = 'D:\\Gouri\\Financial Planning\\Portfolio Raw data\\'
#Change This
#fn_Stock_Raw_Data_Dec_2020='stocks Portfolio 31 Dec 2020.xls'
fn_NITRankData_2020='josaa-nit-cutoff-round-1.pdf'


#Converting PDF data to csv
df_NITRankData_2020 = tabula.read_pdf(project_dir+fn_NITRankData_2020,pages="all")
tabula.convert_into(project_dir+fn_NITRankData_2020, project_dir + "output.csv", output_format="csv", pages='all')
#df_Stock_Raw_Data.drop(['TOTAL'])
#Remove from bottom 1 row


# Reading CSV Data
fn_NITRankData_2020_CSV="NITCutOffRound2Source.csv"
df_NITRankData_2020_CSV = pd.read_csv(project_dir+fn_NITRankData_2020_CSV,header=None)
df_NITRankData_2020_CSV.columns=['SrNo','Institute','Academic Program Name','Quota','Seat Type','Gender','Opening Rank','Closing Rank']