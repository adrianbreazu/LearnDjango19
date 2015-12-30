Lesson 1
- STEP 1 - Create a project
    - from command line run:
        $ django-admin startproject mysite
    - this will create:
        - manage.py: a command-line utility that lets you interact with Django projects
        - mysite/ directory - the actual Python package for your project
        - mysite/__init__.py - an empty file that tells Python that this directory should be considered
        a Python package
        - mysite/settings.py - settings/configuration dor this django project
        - mysite/urls.py - the URL declaration for this django project , a table of content
        - mysite/wsgi.py -  an entry-point for WSGI-compatible web servers to serve the project
- STEP 2 - RUN THE SERVER - NOT FOR PRODUCTION !!!
    $ python manage.py runserver
    - if you want to run on a different port please add the port number
- STEP 3 - CREATE AN APP
    - project vs app: an app is an web application that does somethig, a project is a collection of apps
    for an particular website. An app can be present in multiple projects
    - for creating an app run the following line in command line:
        $ python manage.py startapp polls
    - this will create a new directory structure:
- STEP 4 - WRITE YOUR FIRST VIEW
    - for this you need to edit the polls/views.py
    - in order to call a view you need to map it to URL, so please create file urls.py in polls directory
    - add the url line in polls/urls.py
    - after this you need to link the app urls.py to the project urls.py by changing the mysite/urls.py file
    - now with $python manager.py runserver you should be able to access the localhost:8000/polls/ message
-