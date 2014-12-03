#!/usr/bin/env python
# coding:utf-8

import tornado.web

import sys

reload(sys)
sys.setdefaultencoding('utf-8')


class docHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("doc.html")

class doclistHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("docList.html")