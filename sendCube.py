#!/usr/bin/python
import serial
import string
import time
import sys

def ordPrint(str):
	for f in range(0,len(str) - 1):
		print(ord(str[f]))

def readLine(serObj):
	dataBit = serObj.read(1)
	lnData = ""

	while (dataBit != '\n'):
		lnData = lnData + dataBit
		dataBit = serObj.read(1)
		
	return (lnData)

def processCmd(cmd):
	serObj = serial.Serial("/dev/ttymxc3", 115200, rtscts=0, bytesize=8, timeout=None)

	serObj.write(cmd)

	line = ""

	while (line != '\f'):
		line = readLine(serObj).strip('\n\r')
		if (line != '\f'):
			print(line)

	serObj.close()

def main(argv):
	if (len(sys.argv) > 1):
		args = argv
		args.pop(0)
		cmd = " "
		cmd = cmd.join(args)
	
		processCmd(cmd)
	else:
		f = sys.stdin
		while (not f.closed):
			buffer = f.readline().strip('\n\r')
			if (buffer == ""):
				break
			processCmd(buffer)

if __name__ == "__main__":
	main(sys.argv)
