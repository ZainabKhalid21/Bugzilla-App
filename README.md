# Bugzilla-App
Bugzilla is a Bug Tracking System . It helps us to solve bugs in our project . Different types of users with different roles are present . These users are : 
- Manager 
- Developer
- QA 
Manager is responsible for basic CRUD operations related to projects . They can also Add/Remove Developer and QA from the projects.

Developer is responsible for assigning bugs to himself and resolving a bug .

QA is responsible for CRUD operations related to bugs .

# Commmads
*To run the project :* 

- python manage.py runserver 

*For Database :*

- .\psql -U postgres -d postgres

*For running migrations :*

- python manage.py makemigrations
- python manage.py migrate


