# Generated by Django 4.2.5 on 2024-03-18 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_alter_customuser_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='user_type',
            field=models.CharField(choices=[('Student', 'Student'), ('Coordinator', 'Coordinator'), ('TNP-Office', 'TNP-Office')], default='Student', max_length=15),
        ),
    ]
