# Generated by Django 2.2.7 on 2019-11-27 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_auto_20191127_1518'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookinstance',
            name='id',
            field=models.CharField(help_text='Unique ID', max_length=200, primary_key=True, serialize=False),
        ),
    ]