# Generated by Django 3.2.3 on 2022-06-09 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_pro', '0003_auto_20220609_1516'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='img',
            field=models.ImageField(null=True, upload_to='img_mp'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='img',
            field=models.ImageField(null=True, upload_to='img_mp'),
        ),
    ]
