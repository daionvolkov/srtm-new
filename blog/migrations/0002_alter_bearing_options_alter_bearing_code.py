# Generated by Django 4.0.1 on 2022-03-04 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bearing',
            options={'verbose_name': 'Подшипник', 'verbose_name_plural': 'Подшипники'},
        ),
        migrations.AlterField(
            model_name='bearing',
            name='code',
            field=models.CharField(max_length=200, verbose_name='Артикул'),
        ),
    ]