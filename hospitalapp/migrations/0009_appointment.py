# Generated by Django 5.1.6 on 2025-02-28 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospitalapp', '0008_ward'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=15)),
                ('date', models.DateTimeField()),
                ('department', models.CharField(max_length=50)),
                ('doctor', models.CharField(max_length=50)),
                ('message', models.TextField()),
            ],
        ),
    ]
