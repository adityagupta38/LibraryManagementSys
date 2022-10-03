# Generated by Django 4.1.1 on 2022-10-03 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookslib', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='uname',
            new_name='username',
        ),
        migrations.RemoveField(
            model_name='user',
            name='pwd',
        ),
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default='', max_length=55),
            preserve_default=False,
        ),
    ]
