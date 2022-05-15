import os
import excel_writer

# there are three input variables to the excel_writer.row_writer method
"""
input variable 1: Enter the name of the Excel Work Book you are going to create
input variable 2: Enter the name of the excel sheet you are going to create
input variable 3: This will input the names of the excel files in the specified folder that you are going to merge as a List which is generated from the listdir function
when you input the path of the directory
"""

b = (os.listdir(r'C:\Users\Acer\PycharmProjects\pythonProject\CV'))
excel_writer.row_writer('forecast3.xlsx', 'summary_all', b)
