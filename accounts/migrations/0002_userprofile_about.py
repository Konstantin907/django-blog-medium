# Generated by Django 5.1.7 on 2025-04-05 17:43

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='about',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
