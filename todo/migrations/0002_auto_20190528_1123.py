# Generated by Django 2.2.1 on 2019-05-28 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todoitem',
            name='context',
            field=models.TextField(),
        ),
    ]
