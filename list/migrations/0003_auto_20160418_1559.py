# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-18 15:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0002_auto_20160418_1537'),
    ]

    operations = [
        migrations.RenameField(
            model_name='my_contacts',
            old_name='first_name',
            new_name='first',
        ),
        migrations.RenameField(
            model_name='my_contacts',
            old_name='last_name',
            new_name='last',
        ),
    ]