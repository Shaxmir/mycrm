# Generated by Django 5.2 on 2025-04-30 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Deal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=255)),
                ('client_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('status', models.CharField(choices=[('processing', 'В обработке'), ('invoice_created', 'Сделан Счет/Накладная'), ('paid', 'Оплачено'), ('cutting', 'Отдано в распил'), ('completed', 'Сделка завершена')], default='processing', max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='DealProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
