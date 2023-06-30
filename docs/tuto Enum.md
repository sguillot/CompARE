# How to add a value to an ENUM
this tutorial is available for : 
* Method.method 
*  Constrain.constraintype 
* Constrain.constrainvariable

## Start MySQL and open the database

Start MySQL in interactive mode in a terminal

    mysql -u root -p
    # type your password

Select the database you want to use:
    
    show databases;
    use compare3;

## Alter Table 
First we are going to **modificate the database** . To add a variable at an **ENUM** we have to alter the table , herre the script :

    ALTER TABLE constrain_ns 
    MODIFY COLUMN constrainvariable 
    ENUM('R','M-R','R value+errors','New Value') NOT NULL;

The first line states which table will be modified, the second line which column will be modified, 
and the third line list the values.

If you want to check what are the values already existing you can display them with the command:

    SELECT SUBSTRING(COLUMN_TYPE,5)
	FROM information_schema.COLUMNS
	WHERE TABLE_SCHEMA='compare3' 
    AND TABLE_NAME='constrain_ns'
    AND COLUMN_NAME='constrainvariable';


## Alter the Django code for the application 

Go to the model.py page and change list that look like this :

    CONSTRAIN_VAR = [
	    ("R", "R"),
	    ("M-R", "M-R"),
	    ("R value+errors","R value+errors"),
	    ("New Value","New Value")
    ]

Add the new value (2 times) that  you added in the database 
	

