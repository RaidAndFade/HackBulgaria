# GUI Email Composer

## Purpose:
An alternative to composing emails using a web browser.
You can set your desired SMTP hostname, port, username and password.
Also, composed emails can include an attachment.


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

## Important:
[Google introduced application passwords that break this application, unless you create create an app password for the Email Composer.](https://support.google.com/accounts/answer/185833)
However an alternative for Bulgarians is [abv.bg's SMTP server](http://help.abv.bg/?p=1350).


## Third-party libraries:
* javax.mail 1.4.4
* [apache.commons.email 1.3.2](http://commons.apache.org/proper/commons-email/)
