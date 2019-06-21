# Generated by Django 2.2.2 on 2019-06-21 17:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blogger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['first_name', 'last_name'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(help_text='Enter a comment here', max_length=200)),
                ('post_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-post_date'],
            },
        ),
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Enter a blog title', max_length=200)),
                ('post', models.TextField(help_text='Type your blog post here', max_length=5000)),
                ('post_date', models.DateTimeField(auto_now_add=True)),
                ('blogger', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.Blogger')),
            ],
            options={
                'ordering': ['-post_date'],
            },
        ),
    ]
