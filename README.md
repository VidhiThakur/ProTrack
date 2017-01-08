# ProTrack
Web-based Project Tracking Application.

# Setup for Local Environment:
 1) Install python3 ad django 1.10
 
 2) Clone from git repository to a local directory(Directory A)
 
 3) From command prompt,change to Directory A/ProTrack
 
 4) On command prompt,type- python manage.py createsuperuser(Enter any username and password)
  - Go to 127.0.0.1:8000/admin (Enter above created username and password to login)
  - Task section on home screen contains task tables: Task,Tags,Comments,SubTasks (Have read-write privileges here)
 
5) On command prompt,type- python manage.py runserver
  - Go to 127.0.0.1:8000/task/1 from any browser (Task 1)
  - Go to 127.0.0.1:8000/task/2 (Task 2)
  - Go to 127.0.0.1:8000/task/3 (Task 3 Doesn't exist-404 error)
 


