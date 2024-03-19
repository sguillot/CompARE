# Generated by Django 5.0.3 on 2024-03-19 07:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compare', '0005_alter_constrainns_constrainvariable'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='constrainns',
            name='constraindescription',
        ),
        migrations.RemoveField(
            model_name='ns',
            name='filepath',
        ),
        migrations.AddField(
            model_name='assumptionsns',
            name='assumptionsreferences',
            field=models.TextField(blank=True, db_column='AssumptionsReferences', null=True),
        ),
        migrations.AddField(
            model_name='constrainns',
            name='constrainvariable',
            field=models.CharField(choices=[('M', 'M'), ('R', 'R'), ('M-R', 'M-R'), ('F', 'F'), ('L', 'L'), ('M-L', 'M-L')], db_column='constrainvariable', default=0, max_length=19),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='modelns',
            name='dependenciesreferences',
            field=models.TextField(blank=True, db_column='DependenciesReferences', null=True),
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
            model_name='constrainns',
            name='constraintype',
            field=models.CharField(choices=[('MCMC samples', 'MCMC samples'), ('Posterior samples', 'Posterior samples'), ('Quantiles', 'Quantiles'), ('mean +/- 1 sigma', 'mean +/- 1 sigma'), ('Probability distribution', 'Probability distribution'), ('Chi2 contours', 'Chi2 contours')], db_column='ConstrainType', max_length=30),
        ),
        migrations.AlterField(
            model_name='constrainns',
            name='constrainversion',
            field=models.IntegerField(db_column='ConstrainVersion', default=1),
        ),
        migrations.AlterField(
            model_name='methodns',
            name='datadate',
            field=models.TextField(db_column='DataDate', default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='methodns',
            name='method',
            field=models.CharField(choices=[('Pulsar timing', 'Pulsar timing'), ('Thermal emission', 'Thermal emission'), ('Phase-resolved thermal emission', 'Phase-resolved thermal emission')], db_column='Method', max_length=40),
        ),
        migrations.AlterField(
            model_name='methodns',
            name='processinfinfo',
            field=models.TextField(db_column='ProcessinfInfo', default=0),
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
            name='datalink',
            field=models.CharField(blank=True, db_column='DataLink', max_length=256, null=True),
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
