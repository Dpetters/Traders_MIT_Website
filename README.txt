Version 0.1.1

Traders@MIT Website

INSTALLATION

IMPORTANT: If you are setting this up on windows, read the "WINDOWS INSTALLATION PREP" section below first!

1. Make sure you either have "easy_install" or "pip" installed. Typing them in the terminal should tell you whether they are. If you do not have them, simply google for "setuptools".
2. Install virtualenv. This will allow you to install all the dependencies without polluting your global environment.
3. Create a python virtual environment using virtualenv named TRADERS by running “virtualenv TRADERS”. It gets put into whatever folder you run the command from.
4. OPTIONAL. For convenience, create the following aliases in "~/.bash_profile" (unix) or in "C:\bin\cmd_aliases.txt" (windows). Note that for unix you need the single quotes around the commands. For windows you don't.

alias td='cd $TRADERS_AT_MIT_WEBSITE'
alias ts='source $TRADERS_AT_MIT_VIRTUALENV/bin/activate'
Important: In the above aliases, replace the $ variables with their value. Tips as to find their value are right below.
$TRADERS_AT_MIT_VIRTUALENV = path to the virtual environment that you created in step 1.
$TRADERS_AT_MIT_WEBSITE = path to the project root.

Try opening a new cmd and running “td” followed by “ts”. This should activate the environment and put you in the right directory. You can use these aliases whenever you need to activate the TRADERS environment or cd into the project root.

5. IF USING WINDOWS: Download the winpy32 executable from http://www.lfd.uci.edu/~gohlke/pythonlibs/. Activate the TRADERS virtualenv. Now run "pip install $EXECUTABLE" where $EXECUTABLE is the path to the .exe u just downloaded.
6. cd into the project root. If you haven't cloned the project, run "git clone git@github.com:Dpetters/Traders_MIT_Website.git". It will get put into whatever folder you run the command from.
6. Make sure the TRADERS virtualenv is activated. Run "pip install –r requirements.txt" from the project root.
7. Create a copy of settings_local_template.py in the project root and name it settings_local.py
8. Open settings_local.py and replace """NAME, EMAIL""" with your name and email in ADMINS. Make sure to put each in quotations since they're strings.
9. Run “python manage.py syncdb --migrate”.
10. Run “fab load_data”
11. Go to localhost:8000. You’re all set!


WINDOWS INSTALLATION PREP
1. If you do not have git installed, then install the github windows client from windows.github.com
2. OPTIONAL. This step will allow you to create linux-style alises for convenience. Create '/bin' directory in C:. Inside of it create the following three files. Add the content between the triple quotes to the corresponding file. Once done, cd into the bin directory and run cmd_autorun_install.cmd

    1. cmd_autorun.cmd
    """
    @echo off
    cls
    doskey /macrofile=c:\bin\cmd_aliases.txt
    """
    2. cmd_autorun_install.cmd
    """
    reg add "hkcu\software\microsoft\command processor" /v Autorun /t reg_sz /d c:\bin\cmd_autorun.cmd
    """
    3. cmd_aliases.txt
    leave empty 
    
TYPICAL WORKFLOW
1. Open two terminals. In the first one activate the TRADERS virtualenv, cd into the project root, and run "python manage.py runserver". Leave the second for making commits.
2. Make whatever changes you need to.
3. Run "git add -A" or "git add <files to add>" to stage the files you changed.
4. Run "git commit -m '<commit message>'" to commit your changes.
5. Run "git push" to push the changes to staging.
6. Run "fab update" locally to update staging.

DATAFLOW
In order to have your local version of the site look exactly like the one that's live, I added scripts to the fabfile to allow you to commit all site data/media or load all the site data/media. You can only commit all site data/media on the production version of the site. Locally, you can load the data/media using the "fab load_data" command. For more about fab, check out fabfile.org. If you add new models to the site whose data you want committed, add them to DATA_MODELS in the fabfile.py.
