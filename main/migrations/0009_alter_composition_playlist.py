# Generated by Django 4.1.2 on 2022-10-30 14:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_alter_composition_playlist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='composition',
            name='playlist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.playlist'),
        ),
    ]
