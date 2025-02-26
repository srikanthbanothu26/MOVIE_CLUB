# Generated by Django 5.0.6 on 2024-07-03 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moviezapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='Actors',
            field=models.CharField(default='N/A'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='Awards',
            field=models.CharField(default='N/A'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='BoxOffice',
            field=models.CharField(default='N/A'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='Country',
            field=models.CharField(default='N/A'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='Director',
            field=models.CharField(default='N/A'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='Genre',
            field=models.CharField(default='N/A'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='Language',
            field=models.CharField(default='N/A'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='Rated',
            field=models.CharField(default='N/A'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='Released',
            field=models.CharField(default='N/A'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='Runtime',
            field=models.CharField(default='N/A'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='Title',
            field=models.CharField(default='N/A'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='Writer',
            field=models.CharField(default='N/A'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='plot',
            field=models.CharField(default='N/A'),
        ),
    ]
