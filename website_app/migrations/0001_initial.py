# Generated by Django 4.1.3 on 2022-11-08 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.IntegerField()),
                ('whatsapp_number', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('open_time', models.CharField(max_length=50)),
                ('address', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='SocialMediaLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facebook', models.TextField(blank=True, null=True)),
                ('twitter', models.TextField(blank=True, null=True)),
                ('gmail', models.TextField(blank=True, null=True)),
                ('linkedin', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
