# Generated by Django 4.1.4 on 2023-01-25 14:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('autenticacion', '0002_usuario_last_login_usuario_password'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Usuario',
        ),
    ]
