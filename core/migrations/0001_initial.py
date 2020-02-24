# Generated by Django 3.0.2 on 2020-02-22 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Filmes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=40)),
                ('mes', models.CharField(max_length=10)),
                ('ano', models.IntegerField(default=0)),
                ('genero', models.CharField(max_length=20)),
                ('tipo', models.CharField(max_length=10)),
                ('receita', models.IntegerField(default=0)),
            ],
        ),
    ]