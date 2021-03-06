# Generated by Django 3.2.4 on 2022-02-06 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=120)),
                ('author', models.CharField(max_length=120)),
                ('price', models.PositiveIntegerField()),
                ('copies', models.PositiveIntegerField()),
            ],
        ),
    ]
