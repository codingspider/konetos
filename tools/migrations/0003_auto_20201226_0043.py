# Generated by Django 2.2 on 2020-12-25 18:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tools', '0002_auto_20201226_0034'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='autofriend',
            name='user_id',
        ),
        migrations.RemoveField(
            model_name='autogroupjoin',
            name='user_id',
        ),
        migrations.RemoveField(
            model_name='autopagelike',
            name='user_id',
        ),
        migrations.AddField(
            model_name='autofriend',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='autogroupjoin',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='autopagelike',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]