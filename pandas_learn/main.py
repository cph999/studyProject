# coding=utf-8
import pandas as pd
import pymysql

INSERT_STUDENT_SQL = "insert into student (number, realName, classNo, identity, phone, roomNumber) values ('%s', '%s', '%s', '%s', '%s', '%s');"
SELECT_UNIQUE_SQL = ""

db = pymysql.connect(host='121.196.223.94',
                     port=3307,
                     user='root',
                     password='123456',
                     database='pandastest')

student_info = pd.read_excel("../2.xls")
cursor = db.cursor()
if __name__ == "__main__":
    try:
        columns = student_info.columns.values.tolist()  ### 获取excel 表头 ，第一行
        for idx, row in student_info.iterrows():
            d_row = {}
            for column in columns:
                d_row[column] = row[column]
            print(INSERT_STUDENT_SQL % (d_row["学号"], d_row["姓名"], d_row["专业班级"], d_row['身份证号'], d_row['联系方式'], d_row['楼号'] ))
            cursor.execute(INSERT_STUDENT_SQL % (d_row["学号"], d_row["姓名"], d_row["专业班级"], d_row['身份证号'], d_row['联系方式'], d_row['楼号']))
        db.commit()
    except:
        db.rollback()
    finally:
        db.close()
