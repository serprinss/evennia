# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-01-28 18:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scripts', '0011_remove_scriptdb_db_player'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scriptdb',
            name='db_account',
            field=models.ForeignKey(blank=True, help_text='the account to store this script on (should not be set if db_obj is set)', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='scripted account'),
        ),
        migrations.AlterField(
            model_name='scriptdb',
            name='db_attributes',
            field=models.ManyToManyField(help_text='attributes on this object. An attribute can hold any pickle-able python object (see docs for special cases).', to='typeclasses.Attribute'),
        ),
        migrations.AlterField(
            model_name='scriptdb',
            name='db_date_created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='creation date'),
        ),
        migrations.AlterField(
            model_name='scriptdb',
            name='db_desc',
            field=models.CharField(blank=True, max_length=255, verbose_name='desc'),
        ),
        migrations.AlterField(
            model_name='scriptdb',
            name='db_interval',
            field=models.IntegerField(default=-1, help_text='how often to repeat script, in seconds. -1 means off.', verbose_name='interval'),
        ),
        migrations.AlterField(
            model_name='scriptdb',
            name='db_is_active',
            field=models.BooleanField(default=False, verbose_name='script active'),
        ),
        migrations.AlterField(
            model_name='scriptdb',
            name='db_key',
            field=models.CharField(db_index=True, max_length=255, verbose_name='key'),
        ),
        migrations.AlterField(
            model_name='scriptdb',
            name='db_lock_storage',
            field=models.TextField(blank=True, help_text="locks limit access to an entity. A lock is defined as a 'lock string' on the form 'type:lockfunctions', defining what functionality is locked and how to determine access. Not defining a lock means no access is granted.", verbose_name='locks'),
        ),
        migrations.AlterField(
            model_name='scriptdb',
            name='db_obj',
            field=models.ForeignKey(blank=True, help_text='the object to store this script on, if not a global script.', null=True, on_delete=django.db.models.deletion.CASCADE, to='objects.ObjectDB', verbose_name='scripted object'),
        ),
        migrations.AlterField(
            model_name='scriptdb',
            name='db_persistent',
            field=models.BooleanField(default=False, verbose_name='survive server reboot'),
        ),
        migrations.AlterField(
            model_name='scriptdb',
            name='db_repeats',
            field=models.IntegerField(default=0, help_text='0 means off.', verbose_name='number of repeats'),
        ),
        migrations.AlterField(
            model_name='scriptdb',
            name='db_start_delay',
            field=models.BooleanField(default=False, help_text='pause interval seconds before starting.', verbose_name='start delay'),
        ),
        migrations.AlterField(
            model_name='scriptdb',
            name='db_tags',
            field=models.ManyToManyField(help_text='tags on this object. Tags are simple string markers to identify, group and alias objects.', to='typeclasses.Tag'),
        ),
        migrations.AlterField(
            model_name='scriptdb',
            name='db_typeclass_path',
            field=models.CharField(help_text="this defines what 'type' of entity this is. This variable holds a Python path to a module with a valid Evennia Typeclass.", max_length=255, null=True, verbose_name='typeclass'),
        ),
    ]
