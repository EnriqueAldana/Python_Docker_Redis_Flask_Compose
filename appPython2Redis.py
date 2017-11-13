"""
Created on Nov 10 2017

@author: EnriqueAldana
"""

import sys,getopt
import redis


def main(argv):
   hostnameParameter = 'redis'
   hostportParameter = 6379
   hostdatabaseName =0
   keyName='message'
   keyValue='It is a message stored on Redis'
   arguments=0
   action=1

   try:
      opts, args = getopt.getopt(argv,"h:n:p:d:k:v:a:",["hostnameParameter=","hostportParameter=","hostdatabaseName=","keyName=","keyValue=","action="])
      arguments=args
   except getopt.GetoptError:
       print ('appPython2Redis.py -n <Redis host name>  -p <Redis host port> -d <Redis Database name> -k <key Name> -v <key Value> -a <Insert=1 or GetData=0> ')
       sys.exit(2)
   for opt, arg in opts:
       if opt == '-h':   # Requested Help to use it
         print ('appPython2Redis.py -n <Redis host name>  -p <Redis host port> -d <Redis Database name> -k <key Name> -v <key Value> -a <Insert=1 or GetData=0>')
         sys.exit()

       elif opt in ("-n", "--hostnameParameter"):
         hostnameParameter = arg

       elif opt in ("-p", "--hostportParameter"):
         hostportParameter = arg

       elif opt in ("-d", "--hostdatabaseName"):
         hostdatabaseName = arg
       elif opt in ("-k", "--keyName"):
         keyName = arg
       elif opt in ("-v", "--keyValue"):
         keyValue = arg
       elif opt in ("-a", "--action"):
         action = arg

   if len(arguments)== 0:
          if hostnameParameter==None:
              hostnameParameter = 'redis'
          if hostportParameter==None:
              hostportParameter= 6379
          if hostdatabaseName==None:
              hostdatabaseName=0

          print('appPython2Redis program has been started ')
          print ('Host name is ', hostnameParameter)
          print ('Port number is ', hostportParameter)
          print ('hostdatabaseName ' ,hostdatabaseName)
          print ('Key Name ' ,keyName)
          print ('Key Value ' ,keyValue)
          print ('Action ' ,action)

          try :
              	client = redis.StrictRedis(host=hostnameParameter,port=hostportParameter,db=hostdatabaseName)
                if action == 1:
                  client.set(keyName,keyValue)
              	  print("Set value from " , keyName, " " , client.get(keyName))
                else:
                  print("Get value from " , keyName, " " , client.get(keyName))
          except  redis.exceptions.ConnectionError:
           	print("Error trying to connect to Redis: ", sys.exc_info()[0])




if __name__ == "__main__":
   main(sys.argv[1:])
