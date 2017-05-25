# coding:utf-8
# 手贱写了个给某某网站刷人气的程序
# （侵权联删，勿做恶意攻击！！！）
# author：fanhualuomu
# usage: python visitor.py 20000000 [可自行设置] 
import requests
import json
import threading
from sys import argv

def visit(max_visitors):
	visitors=0
	while visitors<max_visitors:
		html=json.loads(requests.get('http://angularjs.cn/api/index').text)
		visitors=int(html['data']['visitors'])
		requests.get('http://angularjs.cn/')
		if visitors%10==0:
			print 'current visitors:',visitors

def main():
	# 目标访客数量
	max_visitors=int(argv[1])
	print max_visitors
	threads=[]
	# 多线程  （已证实开启程序，网站会卡）
	# ！！！线程数开小点玩玩即可，切勿搞大，测试500时网站已卡。
	# ！！！使用本程序造成目标站损失的后果自负，与本人无关！！！
	for i in range(10):
		threads.append(threading.Thread(target=visit,args=(max_visitors,)))
	for t in threads:
		t.start()
	t.join()

if __name__ == '__main__':
	main()