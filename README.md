# Python_Docker_Redis_Flask_Compose
It is an exercise to implement a simple use to Python , Docker , Redis and Flask and Docker compose

It has been tested with:
docker-compose version 1.16.1, build 6d1ac21
docker-py version: 2.5.1
CPython version: 2.7.12
OpenSSL version: OpenSSL 1.0.2j  26 Sep 2016
homegroup:Python_Compose JEAS$ docker version
Client:
 Version:      17.09.0-ce
 API version:  1.32
 Go version:   go1.8.3
 Git commit:   afdb6d4
 Built:        Tue Sep 26 22:40:09 2017
 OS/Arch:      darwin/amd64

Server:
 Version:      17.09.0-ce
 API version:  1.32 (minimum version 1.12)
 Go version:   go1.8.3
 Git commit:   afdb6d4
 Built:        Tue Sep 26 22:45:38 2017
 OS/Arch:      linux/amd64
 Experimental: false


Instruction to use

1.- Go to Python_compose folder and execute docker-compose up
2.- Insert a message into Radis instance using : python appPython2Redis.py -n localhost -p 7001 -d 0 -k 'message' -v 'It is a value from key name named message last version'
3.- Finally runthe message with : python appGetMesssage.py -u "http://localhost:7070/hello" -k "message"

You should see something like that:

python appGetMesssage.py -u "http://localhost:7070/hello" -k "message"
Consulting to http://localhost:7070/hello
looking for key value for key name message
1
It is a value from key name named message last version
2
It is a value from key name named message last version
3
It is a value from key name named message last version
4
It is a value from key name named message last version
5
It is a value from key name named message last version
