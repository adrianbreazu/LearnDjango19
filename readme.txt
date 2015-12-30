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
    - $python manage.py runserver
    - if you want to run on a different port please add the port number
-