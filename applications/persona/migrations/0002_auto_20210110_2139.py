# Generated by Django 3.1.4 on 2021-01-11 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departamento', '0002_auto_20210110_2139'),
        ('persona', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Habilidades',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('habilidad', models.CharField(max_length=50, verbose_name='Habilidades')),
            ],
            options={
                'verbose_name': 'Habilidad',
                'verbose_name_plural': 'Habilidades de empleados',
            },
        ),
        migrations.AlterModelOptions(
            name='empleado',
            options={'ordering': ['-first_Name', 'last_Name'], 'verbose_name': 'Mis empleados', 'verbose_name_plural': 'Empleados de la empresa'},
        ),
        migrations.AlterUniqueTogether(
            name='empleado',
            unique_together={('first_Name', 'department')},
        ),
    ]