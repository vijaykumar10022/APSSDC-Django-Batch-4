# APSSDC-Django-Batch-4

[Click Here for syllabus](https://drive.google.com/file/d/1OnBUWHxKIa0ixTU8uKrWTGCE7HB3PbGl/view)

_____
### Day1(03-08-2020)
#### Day1 Content:
_____
- 1.Installation
  - download python exefile[for 64 bit os click here](https://www.python.org/ftp/python/3.6.6/python-3.6.6-amd64.exe)
  - download python exefile[for 32 bit os click here](https://www.python.org/ftp/python/3.6.6/python-3.6.6.exe)
- 2.Function in pYthon 
- 3.OOP'S in Python
  - Class
  - Object
  - Constructors
  
 ____
### Day2(04-08-2020)
#### Day-2 content:
_____

- 1.inheritance with examples
- 2.Python modues with examples
- 3.Python Packages with examples

- if want to install django package
    - pip install django
- Sublime editor linke [click here](https://www.sublimetext.com/3)

 ____
### Day-3(05-08-2020)
#### Day-3 content:
_____

- 1.introdution about django
- 2.MVC, MVT,Architecture of Django
- 3.Project Creation, APP creation and use of
admin app
 - note:select project location in localmachine
  - Project creation Command is 
    - django-admin startproject projectname
    - ex:django-admin startproject demo
  - after creation of project move one step forward 
      - cd projectname
      - ex: cd demo
  - App creation
      - python manage.py startapp appname
      - ex:python manage.py startapp myapp
  - Server Running
      - python manage.py runserver
        -->http://127.0.0.1:8000/urlname or localhost:8000/urlname
        -->ex:http://127.0.0.1:8000/hello or localhost:8000/hello
_________
### Day-4(06-08-2020)
#### Day-4 content:
_________

  - 1. Displaying content by using HttpResponse
  - 2. Using html,css and javascript in HttpResponse
      - This changes can be done in single HttpResponse or else we can use it in different HttpResponses
      - html => views.py
      - ex: 
      ```python 
      def hello(request):
          return HttpResponse("<h1>Hello Welcome Users</h1>")
      ```
      - css => views.py
      - ex:
      ```python 
      def hi(request):
          return HttpResponse("<h1 style='background-color:black;color:white'>Welcome to Django Session</h1>")
      ```
      - javascript => views.py
      - ex:
      ```python 
      def wt(request):
          return HttpResponse("<script>alert("Welcome User")</script>")
      ```
  - 3. Passing 2 or more parameter values in url of a browser and displaying by using HttpResponse
      - single parameter value passing with data type
      - single parameter => urls.py
      - ex: 
      ```python 
         path("sg/<int:t>/",views.roll),
      ```
      - single parameter => views.py
      - ex: 
      ```views.py``` 
      ```python 
      def roll(request,t):
          return HttpResponse("Your roll number is: "+t) 
      ```
      - two parameters => urls.py
      - ex: 
      ```python 
         path("sg/<int:t>/<str:na>/",views.roll),
      ```
      - two parameters => views.py
      - ex: 
      ```views.py``` 
      ```python 
      def roll(request,t,na):
          return HttpResponse("Your roll number is: "+t+"<br>"+"Your name is: "+na) 
      ```
      - similarly for n parameters with different data types
      - string formatting
      - ex: 
      ```views.py```
      ```python
      def roll(request,t,na):
          return HttpResponse("Your roll number is: {}\n Your name is: {}".format(t,na))
          ```
