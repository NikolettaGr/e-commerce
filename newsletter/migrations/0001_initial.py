# Generated by Django 3.2.23 on 2023-12-04 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmailNewsNotification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_name', models.CharField(help_text='Email name.', max_length=100, unique=True, verbose_name='Email name')),
                ('content', models.TextField(help_text='Content.', max_length=1500, verbose_name='Content')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
            ],
            options={
                'verbose_name': 'Email news notification',
                'verbose_name_plural': 'Email news notifications',
            },
        ),
        migrations.CreateModel(
            name='SubscribeUsers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=250)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
            ],
            options={
                'verbose_name': 'Email news notification',
                'verbose_name_plural': 'Email news notifications',
            },
        ),
    ]
