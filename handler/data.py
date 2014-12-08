#!/usr/bin/env python
# coding:utf-8

import tornado.web
import json
import sys
import time

reload(sys)
sys.setdefaultencoding('utf-8')
from optsql.database import dbHander

success = {
                "response": True,
                "success": True
}

fail = {
                "response": True,
                "success": False
}


class dataHandler(tornado.web.RequestHandler):
    def post(self):
        requestType = self.get_argument("requestType")
        requestPage = self.get_argument("page")
        requestData = self.get_argument("data")
        requestIp = self.request.remote_ip
        if (requestData == u"form"):
            if(requestPage == u"vm"):
                print requestData
                dbdataobj = {"id":self.get_argument("id"), "ip":self.get_argument("IP"), "user": self.get_argument("User"), "occupied": self.get_argument("Occupied"), "build": self.get_argument("Build"), "description": self.get_argument("Description")}
                print  dbdataobj
            if(requestPage == u"doc"):

                createdate = time.strftime('%Y/%m/%d',time.localtime(time.time()))
                docurl = "/resource"
                dbdataobj = {"id":self.get_argument("id"), "url":docurl,"docname":self.get_argument("Doc_Name"),"author":self.get_argument("owner"),"date":createdate,"likenum":self.get_argument("likeNum"),"catageotry":self.get_argument("catageotry")}
                print "a"
        if(requestData == u"likenum"):
            dbdataobj = {"id":self.get_argument("id"),"likenum":self.get_argument("likenum")}
            print dbdataobj

        if(requestType == u"read"):
            requestData = self.get_argument("data")
            dbData = dbHander().getData(requestPage, requestData)
            print dbData
            print type(requestData)
            print requestPage
            #print dbHander().transformData(dbData, requestPage)
            print
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
                print requestIp
                fileobj = open('temp/text.json', 'r')
                iplist = json.load(fileobj)
                fileobj.close()
                print type(iplist)

                doclikelist = iplist["log"]

                for i in range(0,len(doclikelist)):
                    if(int(dbdataobj["id"]) == doclikelist[i]["docid"]):
                        dociplist = doclikelist[i]["IP"]
                        if(int(dbdataobj["likenum"]) != len(dociplist)):
                            if(requestIp in dociplist):
                                # send to client
                                self.write({"result":"fail"})
                                return
                            else:
                                dociplist.append(requestIp)
                                dbdataobjtemp = int(dbdataobj["likenum"]) + 1
                                dbdataobj["likenum"] = str(dbdataobjtemp)
                                print dociplist
                                print iplist
                                fileobj = open('temp/text.json', 'w')
                                json.dump(iplist, fileobj)
                                fileobj.close()

                newAdddoc = {"docid":int(dbdataobj["id"]),"IP":[requestIp]}
                doclikelist.append(newAdddoc)
                dbdataobjtemp = int(dbdataobj["likenum"]) + 1
                dbdataobj["likenum"] = str(dbdataobjtemp)
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

