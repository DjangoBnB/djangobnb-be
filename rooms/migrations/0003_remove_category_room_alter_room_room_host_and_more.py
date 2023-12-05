# Generated by Django 4.2.2 on 2023-12-05 03:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0002_remove_host_room_room_room_host_alter_category_room'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='room',
        ),
        migrations.AlterField(
            model_name='room',
            name='room_host',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rooms.host'),
        ),
        migrations.CreateModel(
            name='Room_Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rooms.room')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rooms.category')),
            ],
        ),
        migrations.AddField(
            model_name='room',
            name='room_types',
            field=models.ManyToManyField(blank=True, related_name='types_room', through='rooms.Room_Category', to='rooms.category'),
        ),
    ]
