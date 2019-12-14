
# coding: utf-8
#!/bin/python

'''
	Designed By : 
 █     █░ ██▓ ██▓    ▓█████▄  ▒█████   ███▄    █  ██▓ ▒█████   ███▄    █ 
▓█░ █ ░█░▓██▒▓██▒    ▒██▀ ██▌▒██▒  ██▒ ██ ▀█   █ ▓██▒▒██▒  ██▒ ██ ▀█   █ 
▒█░ █ ░█ ▒██▒▒██░    ░██   █▌▒██░  ██▒▓██  ▀█ ██▒▒██▒▒██░  ██▒▓██  ▀█ ██▒
░█░ █ ░█ ░██░▒██░    ░▓█▄   ▌▒██   ██░▓██▒  ▐▌██▒░██░▒██   ██░▓██▒  ▐▌██▒
░░██▒██▓ ░██░░██████▒░▒████▓ ░ ████▓▒░▒██░   ▓██░░██░░ ████▓▒░▒██░   ▓██
	 4Dv4nC3d S34RcH 4 WOShelf 				>> by cL34n 3v3RytH!n9 <<
'''


# [ x0x0x0x0x0x0x0x0x0x0x0x0x0x00x0x0x0x0x0x0x0x0x0x0x0x 
# 		woarchbot python script to search the given 
# 	text inside eveyfile with .py and .txt extension 
# 	  in a dir then show the name of that file and 
# 	ask for replacing the given text with another one!

# 			WRITTEN-BY: --WILDONION--
# 	x0x0x0x0x0x0x0x0x0x0x0x0x0x00x0x0x0x0x0x0x0x0x0x0x0x ]



# SOURCES:
# https://stackoverflow.com/questions/3964681/find-all-files-in-a-directory-with-extension-txt-in-python
# https://stackoverflow.com/questions/3207219/how-do-i-list-all-files-of-a-directory
# https://stackoverflow.com/questions/845058/how-to-get-line-count-cheaply-in-python
# https://docs.python.org/2/library/fileinput.html
# http://nullsecurity.net/tools/backdoor.html



try:
    import sys, os, fileinput, requests, bs4, argparse
except ImportError as e:
    import pip
    installer = lambda : pip.main(['install', str(e)[15:]]) # TODO : attributeerror-module-pip-has-no-attribute-main
    importer = lambda x : __import__(str(x)).import_module()
    installer()
    importer()
	
class bcolors:
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'


def banner():
	print(bcolors.FAIL+"""	Designed By : 
				 █     █░ ██▓ ██▓    ▓█████▄  ▒█████   ███▄    █  ██▓ ▒█████   ███▄    █ 
				▓█░ █ ░█░▓██▒▓██▒    ▒██▀ ██▌▒██▒  ██▒ ██ ▀█   █ ▓██▒▒██▒  ██▒ ██ ▀█   █ 
				▒█░ █ ░█ ▒██▒▒██░    ░██   █▌▒██░  ██▒▓██  ▀█ ██▒▒██▒▒██░  ██▒▓██  ▀█ ██▒
				░█░ █ ░█ ░██░▒██░    ░▓█▄   ▌▒██   ██░▓██▒  ▐▌██▒░██░▒██   ██░▓██▒  ▐▌██▒
				░░██▒██▓ ░██░░██████▒░▒████▓ ░ ████▓▒░▒██░   ▓██░░██░░ ████▓▒░▒██░   ▓██
					 4Dv4nC3d S34RcH 4 WOShelf 	   >> by cL34n 3v3RytH!n9 <<
					 """+bcolors.ENDC)
	

def search():
	banner()
	try:
		parser = argparse.ArgumentParser()
		parser.add_argument("--path", help="Path To Scan")
		parser.add_argument("--text", help="Text To Search")
		parser.add_argument("--ext", help="Extensions Separated By Comma")
		args = parser.parse_args()
		# path = str(input(">>>Enter The Path : ")) # TODO: wirte it in such a way that i'll scan the whole machine and delete all files with .txt, .py, .exe, .dll and ... extension; kind of a virus bot
		if not os.path.exists(args.path):
			print("[-] Path of the file is Invalid!")
			sys.exit(1)
		key = args.text
		path = args.path
		extension = args.ext
		print("***********************************************")
		extension = extension.split(",")
	except KeyboardInterrupt:
		print("\n[*] ctrl C pressed!")
		sys.exit(1)

	for root, dirs_list, files_list in os.walk(path):
		for file_name in files_list:
			if os.path.splitext(file_name)[-1] in extension:
				file_name_path = os.path.join(root, file_name)
				with open(file_name_path, "rb") as f:
					counter = 0
					found = False
					for line in f.readlines():
						if key in line:# TODO: highlight founded key: use yellow color
							found = True
							counter = counter + 1
							print("[!] FOUND :::::: ", line)
							if '?v' in line: # TODO: also check channels
								proxies = {"https": "103.81.104.33:53281"}
								if key in bs4.BeautifulSoup(requests.get(line, proxies=proxies).text, "html.parser").title.text:
									print("[!] FOUND One Match Between UR Key & The Title Of [[", line, "]] => ((", bs4.BeautifulSoup(requests.get(line, proxies=proxies).text, "html.parser").title.text, "))")
								else:
									print("[*] Video Is About >>> [[", bs4.BeautifulSoup(requests.get(line, proxies=proxies).text, "html.parser").title.text, "]]")
					if found:
						print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
						print("[*] The File Name Is >>> [[", file_name, "]]")
						print("[*] The Full Path Of [[", file_name, "]] Is >>> ", file_name_path)
						print("[!] FOUND UR KEY IN ", counter, " LINEs.\n")
						print("[!] Scanned ", len(list(f)), " LINES.\n") # TODO: doesn't work! what is the bug??
						print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
				if found:
					want_change = input("[?] Wanna change The Key : ")
					if 'y' in want_change: # TODO: change the key in its line or change it in whole lines
						kchw = input(">>>Enter New Note To Replace It With The Current Key : ") 
						for i, line in enumerate(fileinput.input(file_name_path, inplace=1)):
							sys.stdout.write(line.replace(key, kchw))
							# if i == 4: sys.stdout.write('\n')  # write a blank line after the 5th line
					else:
						pass
				print("\n\n")



if "__main__" == __name__:
	search()
