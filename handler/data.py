#!/usr/bin/env python
# coding:utf-8

import tornado.web
import json
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
from optsql.database import dbHander

success = {
                "response": True,
                "success": True
}

fail  =  {
                "response": True,
                "success": False
}


class dataHandler(tornado.web.RequestHandler):
    def post(self):
        requestType = self.get_argument("requestType")
        requestPage = self.get_argument("page")
        requestData = self.get_argument("data")
        requestIp = "9.110.94.12"
        if (requestData == u"form"):
            if(requestPage == u"vm"):
                print requestData
                dbdataobj = {"id":self.get_argument("id"), "ip":self.get_argument("IP"), "user": self.get_argument("User"), "occupied": self.get_argument("Occupied"), "build": self.get_argument("Build"), "description": self.get_argument("Description")}
                print  dbdataobj
            if(requestPage == u"doc"):
                dbdataobj = {"id":self.get_argument("id"), "docname":self.get_argument("docname"),"author":self.get_argument("author"),"date":self.get_argument("Date"),"likenum":self.get_argument("likeNum"),"catageotry":self.get_argument("catageotry")}
                print "a"

        if(requestType == u"read"):
            requestData = self.get_argument("data")
            dbData = dbHander().getData(requestPage, requestData)
            #print dbData
            #print requestPage
            #print dbHander().transformData(dbData, requestPage)
            clientdata = json.dumps(dbHander().transformData(dbData, requestPage))
            print clientdata
            self.write(clientdata)
            return

        if(requestType == u"write"):
            result = dbHander().writeData(requestPage, dbdataobj)
            print  result
            if(result == True):
                self.write(success)
            else:
                self.write(fail)
            return

        if(requestType == u"update"):
            if(requestPage == u"doc"):
                fileobj = open('temp/text.json', 'r')
                iplist = json.load(fileobj)
                fileobj.close()
                print type(iplist)
                dbdataobj={"id":1, "likenum":3}
                doclikelist = iplist["log"]
                for i in range(0,len(doclikelist)):
                    if(dbdataobj["id"] == doclikelist[i]["docid"]):
                        dociplist = doclikelist[i]["IP"]
                        if(dbdataobj["likenum"] != len(dociplist)):
                            if(requestIp in dociplist):
                                # send to client
                                self.write({"result":"fail"})
                                return
                            else:
                                dociplist.append(requestIp)
                                print dociplist
                                print iplist
                                fileobj = open('temp/text.json', 'w')
                                json.dump(iplist, fileobj)
                                fileobj.close()

            result = dbHander().updateData(requestPage, dbdataobj)
            if(result == True):
                self.write(success)
            else:
                self.write(fail)
            return

        if(requestType == u"delete"):
            result = dbHander().deleteData(requestPage, requestData)
            if(result == True):
                self.write(success)
            else:
                self.write(fail)
            return

