# Generated by Django 4.0.4 on 2022-05-03 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shopping', '0002_usuario_alter_cine_options_alter_locales_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='locales',
            name='cantLocales',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='locales',
            name='nomLocales',
            field=models.CharField(default=0, max_length=100),
        ),
        migrations.AlterField(
            model_name='patiocomidas',
            name='cantLocales',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='patiocomidas',
            name='nomLocales',
            field=models.CharField(default=0, max_length=100),
        ),
        migrations.AlterField(
            model_name='promos',
            name='fechas',
            field=models.DurationField(default=0),
        ),
        migrations.AlterField(
            model_name='promos',
            name='precios',
            field=models.BooleanField(default=0),
        ),
        migrations.AlterField(
            model_name='promos',
            name='promociones',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='edad',
            field=models.IntegerField(default=0),
        ),
    ]
