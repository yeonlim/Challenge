# Generated by Django 3.2 on 2021-08-27 17:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('community', '0003_alter_comment_community_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='community',
            name='writer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='account.customuser'),
            preserve_default=False,
        ),
    ]