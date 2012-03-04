Version 0.1.1

Traders@MIT Website

INSTALLATION

IMPORTANT: If you are setting this up on windows, read the "WINDOWS INSTALLATION PREP" section below first!

10. Make sure you either have "easy_install" or "pip" installed. Typing them in the terminal should tell you whether they are.
11. Install virtualenv. This will allow you to install all the dependencies without polluting your global environment.
12. Create a python virtual environment using virtualenv named TRADERS by running “virtualenv TRADERS”
13. For convenience, create the following aliases in "~/.bash_profile" (unix) or in "C:\bin\cmd_aliases.txt" (windows). Note that for unix you need the single quotes around the commands. For windows you don't.

alias td='cd $TRADERS_AT_MIT_WEBSITE'
alias ts='source $TRADERS_AT_MIT_VIRTUALENV/bin/activate'
Important: In the above aliases, replace the $ variables with what's on the right of the equals sign.
$TRADERS_AT_MIT_VIRTUALENV = path to the virtual environment that you created in step 1.
$TRADERS_AT_MIT_WEBSITE = path to the project root.

Try opening a new cmd and running “td” followed by “ts”. This should activate the environment and put you in the right directory.

13. IF USING WINDOWS: Download the winpy32 executable from http://www.lfd.uci.edu/~gohlke/pythonlibs/. Activate your environment by running "ts". Now run "pip install $EXECUTABLE" where $EXECUTABLE is the path to the .exe u just downloaded.
15. Once you have the environment activated (by running “ts”), run "pip install –r requirements.txt" from the project root.
16. Create a copy of settings_local_template.py in the project root and name it settings_local.py
17. Open settings_local.py and replace """NAME, EMAIL""" with your name and email in ADMINS. Make sure to put each in quotations since they're strings.
18. Run “python manage.py syncdb --migrate”.
19. Run “fab load_data”
20. Go to localhost:8000. You’re all set!


WINDOWS INSTALLATION PREP
1. If you do not have git installed, then install msysgit and add its bin as well as the mingw's bin folders to the path. Create a HOME environment variable pointing to home directory.
4. Create '/bin' directory in C:. Inside of it create the following lines with the content that's between the """."

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
5. cd into the bin directory and run cmd_autorun_install.cmd.
    
    
TYPICAL WORKFLOW
1. Open two terminals. In the first one run - "ts", "td", "python manage.py runserver". Leave the second for making commits.
3. Make whatever changes you need to.
4. Run "git add -A" or "git add <files to add>" to stage the files you changed.
5. Run "git commit -m '<commit message>'" to commit your changes.
6. Run "git push" to push the changes to staging.
7. Run "fab update" locally to update staging.