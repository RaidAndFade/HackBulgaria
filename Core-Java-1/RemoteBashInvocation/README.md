# Remote Bash Invocation (RBI)

## Purpose
Enables you to execute console commands from a client to a server using the RBI protocol.
The server logs the command and execution time.
The client prints the command output.

## Includes:
* RBI Protocol
* RBI Client
* RBI Server

## How to run:
If you want the whole repo
```
git clone git@github.com:syndbg/HackBulgaria.git
cd HackBulgaria/Core-Java-1/RemoteBashInvocation
java -jar RBI_Server/build/server.jar 
java -jar RBI_Client/build/client.jar
```


If you want only the jars
```
wget https://github.com/syndbg/HackBulgaria/blob/master/Core-Java-1/RemoteBashInvocation/RBI_Client/build/client.jar?raw=true -O client.jar
wget https://github.com/syndbg/HackBulgaria/blob/master/Core-Java-1/RemoteBashInvocation/RBI_Server/build/server.jar?raw=true -O server.jar
java -jar server.jar
java -jar client.jar
```
