# Generated by Django 2.2.5 on 2019-10-14 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_report'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='cmnt',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='report',
            name='post',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='report',
            name='user',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
