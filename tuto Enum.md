# How to add a value to an ENUM
this tutorial is available for : 
* Method.method 
*  Constrain.constraintype 
* Constrain.constrainvariable

## 1. Alter Table 
First we are going to **modificate the database** . To add a variable at an **ENUM** we have to alter the table , herre the script :

    ALTER TABLE constrain_ns 
    MODIFY COLUMN constrainvariable 
    ENUM('R','M-R','R value+errors','New Value') NOT NULL;

First line we choose what table we want to modify 

Second line we say what type of alter we do , and we choose the column of the table we want to modify 

Third line we put the enums with all the value 

If you want to check what are the values already existing you con put this select :

    SELECT SUBSTRING(COLUMN_TYPE,5)
	FROM information_schema.COLUMNS
	WHERE TABLE_SCHEMA='compare3' 
    AND TABLE_NAME='constrain_ns'
    AND COLUMN_NAME='constrainvariable'

(only the 2 last line can be changed )

## 2.The application 

Go to the model.py page and change list that look like this :

    CONSTRAIN_VAR = [
	    ("R", "R"),
	    ("M-R", "M-R"),
	    ("R value+errors","R value+errors"),
	    ("New Value","New Value")
    ]

Add the new value (2 times) that  you added in the database 
	

