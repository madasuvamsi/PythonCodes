__author__ = 'vamsi'
import pandas
import pyodbc

server="VAMSI_LAPPY\TEST"
db="PRACTICE"

#Connection String
conn=pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DB='+db+';Trusted_Connection=yes')

