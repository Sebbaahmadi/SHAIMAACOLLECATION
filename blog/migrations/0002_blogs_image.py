# Generated by Django 4.0.3 on 2022-05-28 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogs',
            name='image',
            field=models.ImageField(null=True, upload_to='img/%y'),
        ),
    ]