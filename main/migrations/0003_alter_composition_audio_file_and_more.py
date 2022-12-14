# Generated by Django 4.1.2 on 2022-10-22 14:35

from django.db import migrations, models
import main.validators


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_composition_playlist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='composition',
            name='audio_file',
            field=models.FileField(upload_to='', validators=[main.validators.validate_is_audio]),
        ),
        migrations.AlterField(
            model_name='composition',
            name='cover_image',
            field=models.ImageField(upload_to=''),
        ),
    ]
