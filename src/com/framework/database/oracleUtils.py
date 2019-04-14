#!/usr/bin/env python
# -*- coding:utf8 -*-

'''
20171115 操作oracle数据库
'''


import cx_Oracle
from sql import select_sql, select_sql_dict, data_info


host = '192.168.18.*'
port = 1521
service = '*'
username = '*'
password = username


class DataSource(object):

    def __init__(self, host, port, service, user, passwd):
        self.host = host
        self.port = port
        self.service = service
        self.user = user
        self.passwd = passwd

        self.conn = None

        self.cur = None

    def connect(self):
        tns = cx_Oracle.makedsn(self.host, self.port, self.service)
        self.conn = cx_Oracle.connect(self.user, self.passwd, tns, encoding='utf-8')
        print "oracle server version :" + self.conn.version + "\n"
        self.cur = self.conn.cursor()
        return self.cur

    def close(self):
        self.cur.close()
        self.conn.close()

    def execute_select(self, _sql, _data):
        self.cur.prepare(_sql)
        result = self.cur.execute(None, _data)
        return result.fetchone()

    def execute_delete(self, _sql, _data):
        self.cur.prepare(_sql)
        result = self.cur.execute(None, _data)


db = DataSource(host, port, service, username, password)

def list_select():
    cur = db.connect()
    try:
        n = 1
        for s in select_sql:
            row = db.execute_select(s, {'id': num})
            print str(n) + ": " + str(row) + "\n"
            n += 1

    except Exception, e:
        print e
    finally:
        db.close()
        print "sql has executed !"


def dict_select(num):
    db.connect()
    try:
        for d in select_sql_dict:
            row = db.execute_select(select_sql_dict[d], {'id': num})
            print "{}表： -- {}".format(data_info[d], str(row))
    except Exception, e:
        print e
    finally:
        db.close()
        print "sql has executed !"


if __name__ == '__main__':
    num = '#'
    dict_select(num)