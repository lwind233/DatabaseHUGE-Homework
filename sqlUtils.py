from sqlite3 import SQLITE_ANALYZE
from unittest import result
import pymysql
import os
import time
import traceback


def showColumns(db,tableName):
    '''
    返回表中列的名称和数据类型
    db:连接的数据库
    tableName:表名
    '''
    cursor = db.cursor()
    sql = "show columns from {}".format(tableName)
    cursor.execute(sql)
    columns = cursor.fetchall()
    ls = []
    for col in columns:
        ls.append((col[0],col[1]))
    return ls


def showTables(db,op):
    '''
    这个函数用于展示当前数据库中的表，并返回用户选择的表名
    db:连接的数据库
    op:对表的操作，如修改或者查询
    '''
    os.system('cls')
    cursor = db.cursor()
    sql = 'show tables'
    cursor.execute(sql)
    tables = cursor.fetchall()
    print('    -------------------------------------\n')
    print('    请选择您要进行{}的表'.format(op))
    for id,i in enumerate (tables):
        print('    ',id+1,i[0])
    print('    -------------------------------------\n')
    j = eval(input())
    os.system('cls')
    return tables[j-1][0]

def showTable(db,tableName):
    '''
    打印表内内内容,并返回一个id的映射字典用于进行修改操作。当表空时返回false
    映射字典像这样：{1:3,2:4,3:5},意味着打印内容中id等于1对应表内id等于3的行，以此类推。
    db:连接的数据库
    tableName:要打印的表的名称
    在此修改即可，使建立一个id的映射用于修改列号
    '''
    cursor = db.cursor()
    sql = 'select * from {}'.format(tableName)
    cursor.execute(sql)
    values = cursor.fetchall()
    data_nums = len(values)
    if data_nums == 0:
        print("该表空！3秒后返回上一页")
        time.sleep(3)
        return {},False
    columnName = showColumns(db,tableName)
    print("{:-^50}".format(tableName))
    for j in columnName:
        print(j[0],end='\t\t')
    print('')
    dic = {}
    for z,i in enumerate(values):
        print('{}'.format(z+1),end = '\t\t')
        dic[z+1] = i[0]
        for k in i[1:]:
            print('{}'.format(k),end='\t\t')
        print('')
    print("{:-^50}".format(''))
    return dic,True