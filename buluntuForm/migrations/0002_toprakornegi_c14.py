# Generated by Django 4.2.7 on 2024-02-18 14:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('buluntu', '0001_initial'),
        ('buluntuForm', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TOPRAKORNEGI',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.CharField(max_length=50, verbose_name='Miktar')),
                ('flotasyonOncesi', models.CharField(max_length=50, verbose_name='Flotasyon Öncesi Miktar')),
                ('flotasyonSonrasi', models.CharField(max_length=50, verbose_name='Flotasyon Sonrası Miktar')),
                ('description', models.TextField(verbose_name='Tanım')),
                ('linked', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='toprak_ornegi', to='buluntuForm.formlar')),
                ('piece_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buluntu.piece', verbose_name='Eser Adı')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buluntu.status', verbose_name='Durum')),
            ],
        ),
        migrations.CreateModel(
            name='C14',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.CharField(choices=[('1', 'Anali Tüpü'), ('2', 'Plastik Kutu'), ('3', 'Korunmuş Ahşap Örneği')], max_length=50, verbose_name='Miktar')),
                ('description', models.TextField(verbose_name='Tanım')),
                ('linked', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='c14', to='buluntuForm.formlar')),
                ('piece_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buluntu.piece', verbose_name='Eser Adı')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buluntu.status', verbose_name='Durum')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buluntu.tur', verbose_name='Tür')),
            ],
        ),
    ]
