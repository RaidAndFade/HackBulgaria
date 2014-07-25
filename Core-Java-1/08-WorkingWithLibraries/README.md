# GUI Email Composer

## Purpose:
An alternative to composing emails using a web browser.
You can set your desired SMTP hostname, port, username and password.
Also, composed emails can include an attachment.


## How to run:
If you want the whole repo
```
git clone git@github.com:syndbg/HackBulgaria.git
cd HackBulgaria/Core-Java-1/08-WorkingWithLibraries/
java -jar build/emailComposer.jar
```


If you want only the jar
```
wget https://github.com/syndbg/HackBulgaria/blob/master/Core-Java-1/08-WorkingWithLibraries/build/emailComposer.jar?raw=true -O emailComposer.jar
java -jar emailComposer.jar
```

## Important:
[Google introduced application passwords that break this application, unless you create create an app password for the Email Composer.](https://support.google.com/accounts/answer/185833)
However an alternative for Bulgarians is [abv.bg's SMTP server](http://help.abv.bg/?p=1350).


## Third-party libraries:
* javax.mail 1.4.4
* [apache.commons.email 1.3.2](http://commons.apache.org/proper/commons-email/)
