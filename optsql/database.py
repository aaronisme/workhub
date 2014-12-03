#!/usr/bin/env python
# coding:utf-8

import mysql.connector
import json
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
pwd = '123456'

class dbHander():
    def getData(self, table, data):
        conn = mysql.connector.connect(user='root', password = pwd, database='workhub')
        cur = conn.cursor()
        if (data == 'all'):
            query = ("select * from " + table)
        elif(data >=u'\u0030' and data<=u'\u0039'):
            query = ("select * from " + table + " where id = " + data)
        else:
            query = ("select * from " + table + " where catagory = " + "'"+ data + "'")
            print query
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
        conn = mysql.connector.connect(user='root', password= pwd, database='workhub')
        cur = conn.cursor()
        del data["id"]
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
        conn = mysql.connector.connect(user='root', password= pwd, database='workhub')
        cur = conn.cursor()
        dbidkey = data["id"]
        del data["id"]
        items = data.keys()
        values = data.values()
        print items[0]
        print values[0]
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
        conn = mysql.connector.connect(user='root', password= pwd, database='workhub')
        cur = conn.cursor()
        dbidkey = data
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
            if(page == "doc"):
                requestData = {
                    "response": True,
                    "hasData": True,
                    "tabName": "id,url,name,owner,time,description,good,catagory",
                    "data": dbdata
                }

                return  requestData
