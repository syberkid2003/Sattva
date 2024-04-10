# Generated by Django 4.2 on 2024-04-04 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0012_test_questions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=12)),
                ('name', models.CharField(max_length=50)),
                ('marks', models.CharField(max_length=2)),
                ('test_no', models.CharField(max_length=2)),
            ],
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]
