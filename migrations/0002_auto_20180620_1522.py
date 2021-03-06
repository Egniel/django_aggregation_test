# Generated by Django 2.0.6 on 2018-06-20 15:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('text', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('population', models.FloatField(verbose_name='Население')),
                ('area', models.FloatField(verbose_name='Площадь')),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
            ],
        ),
        migrations.RemoveField(
            model_name='borrower',
            name='industry',
        ),
        migrations.DeleteModel(
            name='Borrower',
        ),
        migrations.DeleteModel(
            name='Industry',
        ),
        migrations.AddField(
            model_name='city',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cities', to='text.Country', verbose_name='Страна'),
        ),
    ]
