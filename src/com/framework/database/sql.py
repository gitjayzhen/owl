#!/usr/bin/env python
# -*- coding:utf8 -*-

"""
20171116 需要操作的sql语句
"""
delete_sql = [
    'DELETE from TBL_CHGREQ WHERE ACCTNO = :id',
    ]

select_sql = [
    'select * from TBL_CHGREQ WHERE ACCTNO = :id',
    ]

select_sql_dict = {
    'TBL_CHGREQ': 'select * from TBL_CHGREQ WHERE ACCTNO = :id',
    }

data_info = {
    'TBL_CHGREQ': '信息',
}