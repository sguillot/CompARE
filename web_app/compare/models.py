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
    # Field names are made lowercase
    id_model = models.AutoField(db_column='id_Model', primary_key=True)
    dependenciesprimary = models.CharField(db_column='DependenciesPrimary', max_length=60, blank=True, null=True)
    dependenciessecondary = models.CharField(db_column='DependenciesSecondary', max_length=60, blank=True, null=True)
    dependenciesdescription = models.TextField(db_column='DependenciesDescription', blank=True, null=True)
    dependenciesreferences = models.TextField(db_column='DependenciesReferences', blank=True, null=True)

    class Meta:
        managed = True  
        db_table = 'model_ns'


class AssumptionsNs(models.Model):
    # Field names are made lowercase
    id_assumptions = models.AutoField(db_column='id_Assumptions', primary_key=True)
    assumptionsprimary = models.CharField(db_column='AssumptionsPrimary', max_length=60, blank=True, null=True)
    assumptionssecondary = models.CharField(db_column='AssumptionsSecondary', max_length=60, blank=True, null=True)
    assumptionsdescription = models.TextField(db_column='AssumptionsDescription', blank=True, null=True)
    assumptionsreferences = models.TextField(db_column='AssumptionsReferences', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'assumptions_ns'


class RefNs(models.Model):
    # Field names are made lowercase
    id_ref = models.AutoField(db_column='id_Ref', primary_key=True)
    author = models.CharField(db_column='Author', max_length=30)
    refyear = models.IntegerField(db_column='RefYear')
    short = models.CharField(db_column='Short', max_length=50)
    bibtex = models.TextField(db_column='Bibtex')
    doi = models.TextField(db_column='DOI')
    repositorydoi = models.CharField(db_column='RepositoryDOI', max_length=50, blank=True, null=True)
    datalink = models.CharField(db_column='DataLink', max_length=256, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ref_ns'


class NameNs(models.Model):
    # Field names are made lowercase
    id_name = models.AutoField(db_column='id_Name', primary_key=True)
    namedb = models.CharField(db_column='NameDB', max_length=50)
    classdb = models.CharField(db_column='ClassDB', max_length=50)
    namesimbad = models.CharField(db_column='NameSimbad', max_length=50, blank=True, null=True)
    classsimbad = models.CharField(db_column='ClassSimbad', max_length=50, blank=True, null=True)
    ra = models.DecimalField(db_column='RA', max_digits=20, decimal_places=10, blank=True, null=True)
    declination = models.DecimalField(db_column='Declination', max_digits=20, decimal_places=10, blank=True, null=True)
    localisationfile = models.TextField(db_column='LocalisationFile', blank=True, null=True)
    eventdate = models.DateField(db_column='EventDate', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'name_ns'


class MethodNs(models.Model):

    METHOD_CHOICES = [("Pulsar timing", "Pulsar timing"),
                      ("Thermal emission", "Thermal emission"),
                      ("Phase-resolved thermal emission", "Phase-resolved thermal emission"),
                      ]

    # Field names are made lowercase
    id_method = models.AutoField(db_column='id_Method', primary_key=True)
    method = models.CharField(db_column='Method', max_length=40, choices=METHOD_CHOICES)
    method_specific = models.TextField(db_column='Method_Specific')
    datadate = models.TextField(db_column='DataDate')
    processinfinfo = models.TextField(db_column='ProcessinfInfo')
   
    class Meta:
        managed = True
        db_table = 'method_ns'


class ConstrainNs(models.Model):

    CONSTRAIN_CHOICES = [("MCMC samples", "MCMC samples"),
                         ("Posterior samples", "Posterior samples"),
                         ("Quantiles", "Quantiles"),
                         ("mean +/- 1 sigma", "mean +/- 1 sigma"),
                         ('Probability distribution', 'Probability distribution'),
                         ('Chi2 contours', 'Chi2 contours'),
                         ]

    CONSTRAIN_VAR = [("M", "M"),
                     ("R", "R"),
                     ("M-R", "M-R"),
                     ("F", "F"),
                     ("L", "L"),
                     ("M-L", "M-L"),
                     ]

    # Field names are made lowercase
    id_constrain = models.AutoField(db_column='id_Constrain', primary_key=True)
    constraintype = models.CharField(db_column='ConstrainType', max_length=30, choices=CONSTRAIN_CHOICES)
    constrainvariable = models.CharField(db_column='constrainvariable', max_length=19, choices=CONSTRAIN_VAR)
    constrainversion = models.IntegerField(db_column='ConstrainVersion', default=1)

    class Meta:
        managed = True
        db_table = 'constrain_ns'


class Ns(models.Model):
    # Field names are made lowercase
    filename = models.CharField(db_column='FileName', primary_key=True, max_length=100)
    filepath = models.TextField(db_column='FilePath')
    id_ref = models.ForeignKey(RefNs, on_delete=models.CASCADE, db_column='id_ref', blank=True, null=True)
    id_name = models.ForeignKey(NameNs, on_delete=models.CASCADE, db_column='id_Name', blank=True, null=True)
    id_method = models.ForeignKey(MethodNs, on_delete=models.CASCADE, db_column='id_Method', blank=True, null=True)
    id_constrain = models.ForeignKey(ConstrainNs, on_delete=models.CASCADE, db_column='id_Constrain', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ns'


class NsToModel(models.Model):
    # Field names are made lowercase
    id_ns_to_model = models.AutoField(db_column='id_ns_to_model', primary_key=True)
    filename = models.ForeignKey(Ns, on_delete=models.CASCADE, db_column='FileName')
    id_model = models.ForeignKey(ModelNs, on_delete=models.CASCADE, db_column='id_model')

    class Meta:
        managed = True
        db_table = 'ns_to_model'
        constraints = [models.UniqueConstraint(fields=['filename', 'id_model'], name='unique_host_migration')]


class NsToAssumptions(models.Model):
    id_ns_to_assumptions = models.AutoField(db_column='id_ns_to_assumptions', primary_key=True)
    filename = models.ForeignKey(Ns, on_delete=models.CASCADE, db_column='FileName')
    id_assumptions = models.ForeignKey(AssumptionsNs, on_delete=models.CASCADE, db_column='id_assumptions')

    class Meta:
        managed = True
        db_table = 'ns_to_assumptions'
        constraints = [models.UniqueConstraint(fields=['id_assumptions', 'filename'], name='unique_host_migration2')]
