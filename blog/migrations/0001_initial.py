# Generated by Django 2.2 on 2020-12-24 06:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, null=True)),
                ('slug', models.CharField(blank=True, max_length=255, null=True)),
                ('short_description', models.TextField(null=True)),
                ('description', models.TextField(null=True)),
                ('thumbnail', models.ImageField(null=True, upload_to='blog/')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('likes', models.IntegerField(blank=True, default=0, null=True)),
                ('visit', models.IntegerField(blank=True, default=0, null=True)),
                ('created_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]