import xlsxwriter
import os
import pandas as pd

"""
The logic of the function:
This will read the content of each excel sheet to a Pandas data frame and will loop though each Data frame and append 
the excel sheet as new row,
"""

def row_writer (file_name,sheet_name,filename_list):
    i=0
    with xlsxwriter.Workbook(file_name) as workbook:
        worksheet=workbook.add_worksheet(sheet_name)
        for x in filename_list:
            df=pd.read_excel(x)
            for row,column in df.iterrows():

                worksheet.write_row(i,0,column)
                i=i+1