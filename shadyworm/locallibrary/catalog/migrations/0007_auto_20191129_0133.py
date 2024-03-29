# Generated by Django 2.2.7 on 2019-11-28 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_auto_20191129_0023'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookinstance',
            options={'ordering': ['status']},
        ),
        migrations.RemoveField(
            model_name='bookinstance',
            name='due_back',
        ),
        migrations.RemoveField(
            model_name='bookinstance',
            name='publisher',
        ),
        migrations.AlterField(
            model_name='bookinstance',
            name='status',
            field=models.CharField(blank=True, choices=[('o', 'Out of stock'), ('a', 'Available at Warehouse')], default='m', help_text='Book availability', max_length=1),
        ),
    ]
