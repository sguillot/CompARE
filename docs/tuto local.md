
# How to install and use the database and interface locally

## Install MySQL and create the database

Installation can be done from the MySQL page, or from `brew` (for Mac users, see https://flaviocopes.com/mysql-how-to-install/). 
Installation from Conda might be possible, but I couldn't get it to work.

Define your SQL localhost root password:

    ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'pass1234';

Create the database from the existing `database_compare3.sql` file. Note that `database_draft.sql` is outdated and will not work with the current version of the code (python and html). It will prompt your password: 'pass1234' in the example above)

    mysql -u root -p < scripts/database/database_compare3.sql

Add the environment variable `PWD_MYSQL` with your password (e.g. `pass1234` in the example above) with the following line in your `.bashrc` or `.bash_profile`.

    export PWD_MYSQL="pass1234"


## Clone the CompARE project from GitHub.
 
    git clone https://github.com/sguillot/CompARE

## Create a virtual environment (venv or conda) and activate it
	
    python -m venv venv
    .\venv\Scripts\activate 

or 

    conda create --name compare 
    conda activate compare
   
### Install the required packaged

    pip install -r .\requirementsDjango.txt   

If this does not work, try installing individually the packages listed in `requirementsDjango.txt`

[//]: # (### Change the settings)

[//]: # (Go to the file **web_app/web_app/settings.py** At the line &#40;75&#41; :)

[//]: # ()
[//]: # (If you don't have password to your local mysql database put this settings:)

[//]: # ()
[//]: # (<img width="186" alt="image" src="https://github.com/sguillot/CompARE/assets/122777194/d35714d9-42ad-49e7-91f5-11637d7a882c">)

[//]: # ()
[//]: # (NAME = database Name)

[//]: # ()
[//]: # (HOST = Server address &#40;here local&#41;)

[//]: # ()
[//]: # (USER = Mysql Username)

[//]: # ()
[//]: # (PASSWORD = Mysql Password)

[//]: # ()
[//]: # (PORT = Mysql Port &#40;default used by mysql is 3306&#41;)



### Run the web app server and open the web app interface

In a terminal :

    cd web_app/

    python manage.py runserver

Open the following address in a web browser

    http://127.0.0.1:8000/
