from django.db import models


class Post(models.Model):
    TYPES_CHOICES = [
        ('Entertainment', 'Entertainment'),
        ('Lifestyle', 'Lifestyle'),
        ('Travel', 'Travel'),
        ('Food & Drink', 'Food & Drink'),
        ('Fashion & Beauty', 'Fashion & Beauty'),
        ('Health & Wellness', 'Health & Wellness'),
        ('Technology', 'Technology'),
        ('Business & Finance', 'Business & Finance'),
        ('Education', 'Education'),
        ('Sports', 'Sports'),
        ('Arts & Culture', 'Arts & Culture'),
        ('Science & Nature', 'Science & Nature'),
        ('Personal Development', 'Personal Development'),
        ('Parenting & Family', 'Parenting & Family'),
        ('Politics & Current Events', 'Politics & Current Events'),
    ]

    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    type = models.CharField(max_length=50, choices=TYPES_CHOICES, null=True)
