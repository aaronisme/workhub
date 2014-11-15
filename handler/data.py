#!/usr/bin/env python
# coding:utf-8

import tornado.web
import json
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
from optsql.database import dbHander


class dataHandler(tornado.web.RequestHandler):
    def post(self):
        requestType = self.get_argument("requestType")[0]
        requestPage = self.get_arguments("page")[0]
        requestData = self.get_argument("data")[0]
        if(requestType == u"read"):
            requestData = self.get_argument("data")[0]
            dbData = dataHandler().getData(requestPage, requestData)
            clientdata = json.dumps(dataHandler().transformData(dbData, requestPage))
            self.write(clientdata)
            return False
        if(requestType == u"write"):
            dbData = json.loads(requestData)
            result = dbHander().wirteData(requestPage, dbData)
            if(result == True):
                self.write({"result":"success"})
            else:
                self.write({"result":"fail"})
            return False
        if(requestType == u"update"):
            dbData = json.loads(requestData)
            result = dbHander().updateData(requestPage, dbData)
            if(result == True):
                self.write({"result":"success"})
            else:
                self.write({"result":"fail"})
            return False
        if(requestType == u"delete"):
            dbData = json.loads(requestData)
            result = dbHander().deleteData(requestPage, dbData)
            if(result == True):
                self.write({"result":"success"})
            else:
                self.write({"result":"fail"})
            return False

