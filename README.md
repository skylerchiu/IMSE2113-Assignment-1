
# How to run locally:
## Zipped folder: 
1. Extract all the contents from the zipped folder
2. Ensure an interpreter with Django is selected.
3. Run `python manage.py runserver`


## From git:
1. Git clone the repository using https.
2. Open the repository and open a new terminal
3. Run `python -m venv .\Django-env` to create the virtual environment
4. Select the virtial environment as the interpreter
5. Pip install django
6. Run `python manage.py runserver`




# Development Notes
## Activate the interpreter:
Settings -> Command Palette -> Python: Select Interpreter

## To run the Django app:
run `python manage.py runserver`

## Generate migrations
run `python manage.py makemigrations`
run `python manage.py migrate`

## Resources:
https://docs.djangoproject.com/en/5.0/topics/auth/default/#module-django.contrib.auth.views
https://realpython.com/customize-django-admin-python/#setting-up-the-django-admin 
https://www.freecodecamp.org/news/html-drop-down-menu-how-to-add-a-drop-down-list-with-the-select-element/
https://learndjango.com/tutorials/django-password-reset-tutorial
