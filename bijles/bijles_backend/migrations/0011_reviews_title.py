# Generated by Django 4.0.3 on 2022-04-04 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bijles_backend', '0010_remove_matches_student_remove_matches_teacher_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviews',
            name='title',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]