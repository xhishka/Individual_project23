# Generated by Django 4.1.3 on 2023-01-24 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_gifts_delete_gift'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gifts',
            name='task',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
