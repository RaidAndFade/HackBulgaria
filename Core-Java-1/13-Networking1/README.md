# 13 - Networking-1

## Includes:

* **InternetUtils** - a tool to print your own IPv4 or IPv6 address and find available IPv4 hosts in your network.
* **Echo Client and Echo Server** - a small client and server echoing messages back and forth between themselves.

## How to run:

If you want the whole repo
```
git clone git@github.com:syndbg/HackBulgaria.git
cd HackBulgaria/Core-Java-1/13-Networking1/
java -jar build/internetUtils.jar
java -jar build/echoServer.jar
java -jar build/echoClient.jar
```


If you want only the jars
```
wget https://github.com/syndbg/HackBulgaria/blob/master/Core-Java-1/13-Networking1/build/echoClient.jar?raw=true -O echoClient.jar
wget https://github.com/syndbg/HackBulgaria/blob/master/Core-Java-1/13-Networking1/build/echoServer.jar?raw=true -O echoServer.jar
wget https://github.com/syndbg/HackBulgaria/blob/master/Core-Java-1/13-Networking1/build/internetUtils.jar?raw=true -O internetUtils.jar
java -jar internetUtils.jar
java -jar echoServer.jar
java -jar echoClient.jar
```
