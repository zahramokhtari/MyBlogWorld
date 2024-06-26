# Generated by Django 5.0.6 on 2024-05-15 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_post_city'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='city',
        ),
        migrations.AddField(
            model_name='post',
            name='type',
            field=models.CharField(choices=[('Entertainment', 'Entertainment'), ('Lifestyle', 'Lifestyle'), ('Travel', 'Travel'), ('Food & Drink', 'Food & Drink'), ('Fashion & Beauty', 'Fashion & Beauty'), ('Health & Wellness', 'Health & Wellness'), ('Technology', 'Technology'), ('Business & Finance', 'Business & Finance'), ('Education', 'Education'), ('Sports', 'Sports'), ('Arts & Culture', 'Arts & Culture'), ('Science & Nature', 'Science & Nature'), ('Personal Development', 'Personal Development'), ('Parenting & Family', 'Parenting & Family'), ('Politics & Current Events', 'Politics & Current Events')], max_length=50, null=True),
        ),
    ]
