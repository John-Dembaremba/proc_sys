# Generated by Django 3.0.8 on 2021-05-20 13:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0003_auto_20210519_1237'),
    ]

    operations = [
        migrations.RenameField(
            model_name='apply',
            old_name='created_at',
            new_name='applied',
        ),
    ]