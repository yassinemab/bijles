# Generated by Django 4.0.3 on 2022-04-04 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bijles_backend', '0011_reviews_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profiles',
            name='biography',
            field=models.CharField(blank=True, default=None, max_length=300, null=True),
        ),
    ]