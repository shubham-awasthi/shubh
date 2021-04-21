#!/usr/bin/python

print "Content-type:text/html\r\n\r\n"

import os
import cgi,commands,re,cgitb
import mysql.connector as mariadb





x=cgi.FieldStorage()
lang=x.getvalue('languages')
name=x.getvalue('n')
mes=x.getvalue('message')
inp=x.getvalue('input')


r=os.chdir("/var/www/html/")

f = open("{}.java".format(name),"w")
f.write("{}".format(mes))
f.close()

f = open("i{}.txt".format(name),"w")
f.write("{}".format(inp))
f.close()



d=commands.getstatusoutput("sudo docker run --rm -v \"$PWD\":/usr/src/myapp -w /usr/src/myapp java:7 javac {}.java".format(name))

e=commands.getstatusoutput("sudo docker run --rm -v \"$PWD\":/usr/src/myapp -w /usr/src/myapp java:7 cat i{}.txt | java {}".format(name,name))


f = open("{}.txt".format(name),"w")
f.write("{}".format(e[1]))
f.close()

print "<META HTTP-EQUIV=refresh CONTENT=\"0; URL=http://192.168.43.80/{}.txt\">".format(name)


a=commands.getstatusoutput("rm {}.java {}.class i{}.txt".format(name,name,name,name))








