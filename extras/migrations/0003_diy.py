# Generated by Django 2.1.7 on 2019-09-16 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('extras', '0002_auto_20190915_1142'),
    ]

    operations = [
        migrations.CreateModel(
            name='DIY',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('photo', models.ImageField(upload_to='img/diy')),
                ('desc', models.CharField(max_length=1000)),
                ('mentor', models.CharField(max_length=50)),
                ('members', models.CharField(max_length=200)),
            ],
        ),
    ]
