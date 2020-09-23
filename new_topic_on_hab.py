#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, sys

HOME_DIR = "/home/user"

LAST_DIR = HOME_DIR + "/.habralast"
HTML_DIR = HOME_DIR + "/.habr.html"
SHOW_FIRST_TIME = 5
n = 1
new_addr = 0
count = 0

if os.path.isfile(LAST_DIR):
	fp = open(LAST_DIR, "r")
	topic1 = fp.readline()
	fp.close()
	last_existed = 1
else:
	fp = open(LAST_DIR, "w")
	topic1 = ""
	fp.close()
	last_existed = 0

while(1):
	if n == 1:
		url = "habrahabr.ru"
	else: url = "habrahabr.ru/page" + str(n) + "/"
	wget = "wget " + url + " -O " + HTML_DIR
	try:
		os.system(wget)
	except:
		print "Cannot connect to server"
		sys.exit()

	index = open(HTML_DIR, "r")
	s = '				  <a href="http://habrahabr.ru/'
	ss = '						<a'
	sss = '			<div class="published"><!-- Дата в формате ISO пихается в title -->'

	for i in range(2000):
		line = index.readline()
		if s in line:
			blog_s = line.find('">')
			blog_e = line.find("</a>")
			blog = line[blog_s+2:blog_e]

			for j in range(50):
				line = index.readline()
				if ss in line:
					topic_s = line.find('">')
					topic_e = line.find("</a>")
					topic = line[topic_s+2:topic_e]
					if topic.find("</span>") != -1:
						topic = topic[topic.find("</span>")+7:]
					if topic != topic1:
						if new_addr == 0:
							fp = open(LAST_DIR, "w")
							fp.write(topic)
							fp.close()
							new_addr = 1
						print "Blog:\t" + blog
						print "Topic:\t" + topic

						for k in range(100):
							line = index.readline()
							if sss in line:
								line = index.readline()
								time_s = line.find("<span>")
								time_e = line.find("</span>")
								date = line[time_s+6:time_e]
								print "Date:\t" + date + "\n"
								notify = "notify-send 'Habrahabr.ru: " + blog + "' '" + topic + "\n<i>" + date + "</i>'"
								os.system(notify)
								count += 1
								if count == SHOW_FIRST_TIME and last_existed == 0:
									os.system("rm -f " + HTML_DIR)
									sys.exit()
								break
						break
					else:
						os.system("rm -f " + HTML_DIR)
						sys.exit()
	n += 1
	index.close()
