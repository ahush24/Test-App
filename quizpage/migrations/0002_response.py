# Generated by Django 3.2.3 on 2021-05-28 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizpage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Question', models.CharField(max_length=100)),
                ('solution', models.CharField(max_length=100)),
            ],
        ),
    ]
