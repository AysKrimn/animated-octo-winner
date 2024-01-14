# Generated by Django 4.2.7 on 2024-01-14 17:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fixture', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customtaxrate',
            name='rate',
            field=models.DecimalField(decimal_places=2, max_digits=6, unique=True, verbose_name='Vergi Oranı'),
        ),
        migrations.AlterField(
            model_name='fixture',
            name='taxrate',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fixture.customtaxrate', to_field='rate', verbose_name='Vergi'),
        ),
    ]
