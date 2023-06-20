
# How to install the project in local 

 ## 1. Prendre le projet depuis git (pull ?)
 ## 2.Create a virtual environement 
 

 ### 1. make sure you have python installed
 in a terminal :

    python --version

### 2. Go to the folder of the project 

### 3. Create a virtual environnement
in a terminal :
	
    python -m venv venv   
Activate the virtual environment that you created


    .\venv\Scripts\activate 

   
### 4. Install the librairies 
in a terminal :

    pip install -r .\requirementsDjango.txt   


### 5.Change the settings
Go to the file **web_app/web_app/settings.py** At the line (75) :

If you don't have password to your local mysql database put this settings:


<img width="186" alt="image" src="https://github.com/sguillot/CompARE/assets/122777194/d35714d9-42ad-49e7-91f5-11637d7a882c">


NAME = database Name

HOST = Server address (here local)

USER = Mysql Username

PASSWORD = Mysql Password

PORT = Mysql Port (default used by mysql is 3306)



### 6. Run the application 
from vscode : 


<img width="124" alt="gsfdgd" src="https://github.com/sguillot/CompARE/assets/122777194/e9a146d8-cce4-477b-8a80-2708743ab7a8">


in a terminal :

    cd .\web_app\

    py manage.py runserver

`


`

	   
	


