# Generated by Django 3.2.9 on 2022-01-02 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0003_alter_listing_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='title',
            field=models.CharField(max_length=255),
        ),
    ]