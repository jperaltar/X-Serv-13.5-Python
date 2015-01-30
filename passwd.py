#! /usr/bin/python
# -*- coding: utf-8 -*-

#Store lines from file /etc/passwd
fd = open("/etc/passwd", "r")
lines = fd.readlines()
fd.close()

#Store pairs user-shell in dictionary user_shells
user_shells = {}

for line in lines:
	#Divide lines by ":"
	arg_list = line.split(":")
	user_shells[arg_list[0]] = arg_list[-1]

#Print shells of users in list users
users = ['root', 'imaginario']

for user in users:
	try:
		print user + ":", user_shells[user]
	except:
		#Exception handler
		print 'User not found'
