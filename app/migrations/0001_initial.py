# Generated by Django 4.2.1 on 2023-06-16 16:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='department',
            fields=[
                ('dep_no', models.IntegerField(primary_key=True, serialize=False)),
                ('dep_name', models.CharField(max_length=100)),
                ('dep_location', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='employee',
            fields=[
                ('emp_no', models.IntegerField(primary_key=True, serialize=False)),
                ('emp_name', models.CharField(max_length=100)),
                ('salary', models.IntegerField()),
                ('dep_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.department')),
            ],
        ),
    ]
