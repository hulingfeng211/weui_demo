# -*- coding:utf-8 -*- 

import tornado 
import os
from tornado.gen import IOLoop
from tornado.web import Application,RequestHandler,url

class IndexHandler(RequestHandler):
	def get(self,*args,**kwargs):
		self.render('jquery-weui-demos/index.html')
		#self.write('hello,text')

class Index2Handler(RequestHandler):
	def get(self,*args,**kwargs):
		self.render('index.html')
		#self.write('hello,text')

class PageHandler(RequestHandler):
	#(r"/(P?<nickname>.*)/article/details/(P?<postid>.*)", MainHandler),
	def get(self,*args):
		#self.write(args[0])
		self.render('jquery-weui-demos/%s'%args[0])
		pass

						

settings = {
	'debug':True,
	'static_path':os.path.join(os.path.dirname(__file__),'static'),
	'template_path':os.path.join(os.path.dirname(__file__),'template'),

}


if __name__=='__main__':
	app=Application(handlers=[
		url(r'/',IndexHandler),
		#url(r'/2',Index2Handler),
		#(r"/(P?<nickname>.*)/article/details/(P?<postid>.*)", MainHandler),
		url(r'/(.*)',PageHandler),
		],**settings)
	app.listen(11108)
	IOLoop.current().start()
