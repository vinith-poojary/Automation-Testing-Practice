import openpyxl
from openpyxl.styles import PatternFill

#how to write rowcount,columncount,rowdata,writedata,fillgreencolor

def getRowcount(file, sheet):
    workbook = openpyxl.load_workbook(file)
    sheet = workbook[sheet]
    return (sheet.max_row)

def getColumncount(file, sheet):
    workbook = openpyxl.load_workbook(file)
    sheet = workbook[sheet]
    return (sheet.max_column)

def readData(file, sheet, rowcount, column, columnno, rownum):
    workbook = openpyxl.load_workbook(file)
    sheet = workbook[sheet]
    return sheet.cell(rownum,columnno).value

def writeData(file, sheet,rownum,columnno,data):
    workbook = openpyxl.load_workbook(file)
    sheet = workbook[sheet]
    sheet.cell(rownum,columnno).value=data
    workbook.save(file)

def fillGreenColor(file,sheet,rownum,columnum):
    workbook = openpyxl.load_workbook(file)
    sheet = workbook[sheet]
    greenfill=PatternFill(start_color='68b212',end_color='68b212',fill_type='solid')
    sheet.cell(rownum,columnum).fill=greenfill
    workbook.save(file)
