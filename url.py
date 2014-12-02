#!/usr/bin/env/ python
#coding:utf-8

import sys
reload(sys)
sys.setdefaultencoding('utf-8')


from handler.index import indexHandler
from handler.data import dataHandler
from handler.vm import vmHandler
from handler.vm import addVmHandler
from handler.test import testHandler
url=[
	(r'/',indexHandler),
	 (r'/data',dataHandler),
	 (r'/vm',vmHandler),
    (r'/test',testHandler),
    (r'/addVM',addVmHandler)
]