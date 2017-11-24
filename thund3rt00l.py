import argparse

def main():
	parser = argparse.ArgumentParser(
		description = 'Network Analyze Tool'
	)
	# Const Args
	# --Required variables
	parser.add_argument('--url','-u',action='store',type=str,metavar='URL',help='Setting URL Variable. http:// or https:// must be in url!')
	parser.add_argument('--target-ipv4','-tipv4',action='store',type=str,metavar='IPv4 Address',help='Setting IPv4 Variable. Must be IPv4 Address')	
	
	# URL & Domain Args
	parser.add_argument('--whois',action='store_true',help='Domain querying with whois')
	
	# Argument Parsing
	argResult = parser.parse_args()

if __name__ == '__main__':
	main()
