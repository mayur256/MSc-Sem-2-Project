# Generated by Django 2.2.5 on 2019-10-14 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20191007_2343'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='city',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='mob',
            field=models.CharField(blank=True, max_length=14, null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.CharField(max_length=160),
        ),
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('Happy', 'Happy'), ('Sad', 'Sad'), ('Alone', 'Alone'), ('Loved', 'Loved'), ('Broken', 'Broken'), ('Excited', 'Excited'), ('Motivated', 'Motivated'), ('Crazy', 'Crazy'), ('Cried', 'Cried')], default='Happy', max_length=10),
        ),
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='images'),
        ),
    ]
