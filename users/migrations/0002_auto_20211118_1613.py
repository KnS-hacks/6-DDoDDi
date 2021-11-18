# Generated by Django 3.2.9 on 2021-11-18 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='letter',
            old_name='sender',
            new_name='recipient',
        ),
        migrations.RemoveField(
            model_name='letter',
            name='letter_box',
        ),
        migrations.RemoveField(
            model_name='letter',
            name='updated_at',
        ),
        migrations.AlterField(
            model_name='letter',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='letterbox',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
