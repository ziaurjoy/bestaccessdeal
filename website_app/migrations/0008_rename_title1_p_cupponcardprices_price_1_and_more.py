# Generated by Django 4.1.3 on 2022-11-09 10:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website_app', '0007_rename_image1_services_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cupponcardprices',
            old_name='title1_p',
            new_name='price_1',
        ),
        migrations.RenameField(
            model_name='cupponcardprices',
            old_name='title2_p',
            new_name='price_2',
        ),
        migrations.RenameField(
            model_name='cupponcardprices',
            old_name='title3_p',
            new_name='price_3',
        ),
        migrations.RenameField(
            model_name='cupponcardprices',
            old_name='title_1',
            new_name='products_1',
        ),
        migrations.RenameField(
            model_name='cupponcardprices',
            old_name='title_2',
            new_name='products_2',
        ),
        migrations.RenameField(
            model_name='cupponcardprices',
            old_name='title_3',
            new_name='products_3',
        ),
    ]
