# Generated by Django 5.1.1 on 2024-10-22 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_alter_request_earning_alter_request_project_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='NotificationsCounter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.AlterField(
            model_name='request',
            name='request_type',
            field=models.CharField(choices=[('refund', 'استرداد'), ('reinvest', 'إعادة الاستثمار')], max_length=10, verbose_name='Request Type'),
        ),
    ]