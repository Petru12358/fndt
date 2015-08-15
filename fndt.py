#!/usr/bin/python
import sys
import termcolor
from termcolor import colored
import colorama
from colorama import Back, Style
colorama.init()
l=[]
start = "\033[3;5m"
end = "\033[0;0m"
def print_Title(myString):
	print colored ("Welcome and congratulations!The searching string:'" + start + myString + "'"+end + " was founded in lines: ", 'yellow')
	
if (len(sys.argv)==5 and sys.argv[1]=='-f'and sys.argv[3]=='-v'):

	def searchString(fileName=sys.argv[2], myString=sys.argv[4]):
		myFile = open(fileName)
		print_Title(myString)
		n=0
		for line in myFile:
			n+=1
        		if myString in line:
				l.append(n)
				line=line.replace(myString, termcolor.colored(Back.GREEN+start+myString+Style.RESET_ALL+end, 'red'))				
    				print l,line 
				del l[0]
			



	searchString()
	del sys.argv
elif (len(sys.argv)==4 and sys.argv[1]=='-f'):
	def searchString1(fileName=sys.argv[2], myString=sys.argv[3]):
		myFile = open(fileName)
		print_Title(myString)
		n=0
		for line in myFile:
        		n+=1
        		if myString in line:
        	    		l.append(n)
    		print l

	searchString1()
	del sys.argv
	
elif(len(sys.argv)>1 and sys.argv[1]=='-v'):
	def search2(myString=sys.argv[2]):
		print_Title(myString)	
		n=0
		for line in sys.stdin:
			n+=1
			if myString in line:
				l.append(n)
				line=line.replace(myString, termcolor.colored(Back.GREEN+start+myString+Style.RESET_ALL+end, 'red'))							
				print l, line
				del l[0]

	search2()
	del sys.argv
else:
	def search3(myString=sys.argv[1]):
		print_Title(myString)	
		n=0
		for line in sys.stdin:
        		n+=1
        		if myString in line:
        	    		l.append(n)

    		print l


	search3()
	del sys.argv




