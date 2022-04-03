# Generated by Django 4.0.3 on 2022-04-02 21:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bijles_backend', '0004_alter_profiles_physical_alter_users_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='profile',
        ),
        migrations.AddField(
            model_name='profiles',
            name='user',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='bijles_backend.users'),
        ),
    ]