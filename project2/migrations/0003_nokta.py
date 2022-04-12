# Generated by Django 4.0.3 on 2022-04-12 00:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project2', '0002_rename_users_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nokta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nokta', models.CharField(max_length=200)),
                ('vote', models.SmallIntegerField(null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project2.user')),
            ],
        ),
    ]
