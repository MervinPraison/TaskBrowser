# Task Browser using Django

## Basic

This is a simple Task browser app. 
The Task browser consists of fields such as Task ID, Task Name, Start Date, End Date, Parent. 
Duration and status of the task will be created during runtime

## Construction

1. Created Django app 
2. Sqlite database was used to save data
3. Django admin panel was created to manage data
4. REST API was created so that it could be used to create the React front-end
5. React, Next.js and Bootstrap are used to create the front-end

## Installation

### Installing Django App

```sh
git clone https://github.com/MervinPraison/TaskBrowser.git
cd TaskBrowser/DjangoTaskBrowserDjango
virtualenv env
source env/bin/activate
pip install -r requirements.txt
python tasks/manage.py runserver
```

### Installing React App

```sh
git clone https://github.com/MervinPraison/TaskBrowser.git
cd TaskBrowser/DjangoTaskBrowserReact
npm install
npm run dev
```

## Task Browser App Demo

1. Django App https://praison.com/tasksbrowser/
2. Admin Panel to manage data https://praison.com/tasksbrowser/administrator/ 
3. Django API https://praison.com/tasksbrowser/api/ , https://praison.com/tasksbrowser/api/1/ , https://praison.com/tasksbrowser/interface/
4. Front-end with React, Next JS and Bootstrap using API https://praison.com/tasksbrowserreact/

## Github Link 

https://github.com/MervinPraison/TaskBrowser

## Author

Mervin Praison
