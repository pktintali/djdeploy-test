# Generated by Django 4.0.3 on 2022-04-04 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0016_alter_user_last_seen_categoryrequest_reportfact'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categoryrequest',
            name='isCompleted',
        ),
        migrations.AddField(
            model_name='categoryrequest',
            name='status',
            field=models.IntegerField(default=0),
        ),
    ]
