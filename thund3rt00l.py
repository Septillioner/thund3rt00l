"""
        Author    : Septillioner <egeismailkosedag@gmail.com> or <septillioner@protonmail.com>
        Name      : thund3rt00l(main)
"""

"""docstring for thund3rt00l.py"""

# Imports
import argparse
import thunderlib.checklib as chklb
from thunderlib.whois import whois
from urlparse import urlparse as ParseURL
config = {}
def LoadConfig():
	global config
	from json import loads
	try:
		with open('thunder-config.json',"r") as fp: config = loads(fp.read())
		return False
	except:
		print "Config error! Try again after please take a look config file."
		return True
def main():
	global config
	if(LoadConfig()):
		return
	parser = argparse.ArgumentParser(
		description = 'Network Analyze Tool'
	)
	# Const Args
	# --Required variables
	parser.add_argument('--url','-u',action='store',type=str,metavar='URL',help='Setting URL Variable. http:// or https:// must be in url!')
	parser.add_argument('--target-ipv4','-tipv4',action='store',type=str,metavar='IPv4 Address',help='Setting IPv4 Variable. Must be IPv4 Address')	
	
	# URL & Domain Events
	parser.add_argument('--whois',action='store_true',help='Domain querying with whois')
	
	# Argument Parsing
	argResult = parser.parse_args()
	if(argResult.url):
		if(chklb.CheckURL(argResult.url)):
			SplittedURL = ParseURL(argResult.url)
			if(argResult.whois):
				whq = whois(config["paths"]["whois-servers"])
				result = whq.Query(SplittedURL.netloc.split("www.")[-1])
				print "Whois Result(%s):\n%s"%((SplittedURL.netloc.split("www.")[-1],result["data"].replace("\n","\n\t")))
			else:
				print "Tool not entered."
		else:
			parser.print_usage()
	elif(argResult.target_ipv4):
		pass
	else:
		parser.print_usage()
if __name__ == '__main__':
	main()
