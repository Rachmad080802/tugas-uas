# Generated by Django 4.1.3 on 2022-12-08 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Upload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('judul', models.CharField(max_length=200)),
                ('konten', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='images')),
                ('date', models.DurationField()),
            ],
        ),
    ]
