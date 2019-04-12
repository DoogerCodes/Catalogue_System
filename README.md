# Catalogue_System

Description: Simple item catalogue system that stores inputs given by the user and shown in a tabular form.

Dependencies:
  Django==2.2
  django-crispy-forms==1.7.2
  django-materialize==1.0.1a2
  pytz==2019.1
  sqlparse==0.3.0

Installation:
  *Note: This was done through Windows. Installation on other platforms may differ

1. Download Python through link: https://www.python.org/downloads/

2. Install Pip

3. Create virtual environment. On the console, type:
      pip install virtualenvwrapper-win
      mkvirtualenv name_of_environment
      workon name_of_environment (*to activate the virtual environment)
      
4. Check dependencies using:
      pip freeze
      
5. Install Django:
      pip install django==2.2
      
6. Install django-crispy-forms:
      pip install django-crispy-forms

7. Go to the project directory with manage.py

8. Run project by typing:
      python manage.py runserver

9. Open browser to the URL given
