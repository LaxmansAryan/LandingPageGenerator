# Generated by Django 4.1.6 on 2023-04-05 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_alter_image_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='photo',
            field=models.ImageField(default='', null=True, upload_to='landing_page_images/'),
        ),
    ]
