# Generated by Django 4.0.6 on 2022-12-07 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BlogPost', '0002_alter_blogmodel_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogmodel',
            name='image',
            field=models.ImageField(upload_to='blogPost/'),
        ),
    ]
