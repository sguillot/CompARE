# Generated by Django 4.2 on 2023-04-12 10:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AssumptionsNs',
            fields=[
                ('id_assumptions', models.AutoField(db_column='id_Assumptions', primary_key=True, serialize=False)),
                ('assumptionsprimary', models.CharField(blank=True, db_column='AssumptionsPrimary', max_length=60, null=True)),
                ('assumptionssecondary', models.CharField(blank=True, db_column='AssumptionsSecondary', max_length=60, null=True)),
                ('assumptionsdescription', models.TextField(blank=True, db_column='AssumptionsDescription', null=True)),
            ],
            options={
                'db_table': 'assumptions_ns',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ConstrainNs',
            fields=[
                ('id_constrain', models.AutoField(db_column='id_Constrain', primary_key=True, serialize=False)),
                ('constraintype', models.CharField(choices=[('Likelihood', 'Lielihood'), ('MCMC samples', 'MCMC samples'), ('Confidence Interval', 'Confidence Interval')], db_column='ConstrainType', max_length=19)),
                ('constrainversion', models.IntegerField(db_column='ConstrainVersion')),
                ('constraindescription', models.TextField(db_column='ConstrainDescription')),
            ],
            options={
                'db_table': 'constrain_ns',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MethodNs',
            fields=[
                ('id_method', models.AutoField(db_column='id_Method', primary_key=True, serialize=False)),
                ('method', models.CharField(choices=[('Pulsar timing', 'Pulsar timing'), ('Thermal emission', 'Thermal emission'), ('Gravitational wave merger', 'Gravitational wave merger')], db_column='Method', max_length=25)),
                ('method_specific', models.TextField(db_column='Method_Specific')),
                ('datadate', models.CharField(blank=True, db_column='DataDate', max_length=70, null=True)),
                ('processinfinfo', models.TextField(blank=True, db_column='ProcessinfInfo', null=True)),
            ],
            options={
                'db_table': 'method_ns',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ModelNs',
            fields=[
                ('id_model', models.AutoField(db_column='id_Model', primary_key=True, serialize=False)),
                ('dependenciesprimary', models.CharField(blank=True, db_column='DependenciesPrimary', max_length=60, null=True)),
                ('dependenciessecondary', models.CharField(blank=True, db_column='DependenciesSecondary', max_length=60, null=True)),
                ('dependeciesdescription', models.TextField(blank=True, db_column='DependeciesDescription', null=True)),
            ],
            options={
                'db_table': 'model_ns',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='NameNs',
            fields=[
                ('id_name', models.AutoField(db_column='id_Name', primary_key=True, serialize=False)),
                ('namedb', models.CharField(db_column='NameDB', max_length=50)),
                ('classdb', models.CharField(db_column='ClassDB', max_length=50)),
                ('namesimbad', models.CharField(db_column='NameSimbad', max_length=50)),
                ('classsimbad', models.CharField(db_column='ClassSimbad', max_length=50)),
                ('ra', models.DecimalField(blank=True, db_column='RA', decimal_places=10, max_digits=20, null=True)),
                ('declination', models.DecimalField(blank=True, db_column='Declination', decimal_places=10, max_digits=20, null=True)),
                ('localisationfile', models.TextField(blank=True, db_column='LocalisationFile', null=True)),
                ('eventdate', models.DateField(blank=True, db_column='EventDate', null=True)),
            ],
            options={
                'db_table': 'name_ns',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Ns',
            fields=[
                ('filename', models.CharField(db_column='FileName', max_length=100, primary_key=True, serialize=False)),
                ('filepath', models.TextField(db_column='FilePath')),
            ],
            options={
                'db_table': 'ns',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='RefNs',
            fields=[
                ('id_ref', models.AutoField(db_column='id_Ref', primary_key=True, serialize=False)),
                ('author', models.CharField(db_column='Author', max_length=30)),
                ('refyear', models.IntegerField(db_column='RefYear')),
                ('short', models.CharField(db_column='Short', max_length=50)),
                ('bibtex', models.TextField(db_column='Bibtex')),
                ('doi', models.CharField(db_column='DOI', max_length=70)),
                ('repositorydoi', models.CharField(blank=True, db_column='RepositoryDOI', max_length=50, null=True)),
                ('datalink', models.CharField(blank=True, db_column='DataLink', max_length=70, null=True)),
            ],
            options={
                'db_table': 'ref_ns',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='NsToAssumptions',
            fields=[
                ('id_assumptions', models.OneToOneField(db_column='id_Assumptions', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='compare.assumptionsns')),
            ],
            options={
                'db_table': 'ns_to_assumptions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='NsToModel',
            fields=[
                ('id_model', models.OneToOneField(db_column='id_Model', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='compare.modelns')),
            ],
            options={
                'db_table': 'ns_to_model',
                'managed': False,
            },
        ),
    ]
