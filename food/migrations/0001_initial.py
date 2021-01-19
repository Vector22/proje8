# Generated by Django 2.0.2 on 2020-11-23 12:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('url', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('nameFr', models.CharField(max_length=200)),
                ('genericNameFr', models.CharField(max_length=200)),
                ('url', models.CharField(max_length=200)),
                ('nutritionGrade', models.CharField(max_length=3)),
                ('countries', models.CharField(max_length=200)),
                ('purchasePlaces', models.CharField(max_length=200)),
                ('manufacturingPlaces', models.TextField()),
                ('ingredientsText', models.TextField()),
                ('image_link', models.URLField(max_length=250, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food.Category')),
            ],
        ),
        migrations.CreateModel(
            name='MyFood',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userId', models.IntegerField()),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food.Food')),
            ],
        ),
    ]