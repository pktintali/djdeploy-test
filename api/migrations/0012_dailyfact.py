# Generated by Django 4.0.3 on 2022-03-28 05:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_fact_imgurl2'),
    ]

    operations = [
        migrations.CreateModel(
            name='DailyFact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('fact', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.fact')),
            ],
        ),
    ]
