#获取第N张sheet表格
import datetime
from the_N_excelsheets import *
import xlrd
#获取第N张sheet表格
from datetime import datetime
from xlrd import xldate_as_tuple
import pandas as pd
from the_N_excelsheets import *
import xlrd
from datetime import datetime
from xlrd import xldate_as_tuple


def todaota(Now_N_sheets,j):  # 传入文件路径字符串即可，例如：get_excel_data('account.xlsx')

    #当前的第N张sheet
    sheet = get_excelNsheets(Now_N_sheets,j)[0]
    first_row_values = sheet.row_values(0)  # 第一行数据
    print(first_row_values)
    nrows = sheet.nrows  # 行数
    print(nrows)
    list = []
    num = 1

    for row_num in range(1, nrows):
        row_values = sheet.row_values(row_num)
        if row_values:
            str_obj = {}
        for i in range(len(first_row_values)):
            ctype = sheet.cell(num, i).ctype
            cell = sheet.cell_value(num, i)
            if ctype == 2 and cell % 1 == 0.0:  # ctype为2且为浮点
                cell = int(cell)  # 浮点转成整型
                cell = str(cell)  # 转成整型后再转成字符串，如果想要整型就去掉该行
            elif ctype == 3:
                date = datetime(*xldate_as_tuple(cell, 0))
                cell = date.strftime('%Y/%m/%d %H:%M:%S')
            elif ctype == 4:
                cell = True if cell == 1 else False
            str_obj[first_row_values[i]] = cell
        list.append(str_obj)
        # 把它变成PANDAS数据框输出：
        num = num + 1
    list = pd.DataFrame(list)
    print(list)
    return list


# if __name__=="__main__":
#
#     a = todaota(0,0)
