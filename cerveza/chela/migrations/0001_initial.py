# Generated by Django 3.2.5 on 2021-07-03 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='chela',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=50)),
                ('alcohol', models.DecimalField(decimal_places=2, max_digits=4)),
                ('minilitros', models.IntegerField()),
                ('artesanal', models.BooleanField()),
                ('nacionalidad', models.CharField(blank=True, max_length=50, null=True)),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('editado', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
