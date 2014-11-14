#!/usr/bin/env python
# coding:utf-8

import tornado.web
import json
import sys
from optsql.database import dbHandler

reload(sys)
sys.setdefaultencoding('utf-8')


class dataHandler(tornado.web.RequestHandler):
    def post(self):
        requesttype = self.get_argument("requestType")[0]
        requestpage = self.get_argument("requestpage")[0]
        # print requestPage
        if requesttype == u"read":

            self.write(requestdata)
        if requesttype == u"write":

            self.write()
        if requesttype == u"update":
        if requesttype == u"delete":

            self.write(vmdata)
