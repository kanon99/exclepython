#!/usr/bin/python3
#导入得到的list，每个excel的表名称和当前的第N个sheet,组合成为数据库全名
import xlrd
from ffinally import *
from functools import lru_cache

@lru_cache(maxsize=500)
def get_excelNsheets(Now_N_sheets,j):

    # #读取已经生成好的excel工作簿路径列表文件
    workbook_origin = xlrd.open_workbook('C:\\Users\\Administrator\\PycharmProjects\\excel_all_data\\excelalldata.xlsx')

    #读取第一个sheet里面的所有excel文件列表信息
    sheet0 = workbook_origin.sheets()[0]
    nrows_values = sheet0.nrows
    first_row_values = sheet0.row_values(j)
    workbook = xlrd.open_workbook(first_row_values[0])
    create_names_excel = first_row_values[0][9:-5]
    Nsheets = len(workbook.sheet_names())
    sheet = workbook.sheets()[Now_N_sheets]

    nrows_values = sheet.nrows

    #返回sheet对象 和 当前工作簿的名称 , 行数 以及 sheets数量
    return  sheet , create_names_excel , nrows_values , Nsheets


# if __name__ == "__main__":
#     Now_N_sheets = 0
#     j = 0
#     a = get_excelNsheets(Now_N_sheets,j)
#     print(a)