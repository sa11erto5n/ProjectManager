# Generated by Django 5.1.1 on 2024-10-19 16:09

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100, verbose_name='اسم المنتج')),
                ('product_quantity', models.IntegerField(verbose_name='كمية المنتج')),
                ('remaining_quantity', models.IntegerField(default=0, verbose_name='الكمية المتبقية')),
                ('product_price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='سعر')),
                ('product_image', models.ImageField(max_length=1200, upload_to='products/', verbose_name='صورة المنتج')),
                ('date_added', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Earning',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('earning', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='السعر المكتسب')),
                ('date_added', models.DateField(auto_now_add=True, verbose_name='تاريخ الإضافة')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='earnings', to=settings.AUTH_USER_MODEL, verbose_name='أرباح المستخدم')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='earning', to='dashboard.product', verbose_name='منتج')),
            ],
        ),
        migrations.CreateModel(
            name='Contribution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_price', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='سعر المساهمة')),
                ('date_added', models.DateField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='contributions', to=settings.AUTH_USER_MODEL, verbose_name='مستخدم')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contributed_projects', to='dashboard.product', verbose_name='منتج')),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(verbose_name='الكمية المباعة')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='سعر')),
                ('date_added', models.DateField(verbose_name='تاريخ البيع')),
                ('is_returned', models.BooleanField(default=False, verbose_name='Returned Products?')),
                ('is_canceled', models.BooleanField(default=False, verbose_name='تم إلغاء الطلب؟')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='report', to='dashboard.product', verbose_name='منتج')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reports', to=settings.AUTH_USER_MODEL, verbose_name='تقارير المستخدم')),
            ],
        ),
    ]
