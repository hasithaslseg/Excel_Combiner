import xlsxwriter
import os
import pandas as pd
import openpyexcel
i=0
directory = 'CV'
b=(os.listdir(directory))



with xlsxwriter.Workbook('forecast1.xlsx') as workbook:
    worksheet=workbook.add_worksheet('all_data')
    for x in b:
        df=pd.read_excel(x)
        for row,column in df.iterrows():
            
            worksheet.write_row(i,0,column)
            i=i+1
