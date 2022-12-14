# Generated by Django 4.1.3 on 2022-12-13 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_image_classification_alter_image_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='dateClassified',
            field=models.DateTimeField(blank=True, default=None, null=True, verbose_name='classified on'),
        ),
        migrations.AlterField(
            model_name='image',
            name='dateAdded',
            field=models.DateTimeField(verbose_name='added on'),
        ),
    ]
