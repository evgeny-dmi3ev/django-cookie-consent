# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-01-21 03:29
from __future__ import unicode_literals

import aldryn_common.admin_fields.sortedm2m
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0020_old_tree_cleanup'),
        ('cookie_consent', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CookieConsentPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='cookie_consent_cookieconsentplugin', serialize=False, to='cms.CMSPlugin')),
                ('groups', aldryn_common.admin_fields.sortedm2m.SortedM2MModelField(blank=True, help_text='Select and arrange specific cookie groups, or, leave blank to select all.', to='cookie_consent.CookieGroup')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]