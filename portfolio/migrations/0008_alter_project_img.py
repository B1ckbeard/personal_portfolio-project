# Generated by Django 3.2.7 on 2021-11-26 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0007_rename_imagemain_project_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='img',
            field=models.ImageField(upload_to='portfolio/images'),
        ),
    ]