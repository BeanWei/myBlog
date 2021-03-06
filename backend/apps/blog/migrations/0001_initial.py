# Generated by Django 2.0.2 on 2018-03-13 02:50

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='名称')),
            ],
            options={
                'verbose_name': '类别',
                'verbose_name_plural': '类别',
                'ordering': ['name', 'id'],
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='标题')),
                ('body', models.TextField(verbose_name='内容')),
                ('excerpt', models.CharField(blank=True, max_length=255, verbose_name='摘要')),
                ('timestamp', models.DateTimeField(db_index=True, default=datetime.datetime.now, verbose_name='时间戳')),
                ('read_num', models.IntegerField(default=0, editable=False, verbose_name='阅读次数')),
                ('own', models.BooleanField(choices=[(True, '原创'), (False, '转载')], default=True, verbose_name='属性')),
                ('published', models.BooleanField(choices=[(True, '发布'), (False, '草稿')], default=False, verbose_name='状态')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='作者')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.Category', verbose_name='类别')),
            ],
            options={
                'verbose_name': '文章',
                'verbose_name_plural': '文章',
                'ordering': ['-timestamp', 'id'],
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='名称')),
            ],
            options={
                'verbose_name': '标签',
                'verbose_name_plural': '标签',
                'ordering': ['name', 'id'],
            },
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(null=True, to='blog.Tag', verbose_name='标签'),
        ),
    ]
