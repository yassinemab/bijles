# Generated by Django 4.0.3 on 2022-04-02 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bijles_backend', '0003_alter_profiles_physical'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profiles',
            name='physical',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]