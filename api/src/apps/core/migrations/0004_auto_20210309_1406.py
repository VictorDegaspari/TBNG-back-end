# Generated by Django 3.0.8 on 2021-03-09 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20210309_1220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='members',
            name='vip',
            field=models.CharField(choices=[('Não', 'básico'), ('Sim', 'premium')], default='Não', max_length=3),
        ),
    ]
