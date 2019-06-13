Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 16:52:21) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> import datetime
>>> ob=datetime.datetime.now()
>>> print(type(ob))
<class 'datetime.datetime'>
>>> print(ob)
2019-06-12 13:08:20.037868
>>> print('-'*25)
-------------------------
>>> print(ob.year)
2019
>>> print(ob.month)
6
>>> print(ob.day)
12
>>> print(ob.hour)
13
>>> print(ob.minute)
8
>>> print(ob.second)
20
>>> str1=str(ob.hour)+':'+str(ob.minute)+':'+str(ob.second)
>>> print(str1)
13:8:20
>>> print('-'*25)
-------------------------
>>> print('1 week ago it was:',ob-datetime.timedelta(weeks=1))
1 week ago it was: 2019-06-05 13:08:20.037868
>>> print('100 days ago, it was:', ob-datetime.timedelta(days=100))
100 days ago, it was: 2019-03-04 13:08:20.037868
>>> print('1 week from now, it will be:',ob+datetime.timedelta(weeks=1))
1 week from now, it will be: 2019-06-19 13:08:20.037868
>>> yy=int(input("enter the year"))
enter the year
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    yy=int(input("enter the year"))
ValueError: invalid literal for int() with base 10: ''
>>> 
>>> 
>>> yy=int(input("enter the year"))
enter the year2017
>>> dd=int(input("enter the day"))
enter the day23
>>> bday=datetime.datetime(yy,mm,dd)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    bday=datetime.datetime(yy,mm,dd)
NameError: name 'mm' is not defined
>>> mm=int(input('enter the month'))
enter the month07
>>> bday=datetime.datetime(yy,mm,dd)
>>> 
>>> print("-"*25)
-------------------------
>>> print("birthday in", ob-bday)
birthday in 689 days, 13:08:20.037868
>>> print('-'*25)
-------------------------
>>> 
