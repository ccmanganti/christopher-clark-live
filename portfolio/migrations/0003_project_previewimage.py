# Generated by Django 3.2.9 on 2022-02-20 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_rename_post_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='previewImage',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
