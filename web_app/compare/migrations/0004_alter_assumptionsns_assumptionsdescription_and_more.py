# Generated by Django 4.2 on 2023-05-24 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compare', '0003_constrainns_constrainvariable_ns_id_constrain_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assumptionsns',
            name='assumptionsdescription',
            field=models.TextField(blank=True, db_column='AssumptionsDescription', null=True),
        ),
        migrations.AlterField(
            model_name='modelns',
            name='dependenciesdescription',
            field=models.TextField(blank=True, db_column='DependenciesDescription', null=True),
        ),
    ]
