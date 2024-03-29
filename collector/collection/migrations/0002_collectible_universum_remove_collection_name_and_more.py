# Generated by Django 4.1.4 on 2023-01-30 19:38

import collection.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('collection', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Collectible',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Universum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('display_name', models.CharField(max_length=200, unique=True)),
                ('slug', models.CharField(max_length=200, unique=True)),
                ('description', models.TextField(default='')),
                ('creator', models.CharField(default='', max_length=200)),
                ('homepage', models.URLField()),
                ('icon', models.ImageField(height_field=100, upload_to='universum_icons', width_field=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='collection',
            name='name',
        ),
        migrations.AddField(
            model_name='collection',
            name='creator',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='collection',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='collection',
            name='display_name',
            field=models.CharField(default='Collection', max_length=200),
        ),
        migrations.AddField(
            model_name='collection',
            name='homepage',
            field=models.URLField(default='default'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='collection',
            name='icon',
            field=models.ImageField(default='icon', height_field=100, upload_to='collection_icons', width_field=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='collection',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=models.SET(collection.models.get_foster_collector), to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='collection',
            name='slug',
            field=models.CharField(default='collection', max_length=200, unique=True),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='HistoricalCollection',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('display_name', models.CharField(default='Collection', max_length=200)),
                ('slug', models.CharField(db_index=True, max_length=200)),
                ('description', models.TextField(default='')),
                ('creator', models.CharField(default='', max_length=200)),
                ('homepage', models.URLField()),
                ('icon', models.TextField(max_length=100)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('owner', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical collection',
                'verbose_name_plural': 'historical collections',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
