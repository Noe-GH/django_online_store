# Generated by Django 3.1.2 on 2021-02-17 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('show_products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='image',
            field=models.CharField(default='https://derdafoods.com/static/backend/img/meal-placeholder.jpg', max_length=500),
        ),
    ]