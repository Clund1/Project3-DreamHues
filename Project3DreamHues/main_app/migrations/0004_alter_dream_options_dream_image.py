# Generated by Django 4.2.9 on 2024-01-23 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_auto_20240123_1706'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dream',
            options={'ordering': ['-date']},
        ),
        migrations.AddField(
            model_name='dream',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='dream_image/'),
        ),
    ]