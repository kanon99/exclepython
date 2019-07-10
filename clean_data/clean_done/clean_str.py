import pandas as pd
import numpy as np
from clean_done.maina import *

#把多余的字符串删除
def clesrningg(Now_N_sheets,j):

    a = str(todaota(Now_N_sheets,j))
    list = todaota(Now_N_sheets,j)

    #统计标题字符串数
    strnumbers = a.find("-")
    strnumbers1 = a.find("*")
    strnumbers3 = a.find(" ")
    strnumbers13 = a.find("\n")

    #统计标题字符串数
    strnumbers4= a.find("*")
    strnumbers5= a.find("\'")
    strnumbers6= a.find("\n")
    strnumbers7= a.find("\r")
    strnumbers8= a.find("\f")
    strnumbers9= a.find("\'")
    strnumbers10= a.find("\;")
    strnumbers11= a.find(" ")

    if strnumbers > 0:
        aa = list.rename(columns=lambda x: x.replace('-', ''), inplace=True)
    if strnumbers1 > 0:
        aa = list.rename(columns=lambda x: x.replace('*', ''), inplace=True)
    if strnumbers3 > 0:
        aa = list.rename(columns=lambda x: x.replace(' ', ''), inplace=True)
    if strnumbers13 > 0:
        aa = list.rename(columns=lambda x: x.replace('\n', ''), inplace=True)
    if strnumbers4 > 0:
        aa = list.replace("*",'')
    if strnumbers5 > 0:
        aa = list.replace("\'",'')
    if strnumbers6 > 0:
        aa = list.replace("\n",'')
    if strnumbers7 > 0:
        aa = list.replace("\r",'')
    if strnumbers8 > 0:
        aa = list.replace("\f",'')
    if strnumbers9 > 0:
        aa = list.replace("\'",'')
    if strnumbers10 > 0:
        aa = list.replace("\;",'')
    if strnumbers11 > 0:
        aa = list.replace(" ",'')

    aa = list.replace('', 'missing')

    #a10=a9.to_csv('Result.csv', encoding="gbk")
    return aa


# def arraytolist(self):
#
#     aa = clesrningg(self)
#     bb = np.array(aa)


#模糊匹配特定字符串并模糊匹配出相关字段的列信息
class findallneedstr(object):

    def findstr(rlist2,onestr,Now_N_sheets,Nexcels):
        rlist2 = clesrningg(Now_N_sheets,Nexcels)
        found = []
        for element in rlist2:
            if onestr in element:
                found.append(element)
        return found

    def findstr2(onestr,Now_N_sheets,Nexcels):

        aa = clesrningg(Now_N_sheets,Nexcels)
        global new_list_jobs,new_list_stores,new_list_Hire,new_list_sex,new_list_cardnum,new_list_cardtype,new_list,new_list1,new_list2,new_list3

        new_list_Hire = []
        new_list = []
        new_list3 = []
        new_list1 = []
        new_list2 = []
        new_list_cardtype = []
        new_list_cardnum = []
        new_list_sex = []
        new_list_stores = []
        new_list_jobs = []


        # 打印出模糊匹配的字符：打印出任职的姓名列的单元格字段
        onestr = "姓名"
        name_ = findallneedstr().findstr(onestr,Now_N_sheets,Nexcels)
        if name_ != []:
            #把姓名列转为为array：
            name_array = np.array(aa[name_])
            #获取名字list
            #print(name_array)
            for i in range(len(name_array)):
                new_list.append(name_array[i,0])

            # 打印出模糊匹配的字符：打印出任职的入职日期列的单元格字段
            onestr = "入职"
            enter_ = findallneedstr().findstr(onestr, Now_N_sheets,Nexcels)
            if enter_ == []:
                o = 0
                new_list3 = []
                for o in range(len(new_list)):
                    new_list3.append("missing")
                    o += 1


            else:
                if enter_ != []:
                    enter_array = np.array(aa[enter_])
                    # 获取入职list

                    for i in range(len(enter_array)):
                        new_list3.append(enter_array[i, 0])

                else:
                    pass

            # 打印出模糊匹配的字符：打印出任职的离职列的单元格字段
            onestr = "离职"
            fire_ = findallneedstr().findstr(onestr, Now_N_sheets,Nexcels)
            if fire_ == []:
                o = 0
                new_list1 = []
                for o in range(len(new_list)):
                    new_list1.append("missing")
                    o += 1
                # print('离职',new_list1)

            else:
                if fire_ != []:
                    findallneedstr_array = np.array(aa[fire_])
                    # 获取离职list

                    for i in range(len(findallneedstr_array)):
                        new_list1.append(findallneedstr_array[i, 0])

                else:
                    pass

            # 打印出模糊匹配的字符：打印出任职的手机列的单元格字段
            onestr = "手机"
            phone_ = findallneedstr().findstr(onestr, Now_N_sheets,Nexcels)
            # print(phone_)
            if phone_ == []:
                o = 0
                new_list2 = []
                for o in range(len(new_list)):
                    new_list2.append("missing")
                    o += 1
                # print('手机',new_list2)

            else:
                if phone_ != []:
                    phone_array = np.array(aa[phone_])
                    # 获取手机list

                    for i in range(len(phone_array)):
                        new_list2.append(phone_array[i, 0])

                else:
                    pass

            # 打印出模糊匹配的字符：
            onestr = "证照类型"
            cardtype_ = findallneedstr().findstr(onestr, Now_N_sheets,Nexcels)
            # print(phone_)
            if cardtype_ == []:
                o = 0
                new_list_cardtype = []
                for o in range(len(new_list)):
                    new_list_cardtype.append("missing")
                    o += 1
                # print('证照类型', new_list_cardtype)

            else:
                if cardtype_ != []:
                    cardtype_array = np.array(aa[cardtype_])
                    # 获取手机list

                    for i in range(len(cardtype_array)):
                        new_list_cardtype.append(cardtype_array[i, 0])

                else:
                    pass

                # 打印出模糊匹配的字符：
            onestr = "证照号码"
            cardnum_ = findallneedstr().findstr(onestr, Now_N_sheets,Nexcels)
            # print(phone_)
            if cardnum_ == []:
                o = 0
                new_list_cardnum = []
                for o in range(len(new_list)):
                    new_list_cardnum.append("missing")
                    o += 1
                # print('证照号码', new_list_cardnum)

            else:
                if cardnum_ != []:
                    cardnum_array = np.array(aa[cardnum_])
                    # 获取手机list

                    for i in range(len(cardnum_array)):
                        new_list_cardnum.append(cardnum_array[i, 0])

                else:
                    pass

                # 打印出模糊匹配的字符：
            onestr = "性别"
            sex_ = findallneedstr().findstr(onestr, Now_N_sheets,Nexcels)
            # print(phone_)
            if sex_ == []:
                o = 0
                new_list_sex = []
                for o in range(len(new_list)):
                    new_list_sex.append("missing")
                    o += 1
                # print('性别', new_list_sex)

            else:
                if sex_ != []:
                    sex_array = np.array(aa[sex_])
                    # 获取手机list

                    for i in range(len(sex_array)):
                        new_list_sex.append(sex_array[i, 0])

                else:
                    pass

                # 打印出模糊匹配的字符：
            onestr = "任职受雇"
            Hier_ = findallneedstr().findstr(onestr, Now_N_sheets,Nexcels)
            # print(phone_)
            if Hier_ == []:
                o = 0
                new_list_Hire = []
                for o in range(len(new_list)):
                    new_list_Hire.append("missing")
                    o += 1
                # print('任职受雇', new_list_Hire)

            else:
                if Hier_ != []:
                    Hier_array = np.array(aa[Hier_])
                    # 获取手机list

                    for i in range(len(Hier_array)):
                        new_list_Hire.append(Hier_array[i, 0])
                    # print('任职受雇', new_list_Hire)
                    # print(len(new_list_Hire))
                else:
                    pass

                # 打印出模糊匹配的字符：
            onestr = "门店"
            stores_ = findallneedstr().findstr(onestr, Now_N_sheets,Nexcels)
            # print(phone_)
            if stores_ == []:
                o = 0
                new_list_stores = []
                for o in range(len(new_list)):
                    new_list_stores.append("missing")
                    o += 1
                # print('门店', new_list_stores)
                # print(len(new_list_stores))
            else:
                if stores_ != []:
                    stores_array = np.array(aa[stores_])
                    # 获取手机list

                    for i in range(len(stores_array)):
                        new_list_stores.append(stores_array[i, 0])
                    # print('门店', new_list_stores)
                    # print(len(new_list_stores))
                else:
                    pass

                # 打印出模糊匹配的字符：
            onestr = "岗位"
            jobs_ = findallneedstr().findstr(onestr, Now_N_sheets,Nexcels)
            # print(phone_)
            if jobs_ == []:
                o = 0
                new_list_jobs = []
                for o in range(len(new_list)):
                    new_list_jobs.append("missing")
                    o += 1
                # print('岗位', new_list_jobs)
                # print(len(new_list_jobs))

            else:
                if jobs_ != []:
                    jobs_array = np.array(aa[jobs_])
                    # 获取手机list

                    for i in range(len(jobs_array)):
                        new_list_jobs.append(jobs_array[i, 0])
                    # print('岗位', new_list_jobs)
                    # print(len(new_list_jobs))
                else:
                    pass

        else:
            pass

        #假如一个储存成dataframe表格
        c = {"nemes": new_list,"entry_data": new_list3,"departure": new_list1,"phone": new_list2,"License_type":
            new_list_cardtype,"License_num": new_list_cardnum,"sex": new_list_sex,"shougu_data": new_list_Hire,"stores":
            new_list_stores,"jobs": new_list_jobs}
        newdata = pd.DataFrame(c)

        return newdata





