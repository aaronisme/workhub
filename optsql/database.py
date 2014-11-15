#!/usr/bin/env python
# coding:utf-8

import mysql.connector
import json
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

conn = mysql.connector.connect(user='root', password='123456', database='workhub')
cur = conn.cursor()

class dbHander():
    def getData(self, table, num):
        if(num == 'all'):
            query = ("select * from " + table)
            cur.execute(query)
            data = cur.fetchall()
            conn.close()
            return data;

    # def writeData(self,table,data):

    def transformData(self, dbdata, page):
        if (len(dbdata) == 0):
            requestData = {
                "response": True,
                "hasData": False,
            }
            return requestData
        else:
            if (page == "vm"):
                requestData = {
                    "response": True,
                    "hasData": True,
                    "tabName": "id,ip,user,Occupied,Build,Description",
                    "data": dbdata
                }
                return requestData

