import pandas
import re
import sys

def read_exce(_sheet):
    # df = pandas.read_excel('CASETA.xlsx', index_col=[0, 1, 2], skiprows=1, sheet_name='DANUBIO', )
    df = pandas.read_excel('DIRECCIONES.xlsx', usecols="A,B", skiprows=0, sheet_name=_sheet, )
    values = df.values
    
    for row in values:
        print(f"Calle->{row[1]}, Numero->{row[0]}")
       
if __name__ == '__main__':
    sheet_name = sys.argv[1]
    read_exce(sheet_name)
