# Generated by Django 5.0.6 on 2024-07-03 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(default='N/A', max_length=100)),
                ('Year', models.IntegerField(default=0)),
                ('Rated', models.CharField(default='N/A', max_length=20)),
                ('Released', models.CharField(default='N/A', max_length=20)),
                ('Runtime', models.CharField(default='N/A', max_length=20)),
                ('Genre', models.CharField(default='N/A', max_length=50)),
                ('Director', models.CharField(default='N/A', max_length=50)),
                ('Writer', models.CharField(default='N/A', max_length=50)),
                ('Actors', models.CharField(default='N/A', max_length=200)),
                ('plot', models.CharField(default='N/A', max_length=500)),
                ('Poster', models.URLField(default='N/A')),
                ('ImdbRating', models.FloatField(default=0.0)),
                ('ImdbVotes', models.IntegerField(default=0)),
                ('BoxOffice', models.CharField(default='N/A', max_length=50)),
                ('Language', models.CharField(default='N/A', max_length=50)),
                ('Awards', models.CharField(default='N/A', max_length=100)),
                ('Country', models.CharField(default='N/A', max_length=50)),
            ],
        ),
    ]