# Todolist
# This is my first practice of Django on todolist
![image](https://github.com/LawrenceGao0224/todolist/blob/main/Result.png)

There are add, delete functions.  

Django is a high-level Python web framework that enables rapid development of secure and maintainable websites.   

First, we need to build Django environment!  
* The following steps are on mac OS operation.  

1. Go to Homebrew : https://brew.sh/ (package manager of mac)  

2. Then install python on mac:  
```brew install python3``` 
```pip3 install pipenv```

3. Then create a todolist folder  

4. Under todolist folder, do the command ```pipenv install django==2.1```  (install django virtural environment under todolist)

5. Do```pipenv shell``` is under the virtural environment  

6. ```django-admin startproject edittodo_project .``` (. represent under the current directory in Unix)  

7. ```python manage.py runserver``` It would show the django website!   

8. ```python manage.py startapp hello``` Create a new app called hello!  

9. Go to the todolist folder, and in settings.py , find line 33 : INSTALLED_APP, add 'hello'

10. Go to hello folder, and in views.py, add: ```from django.http import HttpResponse```

11. And add  
```
def myView(request):
  return HttpResponse("Hello world!")
```  

12. Go to urls.py, add ```from hello.views import myView```

13. And add ```path('hello/', myView),``` under urlpatterns 

14. Go to the websit http://127.0.0.1:8000/hello/ it will show Hello world!




