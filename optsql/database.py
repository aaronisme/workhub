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
        else:
            query = ("select * from " + table + "where id = " + num)
        try:
            cur.execute(query)
            data = cur.fetchall()
        except:
            conn.rollback()

        conn.close()
        return data

    def writeData(self, table, data):
        items = data.keys()
        values = data.values()
        itemstr = data.keys()[0]
        valuestr = data.values()[0]
        for i in range(1,len(items)):
            itemstr = itemstr + ", " + items[i]
        for j in range(1,len(values)):
            valuestr = valuestr + ", " + values[i]

        query = ("insert into " + table + "(" + itemstr +")" +"values" + "("+ valuestr +")" )
        try:
            cur.execute(query)
            cur.commit()
            conn.close()
            return  True
        except:
            conn.rollback()
            conn.close()
            return False


    def updateData(self, table, data):

        return True
    def deleteData(self, table, data):

        return True

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

