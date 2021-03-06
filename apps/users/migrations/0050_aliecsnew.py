# Generated by Django 2.0.2 on 2018-10-09 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0049_auto_20181009_1718'),
    ]

    operations = [
        migrations.CreateModel(
            name='AliEcsnew',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shiliid', models.CharField(max_length=200, verbose_name='id')),
                ('name', models.CharField(max_length=200, verbose_name='名称')),
                ('os', models.CharField(max_length=200, verbose_name='os')),
                ('status', models.CharField(max_length=200, verbose_name='状态')),
                ('beizhu', models.CharField(max_length=200, verbose_name='备注')),
                ('region', models.CharField(max_length=200, verbose_name='地区')),
                ('location', models.CharField(max_length=200, verbose_name='可用区')),
                ('ip', models.CharField(max_length=200, verbose_name='ip')),
                ('neiip', models.CharField(max_length=200, verbose_name='内网ip')),
                ('cpu', models.CharField(max_length=200, verbose_name='cpu')),
                ('mem', models.CharField(max_length=200, verbose_name='内存')),
                ('chuangjian', models.CharField(max_length=200, verbose_name='创建')),
                ('daoqi', models.CharField(max_length=200, verbose_name='到期日期')),
                ('tag', models.CharField(max_length=200, verbose_name='标签')),
                ('images', models.CharField(max_length=200, verbose_name='镜像')),
                ('type', models.CharField(max_length=200, verbose_name='类型')),
            ],
            options={
                'verbose_name': '阿里ecs',
                'verbose_name_plural': '阿里ecs',
            },
        ),
    ]
