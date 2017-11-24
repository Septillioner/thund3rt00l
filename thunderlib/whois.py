"""
	Author	  : Septillioner <egeismailkosedag@gmail.com> or <septillioner@protonmail.com>
	Main	  : thund3rt00l
	Tool Type : Service Query
	Tool	  : Whois Query
"""

"""docstring for whois.py"""



class whois:
	def __init__(self,WSFName):
		self.WSFName = WSFName
		self.ServerDict = {}
		self.ReceiveLimit = 20480
		self.ReceiveBuffer = 1024
		self.SocketTimeout = 5
		# Auto Loading Servers
		self.LoadServers()
	def LoadServers(self):
		from json import loads
		try:
			with open(self.WSFName,"r") as fp: self.ServerDict = loads(fp.read())
		except:
			print "Json error while loading file."
	def LoadConfiguration(self):
		# Not thinked yet
		pass
	def __HasServer(self):
		if(len(self.ServerDict) == 0):
			return False
		else:
			return True
	def Query(self,Domain):
		from socket import gethostbyname,AF_INET,SOCK_STREAM,socket
		# Check Servers
		if(not self.__HasServer):
			# Returning Error
			return {"state":False,
				"data" :"",
				"error":"Server data error"}
		# Query Command Configuration
		query_command = "%s\r\n"%(Domain)
		# Selecting Server
		whois_server = ""
		try:
			#print ".%s"%(".".join(Domain.split(".")[1:]))
			whois_server = self.ServerDict[".%s"%(".".join(Domain.split(".")[1:]))]
		except KeyError:
			# Error returning
			return {"state":False,
				"data" :"",
				"error":"Whois server not found."}
		# Socket Configuration
		sock = socket(AF_INET,
			      SOCK_STREAM)
		host = (gethostbyname(whois_server),
			43)
		sock.settimeout(self.SocketTimeout)
		# Connecting End Data Receiving Stage
		try:
			sock.connect(host)
			sock.send(query_command)
			buffer = ""
			received_buffer = "."
			while len(buffer) < self.ReceiveLimit:
				if(received_buffer == ""): break
				received_buffer = sock.recv(self.ReceiveBuffer)
				buffer += received_buffer
		except Exception,e:
			# Returning Error
			return {"state":False,
				"data" :"",
				"error":"%s"%(str(e))}
		# Giving buffer information
		if(len(buffer) >= self.ReceiveLimit):
			buffer += "...Data buffer overflowed (%s)"%(self.ReceiveLimit)
		# Returning buffer
		return {"state":True,
			"data" :buffer,
			"error":"Error not recorded."}

def main():
	whoisthis = whois(WSFName = "data_sources/wquery_servers.json")
	result = whoisthis.Query('example.com')
	if(result["state"]):
		print "Whois Result :"
		print "%s"%(result["data"].replace("\n","\n\t"))
	else:
		print "Failed Whois Query, Error message : %s"%(result["error"])
if __name__ == "__main__":
	main()
