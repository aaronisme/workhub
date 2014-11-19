#!/usr/bin/env python
# coding:utf-8

import tornado.web

import sys

reload(sys)
sys.setdefaultencoding('utf-8')


class testHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("test.html")

    def post(self):
        data = self.get_argument("name")
        print type(data)
        print data
