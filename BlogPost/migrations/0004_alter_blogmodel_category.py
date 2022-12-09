# Generated by Django 4.0.6 on 2022-12-08 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BlogPost', '0003_alter_blogmodel_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogmodel',
            name='category',
            field=models.CharField(choices=[('life-style', 'LIFESTYLE'), ('journey', 'JOURNEY'), ('inspiration', 'INSPIRATION')], max_length=125),
        ),
    ]