# Generated by Django 4.1.7 on 2023-02-26 09:21

import app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='MediaResource',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.TextField(blank=True, max_length=500, null=True)),
                ('description', models.TextField(blank=True, max_length=5000, null=True)),
                ('audiofile', models.FileField(blank=True, max_length=500, null=True, upload_to=app.models.file_directory_path)),
                ('md5_generated', models.TextField(blank=True, max_length=32, null=True)),
                ('genre', models.TextField(blank=True, max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('artists', models.ManyToManyField(blank=True, related_name='artists', to='app.artist')),
                ('tags', models.ManyToManyField(blank=True, related_name='artists', to='app.tag')),
            ],
        ),
    ]