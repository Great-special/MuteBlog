# Generated by Django 4.0.6 on 2022-12-08 00:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BlogPost', '0004_alter_blogmodel_category'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BlogCategory',
        ),
    ]