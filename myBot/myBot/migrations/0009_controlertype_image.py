# Generated by Django 2.1.4 on 2019-01-16 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myBot', '0008_auto_20190116_1848'),
    ]

    operations = [
        migrations.AddField(
            model_name='controlertype',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
