#!/usr/bin/env python
# coding:utf-8

import mysql.connector
import json
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


class dbHander():
    def getData(self, table, num):
        conn = mysql.connector.connect(user='root', password='pass1234', database='workhub')
        cur = conn.cursor()
        if (num == 'all'):
            query = ("select * from " + table)
        else:
            query = ("select * from " + table + " where id = " + num)
        try:
            print query
            cur.execute(query)
            data = cur.fetchall()
            conn.close()
            return data
        except:
            conn.rollback()

        conn.close()
        return

    def writeData(self, table, data):
        conn = mysql.connector.connect(user='root', password='pass1234', database='workhub')
        cur = conn.cursor()
        items = data.keys()
        values = data.values()
        itemstr = data.keys()[0]
        valuestr = "'" + data.values()[0] + "'"
        for i in range(1, len(items)):
            itemstr = itemstr + ", " + items[i]
        for j in range(1, len(values)):
            valuestr = valuestr + ", " + "'" + values[j] + "'"

        query = ("insert into " + table + "(" + itemstr + ")" + " values " + "(" + valuestr + ")" )
        try:
            print query
            cur.execute(query)
            conn.commit()
            conn.close()
            return True
        except(Exception):
            print Exception
            conn.rollback()
            conn.close()
            return False


    def updateData(self, table, data):
        conn = mysql.connector.connect(user='root', password='pass1234', database='workhub')
        cur = conn.cursor()
        dbidkey = data["id"]
        del data["id"]
        items = data.keys()
        values = data.values()
        updatestr = items[0] + "=" + "'" + values[0] + "'"

        for i in range(1, len(items)):
            updatestr = updatestr + "," + items[i] + "=" + "'" + values[i] + "'"

        query = ("update " + table + " set " + updatestr + " where id = " + dbidkey)

        try:
            print query
            cur.execute(query)
            conn.commit()
            conn.close()
            return True
        except Exception as e:
            print e
            conn.rollback()
            conn.close()
            return False


    def deleteData(self, table, data):
        conn = mysql.connector.connect(user='root', password='pass1234', database='workhub')
        cur = conn.cursor()
        dbidkey = data["id"]

        query = ("delete from " + table + " where id = " + dbidkey)

        try:
            print query
            cur.execute(query)
            conn.commit()
            conn.close()
            return True
        except Exception as e:
            print e
            conn.rollback()
            conn.close()
            return False

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
                print "page is"
                requestData = {
                    "response": True,
                    "hasData": True,
                    "tabName": "id,ip,user,Occupied,Build,Description",
                    "data": dbdata
                }
                return requestData

