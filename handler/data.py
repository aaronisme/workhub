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
        requestType = self.get_argument("requestType")
        requestPage = self.get_argument("page")
        requestData = self.get_argument("data")
        if (requestData == u"form"):
            if(requestPage == u"vm"):
                print requestData
                dbdataobj = {"id":self.get_argument("id"), "ip":self.get_argument("ip"), "user": self.get_argument("user"), "occupied": self.get_argument("Occupied"), "build": self.get_argument("Build"), "description": self.get_argument("Description")}
                print  dbdataobj
            if(requestPage == u"doc"):
                dbdataobj = {"id":self.get_argument("id"), "docname":self.get_argument("docname"),"author":self.get_argument("author"),"date":self.get_argument("Date"),"likenum":self.get_argument("likeNum"),"catageotry":self.get_argument("catageotry")}

        if(requestType == u"read"):
            requestData = self.get_argument("data")
            dbData = dbHander().getData(requestPage, requestData)
            print dbData
            clientdata = json.dumps(dbHander().transformData(dbData, requestPage))
            print clientdata
            self.write(clientdata)
            return False

        if(requestType == u"write"):
            result = dbHander().writeData(requestPage, dbdataobj)
            print  result
            if(result == True):
                self.write({"result":"success"})
            else:
                self.write({"result":"fail"})
            return
        if(requestType == u"update"):
            result = dbHander().updateData(requestPage, dbdataobj)
            if(result == True):
                self.write({"result":"success"})
            else:
                self.write({"result":"fail"})
            return
        if(requestType == u"delete"):
            result = dbHander().deleteData(requestPage, dbdataobj)
            if(result == True):
                self.write({"result":"success"})
            else:
                self.write({"result":"fail"})
            return

