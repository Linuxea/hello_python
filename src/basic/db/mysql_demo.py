# coding=utf-8
import json
from datetime import date, datetime

import mysql.connector


# from
# https://stackoverflow.com/questions/11875770/how-to-overcome-datetime-datetime-not-json-serializable?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa
def json_serial(obj):
    """JSON serializer for objects not serializable by default json code"""
    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    raise TypeError("Type %s not serializable" % type(obj))


conn = mysql.connector.connect(user='root', password='root', database='daily_person', host="localhost")
if conn:
    print("连接db成功!")
cursor = conn.cursor()
cursor.execute("show tables;")
print('cursor.rowcount: %s' % cursor.rowcount)

for x in cursor.fetchall():
    table_name = x[0]
    print("table_name:%s" % table_name)
    sql = "select count(*) from %s; " % table_name
    cursor.execute(sql)
    for count in cursor.fetchall():
        print("%s 数据总数 %s" % (table_name, count[0]))

    # 数据导出
    fetch_sql = "select * from %s;" % table_name
    cursor.execute(fetch_sql)
    with open(table_name + ".txt", mode="w") as file:
        for tuple_data in cursor.fetchall():
            file.writelines(json.dumps(tuple_data, default=json_serial))

cursor.close()
conn.close()
