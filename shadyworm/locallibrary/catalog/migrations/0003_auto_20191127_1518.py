# Generated by Django 2.2.7 on 2019-11-27 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20191127_1507'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookinstance',
            old_name='imprint',
            new_name='publisher',
        ),
        migrations.AlterField(
            model_name='bookinstance',
            name='status',
            field=models.CharField(blank=True, choices=[('o', 'Out of stock'), ('a', 'Available')], default='m', help_text='Book availability', max_length=1),
        ),
    ]
