# Generated by Django 2.0.2 on 2018-08-11 14:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0021_auto_20180811_0951'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fuzeren',
            old_name='fu_ze_ren_qq',
            new_name='qq',
        ),
        migrations.RenameField(
            model_name='fuzeren',
            old_name='fu_ze_ren_shou_ji',
            new_name='shou_ji',
        ),
        migrations.RenameField(
            model_name='fuzeren',
            old_name='fu_ze_ren_wechat',
            new_name='wechat',
        ),
    ]