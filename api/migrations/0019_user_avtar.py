# Generated by Django 4.0.3 on 2022-04-06 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0018_fact_isad'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avtar',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
