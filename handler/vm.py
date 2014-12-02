#!/usr/bin/env python
# coding:utf-8

import tornado.web

import sys

reload(sys)
sys.setdefaultencoding('utf-8')


class vmHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("vm1.html")


class addVmHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("addVM.html")

class editVmHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("editVM.html")