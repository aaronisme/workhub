#!/usr/bin/env python
#coding:utf-8

import tornado.web

import sys
reload(sys)
sys.setdefaultencoding('utf-8') 

class buildHandler(tornado.web.RequestHandler):
	def get(self):
		self.render("build.html")
		