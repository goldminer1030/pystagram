# Generated by Django 2.0.3 on 2018-03-20 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='content',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
    ]