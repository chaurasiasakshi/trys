# Generated by Django 4.2.3 on 2023-09-01 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profileapp', '0002_alter_promodel_message_alter_promodel_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='promodel',
            name='email',
            field=models.CharField(max_length=255),
        ),
    ]
