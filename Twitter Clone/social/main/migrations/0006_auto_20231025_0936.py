# Generated by Django 3.2.12 on 2023-10-25 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_meep_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='facebook_link',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='github_link',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='instagram_link',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='linkedin_link',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='profile_bio',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
