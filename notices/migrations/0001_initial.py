# Generated by Django 4.2.5 on 2024-03-10 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Drive',
            fields=[
                ('title', models.CharField(max_length=100)),
                ('company_name', models.CharField(max_length=30)),
                ('company_logo', models.ImageField(blank=True, null=True, upload_to='')),
                ('date', models.DateField()),
                ('content', models.TextField()),
                ('Bond', models.CharField(max_length=50)),
                ('industry_type', models.CharField(max_length=50)),
                ('job_role', models.CharField(max_length=50)),
                ('job_location', models.CharField(max_length=50)),
                ('job_eligibility', models.TextField()),
                ('selection_process', models.TextField()),
                ('job_CTC', models.CharField(max_length=50)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('drive_id', models.AutoField(primary_key=True, serialize=False)),
                ('department', models.ManyToManyField(to='notices.department')),
            ],
            options={
                'ordering': ['creation_date'],
            },
        ),
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('activity_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('company_logo', models.ImageField(blank=True, null=True, upload_to='')),
                ('company_name', models.CharField(max_length=255)),
                ('industry_type', models.CharField(max_length=255)),
                ('activity_date', models.DateField()),
                ('content', models.TextField()),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('department', models.ManyToManyField(to='notices.department')),
            ],
            options={
                'ordering': ['creation_date'],
            },
        ),
    ]
