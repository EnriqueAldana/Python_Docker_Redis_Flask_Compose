"""
Created on Nov 10 2017

@author: EnriqueAldana
"""

import sys,getopt
import redis
import requests,json
import time

def main(argv):
   urlP = 'http://localhost:7070/hello'
   keyName='message'
   arguments=0
   try:
      opts, args = getopt.getopt(argv,"h:u:k:",["urlP=","keyName="])
      arguments=args
   except getopt.GetoptError:
       print ('appGetMessage.py -u <Url source>  -k <key Name> ')
       sys.exit(2)
   for opt, arg in opts:
       if opt == '-h':   # Requested Help to use it
         print ('appPython2Redis.py -n <Redis host name>  -p <Redis host port> -d <Redis Database name> -k <key Name> -v <key Value>')
         sys.exit()

       elif opt in ("-u", "--url"):
         urlP = arg
       elif opt in ("-k", "--keyName"):
         keyName = arg

   print "Consulting to "  + urlP
   print "looking for key value for key name " + keyName
   try:
   	response = requests.get(urlP)
   	if response.status_code == 200:
   		resp = response.json()
   		#print resp
   		if keyName in resp:
   			message=resp.get(keyName)
   			for i in range(1,6):
   				print i
				print message
				if i == 5:
					break
				time.sleep(10)
		else:
			print "The message labeled with key name as " + keyName + "is not located"
   	else:
   		print "The url given named " + urlP + " back response different like 200 status"
   except requests.exceptions.ConnectionError:
   		print "Failed to establish a new connection:  nodename nor servname provided, or not known"

if __name__ == "__main__":
   main(sys.argv[1:])
