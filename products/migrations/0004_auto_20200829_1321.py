# Generated by Django 3.1 on 2020-08-29 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='ip',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
    ]
