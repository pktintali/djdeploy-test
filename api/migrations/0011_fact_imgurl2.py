# Generated by Django 4.0.3 on 2022-03-24 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_fact_desc_fact_ref'),
    ]

    operations = [
        migrations.AddField(
            model_name='fact',
            name='imgURL2',
            field=models.URLField(blank=True, null=True),
        ),
    ]
