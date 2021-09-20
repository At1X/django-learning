# Generated by Django 3.1.7 on 2021-09-09 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0005_auto_20210905_2108'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'گروه', 'verbose_name_plural': 'گروه\u200cها'},
        ),
        migrations.AlterModelOptions(
            name='foodargus',
            options={'verbose_name': 'غذا', 'verbose_name_plural': 'غذاها'},
        ),
        migrations.AlterField(
            model_name='foodargus',
            name='rate',
            field=models.CharField(choices=[('5', '5'), ('2', '2'), ('3', '3'), ('4', '4'), ('1', '1')], max_length=1),
        ),
    ]
