# Generated by Django 4.1.1 on 2022-12-02 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='subtitle',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]