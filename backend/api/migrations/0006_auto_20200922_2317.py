# Generated by Django 3.1.1 on 2020-09-22 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20200922_2259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qna',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
