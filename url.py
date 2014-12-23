#!/usr/bin/env/ python
#coding:utf-8

import sys
reload(sys)
sys.setdefaultencoding('utf-8')


from handler.index import indexHandler
from handler.data import dataHandler
from handler.vm import vmHandler
from handler.vm import addVmHandler
from handler.vm import editVmHandler
from handler.build import buildHandler
from handler.build import buildListHandler
from handler.doc import docHandler
from handler.doc import doclistHandler
from handler.doc import addDocHandler

url=[
	(r'/',indexHandler),
	 (r'/data',dataHandler),
     (r'/doc',docHandler),
     (r'/docList', doclistHandler),
	 (r'/vm',vmHandler),
    (r'/build',buildHandler),
    (r'/buildList',buildListHandler),
    (r'/addVM',addVmHandler),
    (r'/addDoc',addDocHandler),
    (r'/editVM',editVmHandler)
]