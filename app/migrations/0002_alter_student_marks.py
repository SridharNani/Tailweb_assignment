# Generated by Django 4.1.1 on 2022-09-20 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="student", name="Marks", field=models.PositiveIntegerField(),
        ),
    ]
