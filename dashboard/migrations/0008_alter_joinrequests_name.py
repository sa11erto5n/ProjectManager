# Generated by Django 5.1.1 on 2024-11-04 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0007_joinrequests'),
    ]

    operations = [
        migrations.AlterField(
            model_name='joinrequests',
            name='name',
            field=models.CharField(max_length=350, verbose_name='الاسم الكامل'),
        ),
    ]