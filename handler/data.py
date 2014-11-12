#!/usr/bin/env python
#coding:utf-8

import tornado.web
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8') 
from database import


vmdataobj = {
	"response": True,
	"hasData": True,
	"tabName":"id,ip,user,Occupied,Build,Description",
	"data" : [
		[1,"9.110.94.110:8080","QC","M18","10.2.1003.156","Capsian xxx"],
		[2,"9.110.94.110:8080","QC","M18","10.2.1003.156","Capsian xxx"],
		[3,"9.110.94.110:8080","QC","M18","10.2.1003.156","Capsian xxx"],
		[4,"9.110.94.110:8080","QC","M18","10.2.1003.156","Capsian xxx"],
		[5,"9.110.94.110:8080","QC","M18","10.2.1003.156","Capsian xxx"],
		[6,"9.110.94.110:8080","QC","M18","10.2.1003.156","Capsian xxx"],
		[7,"9.110.94.110:8080","QC","M18","10.2.1003.156","Capsian xxx"],
		[8,"9.110.94.110:8080","QC","M18","10.2.1003.156","Capsian xxx"],
		[9,"9.110.94.110:8080","QC","M18","10.2.1003.156","Capsian xxx"]
	]
}

vmdata = json.dumps(vmdataobj)

class dataHandler(tornado.web.RequestHandler):
	def post(self):
		requestPage = self.get_arguments("data");
		# print requestPage
		if (requestPage == [u"VM"]):
			self.write(vmdata)
		