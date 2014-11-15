#!/usr/bin/env python
#coding:utf-8

import tornado.web
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8') 
from optsql.database import dbHander

class dataHandler(tornado.web.RequestHandler):
	def post(self):
		requestPage = self.get_arguments("data");
		# print requestPage
		if (requestPage == [u"VM"]):
			dbdata = dbHander().getData("vm")
			vmdata = json.dumps(dbHander().transformData(dbdata,"vm"))
			self.write(vmdata)
		