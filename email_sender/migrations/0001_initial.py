# Generated by Django 4.2.1 on 2023-09-19 11:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('JobListings', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Email_Compose',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=255)),
                ('message', models.TextField()),
                ('attachment', models.FileField(blank=True, null=True, upload_to='attachments/')),
                ('send_time', models.DateTimeField(auto_now=True)),
                ('recipients', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='JobListings.applicant')),
            ],
        ),
    ]