# Generated by Django 3.1.7 on 2021-09-01 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='foodArgus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('slug', models.SlugField(max_length=20)),
                ('desc', models.TextField()),
                ('rate', models.CharField(choices=[('2', '2'), ('4', '4'), ('5', '5'), ('1', '1'), ('3', '3')], max_length=1)),
                ('auth', models.CharField(choices=[('Y', 'Yasin'), ('A', 'Atid'), ('N', 'Narges'), ('L', 'Ardalan')], max_length=1)),
                ('pic', models.ImageField(upload_to='foodpics/')),
                ('group', models.ManyToManyField(to='food.category')),
            ],
        ),
    ]