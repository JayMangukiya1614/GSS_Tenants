# Generated by Django 4.2.1 on 2023-09-19 11:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Applicant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('selected', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('resume', models.FileField(upload_to='resumes/')),
                ('linkedin_profile', models.URLField(blank=True)),
                ('github_profile', models.URLField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='JobListing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currently_accepting', models.BooleanField(default=True)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('description_file', models.FileField(upload_to='static/jd/')),
            ],
        ),
        migrations.CreateModel(
            name='ApplicantProgress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('selected', models.BooleanField(default=False)),
                ('status', models.CharField(choices=[('applied', 'Applied'), ('in_review', 'In Review'), ('interviewing', 'Interviewing'), ('offer_extended', 'Offer Extended'), ('hired', 'Hired'), ('rejected', 'Rejected')], default='applied', max_length=20)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='JobListings.applicant')),
            ],
        ),
        migrations.AddField(
            model_name='applicant',
            name='applied_for',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='JobListings.joblisting'),
        ),
    ]
