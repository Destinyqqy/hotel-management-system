# Generated by Django 3.0.4 on 2020-04-13 15:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='dishclass',
            fields=[
                ('classname', models.CharField(max_length=30)),
                ('dishclassno', models.PositiveIntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='past_customer',
            fields=[
                ('id', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('sex', models.CharField(choices=[(1, '男'), (2, '女')], max_length=10)),
                ('birthday', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='room',
            fields=[
                ('room_id', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('room_type', models.CharField(choices=[(1, '高级大床房'), (2, '豪华双人大床房'), (3, '尊贵大床房')], max_length=30)),
                ('room_floor', models.PositiveIntegerField()),
                ('room_deposit', models.PositiveIntegerField()),
                ('room_is_booked', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='preferred_food',
            fields=[
                ('pf_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='CheckIn.past_customer')),
            ],
        ),
        migrations.CreateModel(
            name='dish',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('dishclassno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CheckIn.dishclass')),
            ],
        ),
        migrations.CreateModel(
            name='customer',
            fields=[
                ('id', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('sex', models.CharField(choices=[(1, '男'), (2, '女')], max_length=10)),
                ('birthday', models.DateTimeField()),
                ('is_checked', models.BooleanField()),
                ('agree_record', models.BooleanField()),
                ('face', models.ImageField(upload_to='')),
                ('room_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CheckIn.room')),
            ],
        ),
    ]