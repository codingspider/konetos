# Generated by Django 2.2 on 2020-12-27 15:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('chanel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(null=True)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('profile', models.ImageField(blank=True, null=True, upload_to='channel/profile/')),
                ('cover', models.ImageField(blank=True, null=True, upload_to='channel/cover/')),
                ('status', models.CharField(choices=[('1', 'Active'), ('2', 'Deactivate')], default=1, max_length=5)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
