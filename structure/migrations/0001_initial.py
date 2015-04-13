# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ligand', '0002_auto_20150225_1441'),
        ('common', '0002_auto_20150328_1656'),
        ('protein', '0002_auto_20150316_1232'),
    ]

    operations = [
        migrations.CreateModel(
            name='Structure',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('preferred_chain', models.CharField(max_length=20)),
                ('resolution', models.DecimalField(decimal_places=3, max_digits=5)),
                ('pdb_publication_date', models.DateField()),
                ('endogenous_ligand', models.ForeignKey(related_name='endogenous_ligand', null=True, to='ligand.Ligand')),
                ('pdb_code', models.ForeignKey(to='common.WebLink')),
                ('protein', models.ForeignKey(to='protein.Protein')),
                ('publication', models.ForeignKey(to='common.Publication')),
            ],
            options={
                'db_table': 'structure',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='StructureStabilizingAgent',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('slug', models.SlugField(max_length=20)),
            ],
            options={
                'db_table': 'structure_stabilizing_agent',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='StructureType',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('slug', models.SlugField(max_length=20)),
                ('description', models.TextField()),
            ],
            options={
                'db_table': 'structure_type',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='structure',
            name='stabilizing_agents',
            field=models.ManyToManyField(null=True, to='structure.StructureStabilizingAgent'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='structure',
            name='structure_type',
            field=models.ForeignKey(to='structure.StructureType'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='structure',
            name='xray_ligand',
            field=models.ForeignKey(related_name='xray_ligand', null=True, to='ligand.Ligand'),
            preserve_default=True,
        ),
    ]
