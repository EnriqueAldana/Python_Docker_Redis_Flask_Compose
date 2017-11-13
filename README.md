# Python_Docker_Redis_Flask_Compose
It is an exercise to implement a simple use to Python , Docker , Redis and Flask and Docker compose

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
