# Generated by Django 5.0.2 on 2024-03-14 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0007_membershippackage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shifts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shift', models.CharField(max_length=100)),
            ],
        ),
    ]