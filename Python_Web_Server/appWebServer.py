"""
Created on Nov 10 2017

@author: EnriqueAldana
"""
import os,sys,getopt, json
import redis


class WebServer():

    WebServerHost = '0.0.0.0';
    WebServerPort = 8080;
    RadisHost='172.25.0.101';
    RadisPort=6379;
    RadisDB=0;
    KeyName="message"

    def configuration(self, hostname, portNumber,radisHost,radisPort,radisDB,keyname):
        print ("Configuring WebServer hostname and Port number")
        self.WebServerHost = hostname
        self.WebServerPort = int(portNumber)
        self.RadisHost=radisHost
        self.RadisPort= int(radisPort)
        self.RadisDB=radisDB
        self.KeyName=keyname
        print ("Configuration completed")

    def get_WebServerHost(self):
        return self.WebServerHost
    def get_WebServerPort(self):
        return self.WebServerPort
	def get_RadisHost(self):
		return self.RadisHost
	def get_RadisPort(self):
		return self.RadisPort
	def get_RadisDB(self):
		return self.RadisDB
	def get_KeyName(self):
		return self.KeyName



webserver = WebServer()
from flask import Flask
app = Flask(__name__)

@app.route("/hello")
def hello():

       try :
           client = redis.StrictRedis(host=webserver.RadisHost,port=webserver.RadisPort,db=webserver.RadisDB)
           message = client.get(webserver.KeyName)
           client.connection_pool.disconnect()
       except  redis.exceptions.ConnectionError:
           print("Error trying to connect to Redis: ", sys.exc_info()[0])
           message = "<i>cannot connect to Redis</i>"

       # return mes.toJSON()
       return json.dumps({webserver.KeyName: message})

@app.route("/")
def initialPage():
	html = "<h3> It is a Web application based on Flask microframework to Python </h3>" \
	"<b> It contain access to get a message when you go to /hello url. </b> <br/> " \
	"<b> This greeting message is stored in the Redis database </b> <br/>"\
	"<b> Data configuration </b><br/>" \
    "<b> server host: </b>" + str(webserver.WebServerHost) + "<br/>" \
	"<b> server port: </b>"+str(webserver.WebServerPort) +"<br/>" \
	"<b> redis host: </b>"+str(webserver.RadisHost) +"<br/>" \
	"<b> redis db: </b>"+str(webserver.RadisDB) +"<br/>" \
	"<b> redis port: </b>"+str(webserver.RadisPort) +"<br/>" \
	"<b> Key name: </b>"+str(webserver.KeyName) +"<br/>" \

        return html

def main(argv):

    hostnameParameter = '172.25.0.101'
    hostportParameter = 6379
    hostdatabaseName =0
    keyName='message'
    arguments=0
    server_host='0.0.0.0'
    server_port=8080


    try:
      opts, args = getopt.getopt(argv,"h:n:p:d:k:w:s",["hostnameParameter=","hostportParameter=","hostdatabaseName=","keyName=","server_host=","server_port="])
      arguments=args
    except getopt.GetoptError:
       print ('appPython2Redis.py -n <Redis host name>  -p <Redis host port> -d <Redis Database name> -k <key Name>  -w <server host> -s <server port>')
       sys.exit(2)
    for opt, arg in opts:
       if opt == '-h':   # Requested Help to use it
         print ('appWebServer.py -n <Redis host name>  -p <Redis host port> -d <Redis Database name> -k <key Name>  -w <server host> -s <server port>')
         sys.exit()

       elif opt in ("-n", "--hostnameParameter"):
         hostnameParameter = arg

       elif opt in ("-p", "--hostportParameter"):
         hostportParameter = arg

       elif opt in ("-d", "--hostdatabaseName"):
         hostdatabaseName = arg

       elif opt in ("-k", "--keyName"):
         keyName = arg

       elif opt in ("-w", "--server_host"):
         server_host = arg

       elif opt in ("-s", "--server_port"):
         server_port = arg


    webserver.configuration(server_host, server_port,hostnameParameter,hostportParameter,hostdatabaseName,keyName)
    print('appWebServer program has been started ')
    print ('Radis Host name is '+ hostnameParameter)
    print ('Redis Port number is ' + str(hostportParameter))
    print ('Redis DB Name ' + str(hostdatabaseName))
    print ('Key Name ' +keyName)
    print ('Server host ' + server_host)
    print ('Server port ' + str(server_port))





if __name__ == "__main__":
 main(sys.argv[1:])
    #app.run(host='0.0.0.0', port=80)

app.run(host=webserver.WebServerHost, port=webserver.WebServerPort)
