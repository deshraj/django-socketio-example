# django-socketio-example
A sample django web application using django-socketio for creating socket connections

Note: Since the current version of django-socketio does not work with the latest version of gevent and gevent-socketio, so you need to install the previous version of gevent and gevent-socketio. Its already mentioned in requirements file. 

## Steps to setup the project:

1. Clone the repository using the command

      ``` git clone https://github.com/DESHRAJ/django-socketio-example.git ```

2. Create virtual environment

	``` cd django-socketio-example && virtualenv env```

3. Install the dependenices

	``` pip install -r requirements.txt ``` 

4. Start the server

	``` python manage.py runserver_socketio ```


Thats it. You are all set and ready to ROCK!
