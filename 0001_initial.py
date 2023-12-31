# Generated by Django 4.1.2 on 2022-12-26 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student_marksheet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=50)),
                ('father_name', models.CharField(max_length=50)),
                ('mother_name', models.CharField(max_length=50)),
                ('roll_number', models.IntegerField()),
                ('school_code', models.IntegerField()),
                ('data_of_birth', models.DateField()),
                ('regular_or_private', models.CharField(max_length=15)),
                ('section', models.CharField(max_length=1)),
                ('hindi', models.IntegerField()),
                ('english', models.IntegerField()),
                ('maths', models.IntegerField()),
                ('so_science', models.IntegerField()),
                ('sanskrit', models.IntegerField()),
                ('science', models.IntegerField()),
            ],
        ),
    ]
