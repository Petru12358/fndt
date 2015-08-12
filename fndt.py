#!/usr/bin/python
import sys
import termcolor
if (len(sys.argv)==5 and sys.argv[1]=='-f'and sys.argv[3]=='-v'):

	def searchString(fileName=sys.argv[2], string=sys.argv[4]):
		f=fileName
		myFile = open(f)
		myString=string
		l=[]
		n=0
		print "The string: '" + myString + "' was founded in lines: "
		for line in myFile:
			n+=1
        		if myString in line:
				l.append(n)
				line=line.replace(myString, termcolor.colored(myString, 'red'))				
    				print l,line 
				del l[0]



	searchString()
if (len(sys.argv)==4 and sys.argv[1]=='-f'):
	def searchString1(fileName=sys.argv[2], string=sys.argv[3]):
		f=fileName
		myFile = open(f)
		myString=string
		l=[]
		n=0
		print "The string: '" + myString + "' was founded in lines: "
		for line in myFile:
        		n+=1
        		if myString in line:
        	    		l.append(n)
    		print l

	searchString1()




