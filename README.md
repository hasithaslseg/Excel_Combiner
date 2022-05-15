# Excel_Combiner
This code is used when you want to combine data in multiple excel sheets
The logic of the code is as follows
1. Read the file names in a folder as a list
2. Import the Excel_writer module and use excel_writer.row_writer() method
   there are three imput variables to the excel_writer.row_writer method.   
   
"""
input variable 1: Enter the name of the Excel Work Book you are going to create

input variable 2: Enter the name of the excel sheet

input variable 3: This will input the names of the excel files in the specified folder that you are going to merge as a List

"""

3. The row_writer function will read each excel in to pandas Data frame and will loop through each line and append the data to a new row in excel
