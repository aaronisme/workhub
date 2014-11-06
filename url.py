#!/usr/bin/env/ python
#coding:utf-8

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from handler.index import indexHandler
from handler.login import loginHandler
from handler.build import buildHandler



url=[
	(r'/',indexHandler),
	(r'/login',loginHandler),
	(r'/build',buildHandler)
]