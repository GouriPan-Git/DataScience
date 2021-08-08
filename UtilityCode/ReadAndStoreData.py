# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 03:10:50 2020

@author: gouri
"""

#import csv
import pandas as pd
import pyodbc
#from sqlalchemy import create_engine, types
import numpy as np
#import mysql.connector
#from mysql.connector import FieldType

'''mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.") '''

project_dir = 'D:\\Gouri\\Financial Planning\\Portfolio Raw data\\'
#Change This
#fn_Stock_Raw_Data_Dec_2020='stocks Portfolio 31 Dec 2020.xls'
fn_Stock_Raw_Data ='stocks Portfolio 14 Apr 2021.xls'


#Change This
df_Stock_Raw_Data = pd.read_excel(project_dir+fn_Stock_Raw_Data,thousands=',',usecols=(['Stock','Latest Price','Quantity','Inv. Price','Inv. Date','Inv. Amt','Overall Gain','Overall Gain%','Latest Value','Notes']))
#df_Stock_Raw_Data.drop(['TOTAL'])
#Remove from bottom 1 row
df_Stock_Raw_Data = df_Stock_Raw_Data[:-1]
print(df_Stock_Raw_Data)
#Change This
#df_Stock_Raw_Data.rename(columns={'Latest Price as on 31 Dec 2020':'Latest Price'},inplace=True)

#df_Stock_Raw_Data_Dec_2020 = pd.read_excel(project_dir+fn_Stock_Raw_Data_Feb_2021,usecols=(['Stock','Latest Price as on 31 Dec 2020']))
#,['Quantity'],['Inv. Price'],['Inv. Date'],['Inv. Amt'].['Overall Gain'],['Overall Gain%'],['Latest Value'],['Notes']))

#Stock = df_Stock_Raw_Data_Dec_2020[['Stock']]
Stock = df_Stock_Raw_Data['Stock'].apply(lambda x: pd.Series(x.split('-')))
Stock.rename(columns={0:'StockName',1:'Sensex',2:'DateTime'},inplace=True)
Stock = Stock[['StockName','Sensex','DateTime']]
print(Stock)

#Change This
Stock['DateTime']= pd.to_datetime('14-04-2021')  


df_Stock_Raw_Data_Cleaned = pd.concat([Stock,df_Stock_Raw_Data],axis=1)

#df_Stock_Raw_Data_Cleaned = df_Stock_Raw_Data_Cleaned.astype({"StockName": "|S", "Sensex": "|S", "Notes": "|S"}) 

#Replacing the  NAN values of String objects in the dataframe with blank
df_Stock_Raw_Data_Cleaned['StockName'] = df_Stock_Raw_Data_Cleaned['StockName'].replace(np.nan, '', regex=True)
df_Stock_Raw_Data_Cleaned['Sensex'] = df_Stock_Raw_Data_Cleaned['Sensex'].replace(np.nan, '', regex=True)
df_Stock_Raw_Data_Cleaned['Notes'] = df_Stock_Raw_Data_Cleaned['Notes'].replace(np.nan, '', regex=True)


print('Before' + df_Stock_Raw_Data_Cleaned['Inv. Date'])
df_Stock_Raw_Data_Cleaned['Inv. Date']= pd.to_datetime(df_Stock_Raw_Data_Cleaned['Inv. Date'],format='%d-%m-%Y')
print(df_Stock_Raw_Data_Cleaned['Inv. Date'])

df_Stock_Raw_Data_Cleaned['Quantity']= df_Stock_Raw_Data_Cleaned['Quantity'].astype('int')
#df_Stock_Raw_Data_Cleaned['Quantity'] = pd.to_numeric(df_Stock_Raw_Data_Cleaned['Quantity'])
df_Stock_Raw_Data_Cleaned_Copy = df_Stock_Raw_Data_Cleaned
print(df_Stock_Raw_Data_Cleaned_Copy['Quantity'])


for index, row in df_Stock_Raw_Data_Cleaned.iterrows():
    print(row[1],row['Inv. Date'])
    

server = 'NEENAYI' 
database = 'Stock_Analysis' 
#username = 'username' 
#password = 'yourpassword' 

output_filename = 'df_Stock_Raw_Data_Cleaned.xlsx'
df_Stock_Raw_Data_Cleaned.to_excel(project_dir+output_filename)

cnxn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                      'Server=' + server +';'
                      'Database=' + database + ';'
                      'Trusted_Connection=yes;')
#cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()
# Insert Dataframe into SQL Server:
for index, row in df_Stock_Raw_Data_Cleaned.iterrows():
   print(index,row)
   cursor.execute("INSERT INTO Stock_Analysis.dbo.Raw_Source_Data (Stock_Name,Sensex,Reporting_Date,Latest_Price,Quantity,Inv_Price,Inv_Date,Inv_Amt,Overall_Gain,Overall_Gain_Percent,Latest_Value,Notes) values(?,?,?,?,?,?,?,?,?,?,?,?)", row['StockName'],row['Sensex'],row['DateTime'],row['Latest Price'],row['Quantity'],row['Inv. Price'],row['Inv. Date'],row['Inv. Amt'],row['Overall Gain'],row['Overall Gain%'],row['Latest Value'],row['Notes'])
cnxn.commit()


cursor.execute("SELECT DISTINCT Stock_Name,Reporting_Date,[Latest_Price]FROM Stock_Analysis.dbo.Raw_Source_Data;")

data=cursor.fetchall()
print('Selected record from table is:')

for i in data:

   print(i)
cursor.close()

# to check what odbc drivers you have installed in your system.
for driver in pyodbc.drivers():
    print (driver)

#x = Stock_String.split("-")
#print(x)
#df_Stock_Raw_Data_Dec_2020_Filtered = 


#df_2008_2010_Outpatient_Claims_Temp=df_2008_2010_Outpatient_Claims[['DESYNPUF_ID','ICD9_DGNS_CD_1','ICD9_DGNS_CD_2','ICD9_DGNS_CD_3','ICD9_DGNS_CD_4','ICD9_DGNS_CD_5','ICD9_DGNS_CD_6','ICD9_DGNS_CD_7','ICD9_DGNS_CD_8','ICD9_DGNS_CD_9','ICD9_DGNS_CD_10']]
#df_merge = pd.merge(dfx,file_name1, how ='left', on ='Constituent_ID')



#df_2008_2010_Outpatient_Claims_Temp_subset=df_2008_2010_Outpatient_Claims_Temp.sample(n=4000)
#output_filename = 'df_2008_2010_Outpatient_Claims_Temp_subset.xlsx'
#df_2008_2010_Outpatient_Claims_Temp_subset.to_excel(project_dir+output_filename)

#df_2008_Beneficiary_Summary_Subset=df_2008_Beneficiary_Summary[df_2008_Beneficiary_Summary['SP_DIABETES'] == 2]

#df_2008_2010_Prescription_Drug_Events_subset=df_2008_2010_Prescription_Drug_Events.sample(n=4000)
#output_filename1 = 'df_2008_2010_Prescription_Drug_Events_subset.xlsx'
#df_2008_2010_Prescription_Drug_Events_subset.to_excel(project_dir+output_filename1)