__author__ = 'vamsi'
import pandas
import pyodbc

server="VAMSI_LAPPY\TEST"
db="PRACTICE"

#Connection String
#conn=pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DB='+db+';Trusted_Connection=yes')
conn1=pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DB='+db+';Trusted_Connection=yes')

#Sql Command
sql="SELECT * FROM [PRACTICE].[dbo].EMPLOYEE"
#Creating a dataframe
df=pandas.read_sql(sql,conn1)

print(df.head())#display the data
