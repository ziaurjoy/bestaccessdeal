# Generated by Django 4.1.3 on 2022-11-09 11:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website_app', '0012_rename_blog_blogs'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogs',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='website_app.categorys'),
        ),
    ]
