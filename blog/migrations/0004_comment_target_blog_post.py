# Generated by Django 2.2.2 on 2019-06-22 19:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20190622_1522'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='target_blog_post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.BlogPost'),
        ),
    ]
