# Generated by Django 4.1.7 on 2023-03-02 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=100)),
                ('book_tittle', models.CharField(max_length=100)),
                ('book_author', models.CharField(max_length=50)),
            ],
        ),
    ]
