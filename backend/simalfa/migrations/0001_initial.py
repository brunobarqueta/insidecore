# Generated by Django 4.2 on 2024-03-01 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tenant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True)),
                ('code', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=765)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Metrics',
            fields=[
                ('active', models.BooleanField(default=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=255)),
                ('type', models.CharField(max_length=50)),
                ('service', models.CharField(max_length=4000)),
                ('tenants', models.ManyToManyField(blank=True, null=True, to='simalfa.tenant')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Formula',
            fields=[
                ('active', models.BooleanField(default=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=255)),
                ('expression', models.CharField(max_length=4000)),
                ('tenants', models.ManyToManyField(blank=True, null=True, to='simalfa.tenant')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
