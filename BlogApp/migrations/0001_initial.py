# Generated by Django 3.0.3 on 2020-02-24 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('tagId', models.IntegerField(primary_key=True, serialize=False)),
                ('tagname', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('postId', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=30)),
                ('content', models.CharField(max_length=300)),
                ('date', models.DateField(auto_now=True, verbose_name='Default')),
                ('image', models.ImageField(upload_to=None, verbose_name='Default')),
                ('tags', models.ManyToManyField(to='BlogApp.Tag')),
            ],
        ),
    ]
