Traders@MIT Website v0.1.1
==========================

Before working on the site, please add yourself to the traders-webdev@mit.edu email list.

INSTALLATION

1. Make sure you either have "easy_install" or "pip" installed. Typing them in the terminal should tell you whether they are. If you do not have them, simply google for "setuptools".
2. Install virtualenv. This will allow you to install all the dependencies without polluting your global environment.
3. Create a python virtual environment using virtualenv named TRADERS by running “virtualenv TRADERS”. It gets put into whatever folder you run the command from.
4. Install git and run "git clone git@github.com:Dpetters/Traders_MIT_Website.git". It will get put the project code into whatever folder you run the command from.
5. Make sure the TRADERS virtualenv is activated and run "pip install –r requirements.txt" from the project root.
6. Create a copy of settings_local_template.py in the project root and name it settings_local.py
7. Open settings_local.py and replace """NAME, EMAIL""" with your name and email in ADMINS. Make sure to put each in quotations since they're strings.
8. Run “python manage.py syncdb --migrate --noinput” to set up the database.
9. Run “fab load_data” to load production data locally.
10. Run "python manage.py runserver" to run the dev server.
11. Go to localhost:8000. You’re all set!

DATAFLOW

In order to have your local version of the site look exactly like the one that's live, I added scripts to the fabfile to allow you to commit all site data/media on production (using "fab commit_data") or load all the site data/media locally (using "fab load_data"). If you add new models to the site whose data you want committed, add them to DATA_MODELS in the fabfile.py.
