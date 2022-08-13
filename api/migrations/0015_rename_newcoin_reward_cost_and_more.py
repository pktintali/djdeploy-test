# Generated by Django 4.0.3 on 2022-03-31 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_rename_savedcategories_userinterest'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reward',
            old_name='newCoin',
            new_name='cost',
        ),
        migrations.RenameField(
            model_name='reward',
            old_name='preCoin',
            new_name='duration',
        ),
        migrations.RemoveField(
            model_name='reward',
            name='discount',
        ),
        migrations.AddField(
            model_name='reward',
            name='description',
            field=models.CharField(default='description', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='reward',
            name='title',
            field=models.CharField(max_length=50),
        ),
    ]