# Generated by Django 4.2.3 on 2023-07-09 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('policyholder', '0004_policymodel_is_selected'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='policymodel',
            name='IS_selected',
        ),
        migrations.AddField(
            model_name='policymodel',
            name='iS_selected',
            field=models.CharField(choices=[('Not Selected', 'Not Selected'), ('Selected', 'Selected')], default='Not Selected', max_length=255),
        ),
    ]