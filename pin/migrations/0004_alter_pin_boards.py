# Generated by Django 5.0.6 on 2024-12-23 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
        ('pin', '0003_alter_pin_boards'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pin',
            name='boards',
            field=models.ManyToManyField(blank=True, related_name='pins', to='board.board'),
        ),
    ]
