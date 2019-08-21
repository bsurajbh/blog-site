# blog-site
This is a simple kick start blog website built in django.

### Features:
1) Custom user model
2) User authentication,Login,Sign-up,Logout
3) Blog Addition
4) Publishing blog
5) Adding comments to blog

### Prerequisite

1) Python >= 3.6
2) Django >= 2.2
3) Pip installer
4) Mysql server installed

### Step to get started
```
cd blog-project/
. blog/bin/activate                           #this will activate virual enviroment 
cd blogsite/
mysql -u your yousername -p                   #log into mysql and create blog database 
create database blog;
exit
python3 manage.py migrate                     #migrate database
python3 manage.py runserver
```
