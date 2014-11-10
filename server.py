#!/usr/bin/env/ python
#coding:utf-8

import tornado.ioloop
import tornado.options
import tornado.httpserver

import sys

from application import application
from tornado.options import define,options
define("port",default=8888,help="run on the given port",type=int)

def main():
	tornado.options.parse_command_line()
	http_server = tornado.httpserver.HTTPServer(application)
	http_server.listen(options.port)
	print "On Develop Status... running at localhost:%s/" %options.port
	print "Quit the Server with Contor-C"
	tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
        main()
