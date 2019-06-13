Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 16:52:21) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> print "hello"
SyntaxError: Missing parentheses in call to 'print'. Did you mean print("hello")?
>>> print ("hello")
hello
>>> x=(25)
>>> type(x)
<class 'int'>
>>> x=input()
34-5+3
>>> type(x)
<class 'str'>
>>> 
>>> eval(x)
32
>>> x=eval(input())
34-33
>>> x
1
>>> x= eval(input("enter a vald expression:"))
enter a vald expression:
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    x= eval(input("enter a vald expression:"))
  File "<string>", line 0
    
    ^
SyntaxError: unexpected EOF while parsing
>>> x= eval(input("enter a valid expressio:"))
enter a valid expressio:34-22
>>> x
12
>>> 
