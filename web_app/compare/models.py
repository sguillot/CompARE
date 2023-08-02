from django.db import models

# Create your models here.
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.


class ModelNs(models.Model):
    id_model = models.AutoField(db_column='id_Model', primary_key=True)  # Field name made lowercase.
    dependenciesprimary = models.CharField(db_column='DependenciesPrimary', max_length=60, blank=True, null=True)  # Field name made lowercase.cd 
    dependenciessecondary = models.CharField(db_column='DependenciesSecondary', max_length=60, blank=True, null=True)  # Field name made lowercase.
    dependenciesdescription = models.TextField(db_column='DependenciesDescription',blank=True, null=True)  # Field name made lowercase.
    dependenciesreferences = models.TextField(db_column='DependenciesReferences', blank=True, null=True)

    class Meta:
        managed = True  
        db_table = 'model_ns'

class AssumptionsNs(models.Model):
    id_assumptions = models.AutoField(db_column='id_Assumptions', primary_key=True)  # Field name made lowercase.
    assumptionsprimary = models.CharField(db_column='AssumptionsPrimary', max_length=60, blank=True, null=True)  # Field name made lowercase.
    assumptionssecondary = models.CharField(db_column='AssumptionsSecondary', max_length=60, blank=True, null=True)  # Field name made lowercase.
    assumptionsdescription = models.TextField(db_column='AssumptionsDescription',blank=True, null=True)  # Field name made lowercase.
    assumptionsreferences = models.TextField(db_column='AssumptionsReferences', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'assumptions_ns'

class RefNs(models.Model):
    id_ref = models.AutoField(db_column='id_Ref', primary_key=True)  # Field name made lowercase.
    author = models.CharField(db_column='Author', max_length=30)  # Field name made lowercase.
    refyear = models.IntegerField(db_column='RefYear')  # Field name made lowercase.
    short = models.CharField(db_column='Short', max_length=50)  # Field name made lowercase.
    bibtex = models.TextField(db_column='Bibtex')  # Field name made lowercase.
    doi = models.TextField(db_column='DOI')  # Field name made lowercase.
    repositorydoi = models.CharField(db_column='RepositoryDOI', max_length=50, blank=True, null=True)  # Field name made lowercase.
    datalink = models.CharField(db_column='DataLink', max_length=70, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'ref_ns'


class NameNs(models.Model):
    id_name = models.AutoField(db_column='id_Name', primary_key=True)  # Field name made lowercase.
    namedb = models.CharField(db_column='NameDB', max_length=50)  # Field name made lowercase.
    classdb = models.CharField(db_column='ClassDB', max_length=50)  # Field name made lowercase.
    namesimbad = models.CharField(db_column='NameSimbad', max_length=50 ,blank=True,null=True)  # Field name made lowercase.
    classsimbad = models.CharField(db_column='ClassSimbad', max_length=50 ,blank=True, null=True)  # Field name made lowercase.
    ra = models.DecimalField(db_column='RA', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    declination = models.DecimalField(db_column='Declination', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    localisationfile = models.TextField(db_column='LocalisationFile', blank=True, null=True)  # Field name made lowercase.
    eventdate = models.DateField(db_column='EventDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'name_ns'




class MethodNs(models.Model):

    METHOD_CHOICES = [("Pulsar timing", "Pulsar timing"),
                      ("Thermal emission", "Thermal emission")
                       ]

    id_method = models.AutoField(db_column='id_Method', primary_key=True)  # Field name made lowercase.
    method = models.CharField(db_column='Method', max_length=25,choices=METHOD_CHOICES)  # Field name made lowercase.
    method_specific = models.TextField(db_column='Method_Specific')  # Field name made lowercase.
    #datadate = models.CharField(db_column='DataDate', max_length=70)  # Field name made lowercase.
    datadate = models.TextField(db_column='DataDate')  # Field name made lowercase.
    processinfinfo = models.TextField(db_column='ProcessinfInfo')  # Field name made lowercase.
   
    class Meta:
        managed = True
        db_table = 'method_ns'

class ConstrainNs(models.Model):

    CONSTRAIN_CHOICES = [("MCMC samples", "MCMC samples"),
                         ("Posterior samples", "Posterior samples"),
                         ("Quantiles", "Quantiles"),
                         ("mean +/- 1 sigma", "mean +/- 1 sigma"),
                         ('Probability distribution', 'Probability distribution'),
                         ('Chi2 contours', 'Chi2 contours')
                         ]

    CONSTRAIN_VAR = [("M", "M"),
                     ("R", "R"),
                     ("M-R", "M-R"),
                     ("F", "F"),
                     ("L", "L"),
                     ("M-L", "M-L")
                     ]

    id_constrain = models.AutoField(db_column='id_Constrain', primary_key=True)  # Field name made lowercase.
    constraintype = models.CharField(db_column='ConstrainType', max_length=30, choices=CONSTRAIN_CHOICES)  # Field name made lowercase.
    constrainvariable = models.CharField(db_column='constrainvariable',max_length=19, choices=CONSTRAIN_VAR)  # Field name made lowercase.
    constrainversion = models.IntegerField(db_column='ConstrainVersion',default=1)  # Field name made lowercase.
    

    class Meta:
        managed = True
        db_table = 'constrain_ns'

class Ns(models.Model):
    filename = models.CharField(db_column='FileName', primary_key=True, max_length=100)  # Field name made lowercase.
    filepath = models.TextField(db_column='FilePath')  # Field name made lowercase.
    id_ref = models.ForeignKey(RefNs, on_delete=models.CASCADE, db_column='id_ref', blank=True, null=True)
    id_name = models.ForeignKey(NameNs, on_delete=models.CASCADE, db_column='id_Name', blank=True, null=True)  # Field name made lowercase.
    id_method = models.ForeignKey(MethodNs, on_delete=models.CASCADE, db_column='id_Method', blank=True, null=True)  # Field name made lowercase.
    id_constrain = models.ForeignKey(ConstrainNs,on_delete=models.CASCADE, db_column='id_Constrain', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'ns'


class NsToModel(models.Model):
    id_ns_to_model = models.AutoField(db_column='id_ns_to_model', primary_key=True)  # Field name made lowercase.
    filename = models.ForeignKey(Ns, on_delete=models.CASCADE, db_column='FileName')  # Field name made lowercase.
    id_model = models.ForeignKey(ModelNs,on_delete=models.CASCADE, db_column='id_model') # Field name made lowercase. The composite primary key (id_Model, FileName) found, that is not supported. The first column is selected.

    class Meta:
        managed = True
        db_table = 'ns_to_model'
        constraints = [
            models.UniqueConstraint(fields=['filename','id_model'], name='unique_host_migration'),
        ]


class NsToAssumptions(models.Model):
    id_ns_to_assumptions = models.AutoField(db_column='id_ns_to_assumptions', primary_key=True)  # Field name made lowercase.
    filename = models.ForeignKey(Ns, on_delete=models.CASCADE, db_column='FileName')  # Field name made lowercase.
    id_assumptions = models.ForeignKey(AssumptionsNs,on_delete=models.CASCADE, db_column='id_assumptions')# Field name made lowercase. The composite primary key (id_Model, FileName) found, that is not supported. The first column is selected.

    class Meta:
        managed = True
        db_table = 'ns_to_assumptions'
        constraints = [
            models.UniqueConstraint(fields=['id_assumptions', 'filename'], name='unique_host_migration2'),
        ]















