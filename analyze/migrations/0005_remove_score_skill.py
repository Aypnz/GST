# Generated by Django 2.2.7 on 2019-11-15 21:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('analyze', '0004_score_skill'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='score',
            name='skill',
        ),
    ]