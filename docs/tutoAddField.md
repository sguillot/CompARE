# How to add a field in the database
In this tutorial you will see how to add the field *Caveats References in the database* and the application **CompARE**

## Adding the field to the database 

 ### 1. Connect to the database 
 ### 2.  Alter the table **model_ns** to add the field
	>     ALTER TABLE model_ns
	>     ADD COLUMN CaveatsReferences TEXT ;
First line ,  we choose what table of the database we want to alter 
List of the tables of CompAre :
 - ref_ns
 - name_ns
 - method_ns
 - constrain_ns
 - ns
 - model_ns
 - assumptions_ns
 - ns_to_model
 - ns_to_assumptions

Second line , we choose what type of **ALTER** we want to do , here **ADD**.
List of the possible ALTER  :
 - ADD
 - RENAME
 - MODIFY
 - DROP

After that we put the name off the field we want to add , here **CaveatsReferences**.

Finally , we set the type of the field and the contraints, here **Text** , it will be a string of indefinite size.
List of the types of a MySQL Database :

 - Text
 - Varchar
 - Enum
 - Int
 - Float
 - Date
 - Year
 - [more and explanation of the types](https://www.w3schools.com/mysql/mysql_datatypes.asp)  

### 3. Add the new field to the model field of the Django Project .

		

	class ModelNs(models.Model):
		id_model = models.AutoField(db_column='id_Model', primary_key=True)  # Field name made lowercase.
		dependenciesprimary = models.CharField(db_column='DependenciesPrimary', max_length=60,blank=True, null=True)  # Field name made lowercase.cd 
		dependenciessecondary = models.CharField(db_column='DependenciesSecondary', max_length=60,blank=True, null=True)  # Field name made lowercase.
		dependenciesdescription = models.TextField(db_column='DependenciesDescription',blank=True,null=True)  # Field name made lowercase.
		caveatsReferences = models.TextField(db_column='CaveatsReferences',blank=True, null=True)
		 
		    class Meta:
		    managed = True  
		    db_table = 'model_ns'

    
### 4. Adding the field in the Page detail to see this new field.
In the file **detail.html** of the folder **templates/compare**

 1. Go to the div "**divmodel**"
 2. Add in the for loop :
`{{mo.id_model.caveatsReferences}}`
 3. Add the table header :

		 <th>Caveats References</th>

### 5.Adding the field in the insert page to allow user to add this field 
In the file **insert.html** of the folder **templates/compare**

 1. Go the div "**modelcontent**"
 2. Add the input in reference with the type of the field  , here we have a **Text Field** so we put a **Textarea** :

		 <label>Caveats References</label> 
		 <textarea name="MocaveatsReferences"  id="MocaveatsReferences" placeholder="Caveats References"></textarea>

In the file **scriptAdd.js** of the folder **static/compare**

 1. Go to the function **inTableMod()**
 2. Add a varibale to get the value of the input :
 
	    MoCaveatsRef = document.getElementById('MocaveatsReferences').value
3. Add the value to the table of Models :

	    let MoCaveats = row.insertCell(3)
	    MoCaveats.innerHTML = MoCaveatsRef
	    
4. Reset the input field :

	    document.getElementById('MocaveatsReferences').value = ''

In the file **views.py**  go to the **insert_data** function 

 1. Go to the this **if condition**:
	
	    if(len(insert['assumptions']) > 0):
	
 2. Add the verification of null values in the for loop :
	   
	     if(len(insert['model'][mod][3]) < 1 ):
		    insert['model'][mod][3] = None
		    

 3. Add the verification that this model does not already exist in the database:

	    caveatsReferences = insert['model'][mod][3]

	You will have this :
	
		if (ModelNs.objects.filter(dependenciesprimary = insert['model'][mod][0], dependenciessecondary = insert['model'][mod][1],dependenciesdescription = insert['model'][mod][2],caveatsReferences = insert['model'][mod][3])):

	4.Add the same things to the select and create query 
	

		caveatsReferences = insert['model'][mod][3]
			
	    
	You will have this in case this model already exist :

	    modelId=ModelNs.objects.filter(dependenciesprimary = insert['model'][mod][0], dependenciessecondary = insert['model'][mod][1],dependenciesdescription = insert['model'][mod][2],caveatsReferences = insert['model'][mod][3])


	You will have this in case this model does not exist :
		
	    model = ModelNs(dependenciesprimary = insert['model'][mod][0], dependenciessecondary = insert['model'][mod][1],dependenciesdescription = insert['model'][mod][2],caveatsReferences = insert['model'][mod][3])


### 6. Adding the field in the automatic insertion of the insert page
In the file **views.py** go to the **insert_data** function

 1. Go to :	
	 
		 `for i in range(1,len(d)):`

2. Add this to get the values of the file in a list :

	    listmocaveats = list(d['CaveatReferences'])[i]
		listmocav = listmocaveats.split(",")
		 
 3. Go to:
	
		for j in range(len(listmo)):
3. Add this to get the value of each model of the list :

		`modeldesc = listmodesc[j]`

4. Add the verification , we put Null if there is no data :

	    if len(mocaveats)<1:
		    mocaveats = None
5. Add the verification that this model does not already exist in the database:
	

	    caveatsReferences=mocaveats)
	    
	  You will have this :
	
	    if(ModelNs.objects.filter(dependenciesprimary=modelpri,dependenciessecondary=modelsec,dependenciesdescription=modeldesc)):
	    			    idMo = ModelNs.objects.filter(dependenciesprimary=modelpri,dependenciessecondary=modelsec,dependenciesdescription=modeldesc)
6. Add the same things to the create query :

	    modelN = ModelNs(dependenciesprimary=modelpri ,dependenciessecondary=modelsec ,dependenciesdescription=modeldesc,caveatsReferences=mocaveats)

### 6. Adding the field in the modification page
In the file **modify.html** of the folder **templates/compare**

 1. Go to the div **modify-model**
 2. Add the input field:
 
		<label>Caveats References</label> 
		 <textarea  name="MocaveatsReferences"  class="method{{i.id_model}}"placeholder="{{i.caveatsReferences}}" disabled>{{i.caveatsReferences}}</textarea>
In the file **views.py** go to the **modify** function
1. Go to the condition of model:

	    if  'model'  in request.POST:
2. Get the data :
 
	    depCav = request.POST.get('MocaveatsReferences')

3. Add the verification , we put Null if there is no data :

	    if len(depCav)<1:
		    depCav = None
4. Add this in the update condition to update the model:
 
	    model.caveatsReferences = depCav
 5. Add the verification that this model does not already exist in the database:
		 
	    caveatsReferences=depCav
	You will have this :
	
	    if(ModelNs.objects.filter(dependenciesprimary=depP, dependenciessecondary=depS, dependenciesdescription=depD,caveatsReferences=depCav)):
5. Add the same things to the create query :

	    modelExist = ModelNs.objects.filter(dependenciesprimary=depP, dependenciessecondary=depS, dependenciesdescription=depD,caveatsReferences=depCav)
	    
6. Same things for the else statement :
							
		`model=ModelNs(dependenciesprimary=depP,dependenciessecondary=depS,dependenciesdescription=depD,caveatsReferences=depCav)`

 
 
	    

<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE2NDAyNzkwMzNdfQ==
-->
