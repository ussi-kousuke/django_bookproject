# Generated by Django 4.1 on 2022-09-12 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0008_alter_book_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='book_contents',
            field=models.CharField(max_length=5000, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='book_image_url',
            field=models.URLField(null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='book_url',
            field=models.URLField(null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='price',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='publisherName',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='salesDate',
            field=models.CharField(max_length=100, null=True),
        ),
    ]