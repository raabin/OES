# Generated by Django 3.1.1 on 2020-09-23 15:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_qna_mark'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qna',
            name='exam',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.exams'),
        ),
    ]