# Generated by Django 4.2.1 on 2023-06-10 10:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('asosiy', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mahsulot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('narx', models.PositiveSmallIntegerField()),
                ('min_miqdor', models.PositiveSmallIntegerField()),
                ('davlat', models.CharField(max_length=60)),
                ('brend', models.CharField(max_length=60)),
                ('matn', models.TextField()),
                ('kafolat', models.PositiveSmallIntegerField()),
                ('chegirma', models.PositiveSmallIntegerField(default=0)),
                ('bolim', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asosiy.bolim')),
            ],
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rasm', models.FileField(upload_to='')),
                ('mahsulot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asosiy.mahsulot')),
            ],
        ),
    ]
