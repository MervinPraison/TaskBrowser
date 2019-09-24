# Django Task Browser

Django Task Browser app.

```sh
$ virtualenv env
$ source env/bin/activate
$ pip install -r requirements.txt
$ python tasks/manage.py runserver
```

## Browser app

* ```tasks/browser``` folder contains the main Task Browser app

## Structure

* ```/tasks/browser/templates/browser/index.html``` is the main index file of the app
* ```/tasks/browser/templates/browser/detail.html``` is the the page which display the task in more detail
* ```/tasks/browser/models.py``` contains the ```Task``` model with status, duration and parent functions
* ```/tasks/browser/views.py``` contains ```index```, ```detail``` to render index.html and detail.html page
* ```/tasks/browser/views.py``` contains ```task_list```, ```task_detail```, ```task_detail``` to render ```/api/```, ```/api/1/```, ```/taskbrowser/interface/``` to create REST API
* ```/tasks/browser/admin.py``` to register Task module in Admin panel
