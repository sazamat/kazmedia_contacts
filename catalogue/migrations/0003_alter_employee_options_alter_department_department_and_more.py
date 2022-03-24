# Generated by Django 4.0.3 on 2022-03-23 14:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0002_rename_phone_phone_phone'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='employee',
            options={'ordering': ['name', 'cell'], 'verbose_name': 'Сотрудник', 'verbose_name_plural': 'Сотрудники'},
        ),
        migrations.AlterField(
            model_name='department',
            name='department',
            field=models.CharField(max_length=120, unique=True, verbose_name='Департаменты'),
        ),
        migrations.AlterField(
            model_name='division',
            name='division',
            field=models.CharField(max_length=120, unique=True, verbose_name='Отделы'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='department',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalogue.department', verbose_name='Департамент'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='name',
            field=models.CharField(max_length=120, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='phone',
            name='phone',
            field=models.IntegerField(unique=True, verbose_name='Телефон'),
        ),
    ]