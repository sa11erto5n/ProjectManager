# Generated by Django 5.1.1 on 2024-11-04 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_auth', '0010_alter_user_account_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='notifications_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='orders_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='user',
            name='account_type',
            field=models.CharField(choices=[('admin', 'Administrator'), ('seller', 'Seller'), ('contributor', 'Contributor')], max_length=12, verbose_name='Account Type'),
        ),
    ]