#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
from clean_done.clean_str import *
from the_N_excelsheets import *
from conn_mysql_update import *
from functools import lru_cache

class Model():

    @lru_cache(maxsize=500)
    def calculate(self,orinin_0,Nexcels):

        aaa= findallneedstr().findstr2(orinin_0,Nexcels)
        sheet = get_excelNsheets(orinin_0,Nexcels)[0]
        create_names_excel = get_excelNsheets(orinin_0,Nexcels)[1]
        nrows_values = get_excelNsheets(orinin_0,Nexcels)[2]
        Nsheets = get_excelNsheets(orinin_0,Nexcels)[3]
        #print(aaa, sheet, create_names_excel, nrows_values, Nsheets)
        return aaa, sheet, create_names_excel, nrows_values, Nsheets


def mainmian(orinin_0,Nexcels):

    model = Model()
    #循环放在缓存当中
    i = 0
    for i in range(1):
        model.calculate(orinin_0,Nexcels)


    #从缓存提取数据
    for i in range(1):

        # 设置默认值
        Nsheets = Model().calculate(orinin_0,Nexcels)[4]
        create_names_excel = Model().calculate(orinin_0,Nexcels)[2]
        sheet = Model().calculate(orinin_0,Nexcels)[1]
        aaa = Model().calculate(orinin_0,Nexcels)[0]
        for Now_N_sheets111 in range(Nsheets):
            conntsql().create_table(orinin_0,create_names_excel)
            conntsql().insert_data(orinin_0,sheet,create_names_excel,aaa)

            Now_N_sheets111 += 1


# if __name__ == "__main__":
#     #nrows_values = Model().calculate(1, 0)[3]
#     mainmian(0,0)
#     #print("****************nrows: ", nrows_values)
