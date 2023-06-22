# Generated by Django 4.2 on 2023-05-24 07:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('compare', '0002_alter_assumptionsns_options_and_more'),
    ]

    """ operations = [
        migrations.AddField(
            model_name='constrainns',
            name='constrainvariable',
            field=models.TextField(choices=[('R', 'R'), ('M-R', 'M-R')], db_column='constrainvariable', default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ns',
            name='id_constrain',
            field=models.ForeignKey(blank=True, db_column='id_Constrain', null=True, on_delete=django.db.models.deletion.CASCADE, to='compare.constrainns'),
        ),
        migrations.AddField(
            model_name='ns',
            name='id_method',
            field=models.ForeignKey(blank=True, db_column='id_Method', null=True, on_delete=django.db.models.deletion.CASCADE, to='compare.methodns'),
        ),
        migrations.AddField(
            model_name='ns',
            name='id_name',
            field=models.ForeignKey(blank=True, db_column='id_Name', null=True, on_delete=django.db.models.deletion.CASCADE, to='compare.namens'),
        ),
        migrations.AddField(
            model_name='ns',
            name='id_ref',
            field=models.ForeignKey(blank=True, db_column='id_ref', null=True, on_delete=django.db.models.deletion.CASCADE, to='compare.refns'),
        ),
        migrations.AddField(
            model_name='nstoassumptions',
            name='filename',
            field=models.ForeignKey(db_column='FileName', default=0, on_delete=django.db.models.deletion.CASCADE, to='compare.ns'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='nstoassumptions',
            name='id_ns_to_assumptions',
            field=models.AutoField(db_column='id_ns_to_assumptions', default=0, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='nstomodel',
            name='filename',
            field=models.ForeignKey(db_column='FileName', default=0, on_delete=django.db.models.deletion.CASCADE, to='compare.ns'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='nstomodel',
            name='id_ns_to_model',
            field=models.AutoField(db_column='id_ns_to_model', default=0, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='assumptionsns',
            name='assumptionsdescription',
            field=models.TextField(db_column='AssumptionsDescription', default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='methodns',
            name='datadate',
            field=models.CharField(db_column='DataDate', default=0, max_length=70),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='methodns',
            name='processinfinfo',
            field=models.TextField(db_column='ProcessinfInfo', default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='modelns',
            name='dependeciesdescription',
            field=models.TextField(db_column='DependeciesDescription', default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='namens',
            name='classsimbad',
            field=models.CharField(blank=True, db_column='ClassSimbad', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='namens',
            name='namesimbad',
            field=models.CharField(blank=True, db_column='NameSimbad', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='nstoassumptions',
            name='id_assumptions',
            field=models.ForeignKey(db_column='id_assumptions', on_delete=django.db.models.deletion.CASCADE, to='compare.assumptionsns'),
        ),
        migrations.AlterField(
            model_name='nstomodel',
            name='id_model',
            field=models.ForeignKey(db_column='id_model', on_delete=django.db.models.deletion.CASCADE, to='compare.modelns'),
        ),
        migrations.AlterField(
            model_name='refns',
            name='doi',
            field=models.TextField(db_column='DOI'),
        ),
        migrations.AddConstraint(
            model_name='nstoassumptions',
            constraint=models.UniqueConstraint(fields=('id_assumptions', 'filename'), name='unique_host_migration2'),
        ),
        migrations.AddConstraint(
            model_name='nstomodel',
            constraint=models.UniqueConstraint(fields=('filename', 'id_model'), name='unique_host_migration'),
        ),
    ]
"""