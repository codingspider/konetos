# Generated by Django 2.2 on 2020-12-25 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertise', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertisement',
            name='status',
            field=models.CharField(choices=[('1', 'Active'), ('2', 'Deactivate')], default=1, max_length=5),
        ),
    ]
