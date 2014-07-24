# HackBulgaria Attendance Aggregator

## Purpose
Collects attendance info as JSON from [https://hackbulgaria.com/api/students](https://hackbulgaria.com/api/students) and [https://hackbulgaria.com/api/checkins/](https://hackbulgaria.com/api/checkins/) .

Current options are to show **individual attendance** or **people who attend more than 1 HackBulgaria course**. 
You have a good idea for a feature? Suggest it!

## How to run
If you want the whole repo
```
git clone git@github.com:syndbg/HackBulgaria.git
cd HackBulgaria/Core-Java-1/HackBulgariAttendanceAggregator/
java -jar build/attendance.jar
```


If you want only the attendance.jar
```
wget https://github.com/syndbg/HackBulgaria/blob/master/Core-Java-1/HackBulgariAttendanceAggregator/build/attendance.jar
java -jar attendance.jar
```

## Third-party libraries used 
* [Jettison 1.3.3](http://jettison.codehaus.org/)

P.S It's already included in the project and runnable jar

