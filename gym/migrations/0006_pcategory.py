# Generated by Django 5.0.2 on 2024-03-12 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0005_trainer'),
    ]

    operations = [
        migrations.CreateModel(
            name='PCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=500)),
            ],
        ),
    ]