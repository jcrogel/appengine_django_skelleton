# appengine_django_skelleton
The basic ingredients for quickly deploying a project on AppEngine

This is the basic skelleton to quickly develop and deploy a Django app in Appengine that has a restful api. The purpose is that 

### After cloning
  * Create a virtualenv to this directory
  * Edit app.yaml, replace appname in appengine
  * Run pip install -r requirements.txt
  * Replace git origin:
    git remote set-url origin https://github.com/USERNAME/OTHERREPOSITORY.git
  
### To run
dev_appserver.py --skip_sdk_update_check=yes --port=8080 --admin_port=8000 .
