# Generated by Django 3.2.8 on 2021-10-20 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='clientes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=64)),
                ('contactado', models.DateTimeField(auto_now=True)),
                ('foi_contactado', models.BooleanField(default=False)),
            ],
        ),
    ]
