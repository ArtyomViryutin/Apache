# Generated by Django 3.2 on 2021-04-29 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.GenericIPAddressField()),
                ('date', models.DateTimeField()),
                ('method', models.CharField(max_length=7)),
                ('uri', models.TextField()),
                ('status', models.PositiveSmallIntegerField()),
                ('response_size', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Log',
                'verbose_name_plural': 'Logs',
            },
        ),
    ]
