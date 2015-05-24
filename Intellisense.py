#!/usr/bin/python
import sys
from os import listdir
from os.path import isfile, join
import subprocess
from subprocess import PIPE
from subprocess import STDOUT
import tty
import os.path

tty.setcbreak(sys.stdin)
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

class FileInfo:
	line = ""
	column = ""
	fileName = "" 
	check = False
	def __init__(self, error, compiler):
		if (compiler == 'CS'):
			split = error.split('(')
#			print ("split:")
#			print (split)
			if (len(split[0]) > 0 and ".cs" in split[0]):
#				print ("OKOKO")
				self.check = True
				if (len(split) > 1):
					self.fileName = split[0]
					if (len(split) > 1):
						split = split[1].split(",")
						if (len(split) > 1):
							if (is_number(split[0]) and self.check):
								self.line = split[0]
								split = split[1].split(")")
								if (is_number(split[0] and self.check)):
									self.column = split[0]
		if (compiler == 'C'):
			split = error.split(':')
#			print ("split:")
#			print (split)
			if (len(split[0]) > 0 and ".c" in split[0]):
#				print ("OKOKO")
				self.check = True
				if (len(split) > 1):
					self.fileName = split[0]
					if (len(split) > 2):
						if (is_number(split[1]) and self.check):
							self.line = split[1]
							#split = split[1].split(")")
						if (is_number(split[2] and self.check)):
							self.column = split[2]


help = "{{HELP}}: R: recompile, " #+ "  "
out = None
err = None

input = ""
if (len(sys.argv) >= 2):	

	print('Welcome to intellisense :')
	print('please specify language compiler: C: clang ; CS: mcs')
	input = sys.stdin.read(1);
	#if (input == 'C'):

	#elif (input == '')
	print('\n compile? (y for yes, n for no)\t\t(h for help)')
	compile = ord(sys.stdin.read(1))
if (compile == ord('y')):
	#print("OK");
	#print (sys.argv[1:])
	#p = subprocess.Popen(sys.argv[1 :], shell=True, stdin=subprocess.PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)

	p = subprocess.Popen(sys.argv[1 :], stdout=subprocess.PIPE, stderr=STDOUT)
	output = p.stdout.read()
	#out, err = p.communicate()
	#print ("ERRORS:")
	#print (err)
	lines = output.split("\n")
	for errorline in lines:
		print ("go to next error? (y / n)")
		key = ord(sys.stdin.read(1))
		if (key == ord('y')):
			fileInfo = FileInfo(errorline, input)

			#print ("HEYYY")
			#print (error)
			
			#print ("INFO:")
			print (fileInfo.fileName + ":" + fileInfo.line + ":" +  fileInfo.column)
			#if (os.path.isfile('/Applications/Sublime\ Text.app/Contents/MacOS/Sublime\ Text')):
			#print ("YES IT IS PUTAIN")
			print (errorline)
			if (len(fileInfo.fileName) > 0):
				subprocess.Popen(['/Applications/Sublime Text.app/Contents/MacOS/Sublime Text', fileInfo.fileName + ":" + fileInfo.line + ":" +  fileInfo.column], stdout=subprocess.PIPE, stderr=STDOUT)
			else:
				print ("No sublime text found")
elif (compile == ord('n')):
	pass
elif (compile == ord('h')):
	print(help)
#print(err)

#while (ok):
