#!/usr/bin/python3

from the_N_excelsheets import *
import pymysql


def first_okay_table(aaa):

    #取得当前以及清空的列表
    a_cleaneddata = aaa
    return a_cleaneddata

class conntsql():

    connect = pymysql.Connect(
        host='localhost',
        port=3306,
        user='root',
        passwd='123456',
        db='data_excel',
        charset='utf8'
        )

    cursor = connect.cursor()

    def conne(self):

        # 使用 execute()  方法执行 SQL 查询
        conntsql().cursor.execute("SELECT VERSION()")
        # 使用 fetchone() 方法获取单条数据.
        data = conntsql().cursor.fetchone()
        #print("Database version : %s " % data)


    def use_databases(self):

        #建立表格
        mysqll = 'use data_excel'
        # 使用 execute()  方法执行 SQL 查询
        conntsql().cursor.execute(mysqll)
        #提交事务方法
        conntsql().connect.commit()


    def create_table(self,Now_N_sheets,create_names_excel):

        # 执行创建表语句
        create_mysql_0 =  "CREATE TABLE IF NOT EXISTS "

        create_mysql_2 = """(`ID`  int(11) NOT NULL AUTO_INCREMENT ,
        `nemes`  varchar(20) CHARACTER SET utf8 COLLATE utf8_unicode_ci NULL DEFAULT NULL ,
        `entry_data`  varchar(20) CHARACTER SET utf8 COLLATE utf8_unicode_ci NULL DEFAULT NULL ,
        `departure`  varchar(20) CHARACTER SET utf8 COLLATE utf8_unicode_ci NULL DEFAULT NULL ,
        `phone`  varchar(20) CHARACTER SET utf8 COLLATE utf8_unicode_ci NULL DEFAULT NULL ,
        `License_type`  varchar(20) CHARACTER SET utf8 COLLATE utf8_unicode_ci NULL DEFAULT NULL ,
        `License_num`  varchar(20) CHARACTER SET utf8 COLLATE utf8_unicode_ci NULL DEFAULT NULL ,
        `sex`  varchar(20) CHARACTER SET utf8 COLLATE utf8_unicode_ci NULL DEFAULT NULL ,
        `shougu_data`  varchar(20) CHARACTER SET utf8 COLLATE utf8_unicode_ci NULL DEFAULT NULL ,
        `stores`  varchar(50) CHARACTER SET utf8 COLLATE utf8_unicode_ci NULL DEFAULT NULL ,
        `jobs`  varchar(20) CHARACTER SET utf8 COLLATE utf8_unicode_ci NULL DEFAULT NULL ,
        PRIMARY KEY (`ID`)
        )
        ENGINE=InnoDB
        DEFAULT CHARACTER SET=utf8 COLLATE=utf8_unicode_ci
        ROW_FORMAT=DYNAMIC;
        """

        #合并查询语句
        create_mysql_3 = create_mysql_0 +  create_names_excel + "_" + str(Now_N_sheets) + create_mysql_2
        # 使用 execute()  方法执行 SQL 查询
        conntsql().cursor.execute(create_mysql_3)
        #提交事务方法
        conntsql().connect.commit()


    def insert_data(self,Now_N_sheets,sheet,create_names_excel,aaa):

        # 插入数据

        insert_1 = " INSERT INTO "
        insert_3 = " (`nemes`, `entry_data`, `departure`, `phone`, `License_type`, `License_num`, `sex`, `shougu_data`, `stores`, `jobs`) "
        insert_4 = " VALUES ( '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s') "
        sql_insert =  insert_1 + create_names_excel + "_" + str(Now_N_sheets) +  insert_3  + insert_4
        #数据来源于clean_str文件
        #循环dataframe表格，进行遍历
        #首先取到当前的sheets中的行数：
        now_sheet = sheet
        now_nrows = now_sheet.nrows

        for i in range(now_nrows):

            #根据下标选取元素，选取第I行的names信息
            the_i_data_names = first_okay_table(aaa).at[i,'nemes']
            the_i_data_entry_data = first_okay_table(aaa).at[i, 'entry_data']
            the_i_data_departure = first_okay_table(aaa).at[i, 'departure']
            the_i_data_phone = first_okay_table(aaa).at[i, 'phone']
            the_i_data_License_type = first_okay_table(aaa).at[i, 'License_type']
            the_i_data_License_num = first_okay_table(aaa).at[i, 'License_num']
            the_i_data_sex = first_okay_table(aaa).at[i, 'sex']
            the_i_data_shougu_data = first_okay_table(aaa).at[i, 'shougu_data']
            the_i_data_stores = first_okay_table(aaa).at[i, 'stores']
            the_i_data_njobs = first_okay_table(aaa).at[i, 'jobs']

            #print("insert_step 1 ")

            data = (the_i_data_names,the_i_data_entry_data,the_i_data_departure,the_i_data_phone,
                    the_i_data_License_type,the_i_data_License_num,the_i_data_sex,the_i_data_shougu_data,
                    the_i_data_stores,the_i_data_njobs)

            #print(create_mysq2,sql_insert)
            # 使用 execute()  方法执行 SQL 查询
            conntsql().cursor.execute(sql_insert % data)

            # 提交事务方法
            conntsql().connect.commit()

            print('成功插入', conntsql().cursor.rowcount, '条数据')

            i += 1

    def close_database(self):
        # 关闭数据库连接
        conntsql().connect.close()

# if __name__ == "__main__":
#     Now_N_sheets = 5
#     conntsql().create_table(Now_N_sheets)
#     conntsql().insert_data(Now_N_sheets)
#     conntsql().close_database()