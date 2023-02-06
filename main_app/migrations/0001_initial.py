# Generated by Django 4.1.5 on 2023-02-06 00:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Beyonce',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=250)),
                ('age', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Tour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('album', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Shows',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='shows date')),
                ('sets', models.CharField(choices=[('S', 'Solo'), ('G', 'Group'), ('D', 'Duo')], default='S', max_length=1, verbose_name='show type')),
                ('beyonce', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.beyonce')),
            ],
            options={
                'ordering': ('-date',),
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=200)),
                ('beyonce', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.beyonce')),
            ],
        ),
        migrations.AddField(
            model_name='beyonce',
            name='tour',
            field=models.ManyToManyField(to='main_app.tour'),
        ),
        migrations.AddField(
            model_name='beyonce',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]