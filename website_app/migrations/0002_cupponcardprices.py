# Generated by Django 4.1.3 on 2022-11-08 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CupponCardPrices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header_title', models.CharField(max_length=50)),
                ('title_1', models.CharField(max_length=50)),
                ('title1_p', models.CharField(max_length=100)),
                ('title_2', models.CharField(max_length=50)),
                ('title2_p', models.CharField(max_length=100)),
                ('title_3', models.CharField(max_length=50)),
                ('title3_p', models.CharField(max_length=100)),
            ],
        ),
    ]
