# Generated by Django 2.2.5 on 2020-09-16 18:50

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
            name='Pet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('favorite_toy', models.CharField(max_length=25)),
                ('birthday', models.DateField(verbose_name='Birthday')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=250)),
                ('imagePath', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('pet', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='catalogapp.Pet')),
            ],
            options={
                'verbose_name': 'photo',
                'verbose_name_plural': 'photos',
            },
        ),
        migrations.CreateModel(
            name='PetPhoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pet', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='catalogapp.Pet')),
                ('photo', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='catalogapp.Photo')),
            ],
            options={
                'verbose_name': 'pet photo',
                'verbose_name_plural': 'pets photos',
            },
        ),
    ]
