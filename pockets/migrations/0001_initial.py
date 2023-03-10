# Generated by Django 4.1.5 on 2023-01-24 20:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('items', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Pocket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_of_red_packets', models.IntegerField(default=0)),
                ('multiplier', models.IntegerField(default=1)),
                ('items', models.ManyToManyField(blank=True, related_name='pockets', to='items.item')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pocket', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
