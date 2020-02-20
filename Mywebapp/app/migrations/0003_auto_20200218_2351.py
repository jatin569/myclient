# Generated by Django 2.2.5 on 2020-02-18 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('docfile', models.FileField(upload_to='documents/%Y/%m/%d')),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]