# Generated by Django 3.2.8 on 2021-10-28 10:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_remove_project_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='rating',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='api.rating'),
        ),
    ]