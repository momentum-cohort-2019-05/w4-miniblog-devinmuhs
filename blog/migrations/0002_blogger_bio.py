# Generated by Django 2.2.2 on 2019-06-22 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogger',
            name='bio',
            field=models.TextField(blank=True, default='', help_text='Type the blogger bio here', max_length=5000),
        ),
    ]
