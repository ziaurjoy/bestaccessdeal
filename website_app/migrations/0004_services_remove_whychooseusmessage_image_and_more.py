# Generated by Django 4.1.3 on 2022-11-09 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website_app', '0003_whychooseusmessage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('message', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='services/')),
            ],
        ),
        migrations.RemoveField(
            model_name='whychooseusmessage',
            name='image',
        ),
        migrations.RemoveField(
            model_name='whychooseusmessage',
            name='title',
        ),
    ]
