# Generated by Django 4.1.2 on 2022-11-07 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_alter_composition_options_composition_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='composition',
            name='cover_image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]