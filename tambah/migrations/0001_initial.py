# Generated by Django 4.0.4 on 2022-09-30 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tambah_Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('pono', models.CharField(max_length=255)),
                ('qtykgs', models.IntegerField()),
                ('vendor', models.CharField(max_length=255)),
            ],
        ),
    ]
