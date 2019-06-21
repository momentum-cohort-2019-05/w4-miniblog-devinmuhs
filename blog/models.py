from django.db import models
from django.urls import reverse # Used to generate URLs by reversing the URL patterns
# import uuid # Required for unique blog instances
from datetime import date


# Create your models here.
class BlogPost(models.Model):
    """Model representing a blog post."""
    title = models.CharField(max_length=200, help_text='Enter a blog title')
    post = models.TextField(max_length=5000, help_text='Type your blog post here')
    blogger = models.ForeignKey('Blogger', on_delete=models.SET_NULL, null=True)
    post_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-post_date']

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.title} {self.post_date}'

class Blogger(models.Model):
    """Model representing a blogger."""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    class Meta:
        ordering = ['first_name', 'last_name']

    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('blogger-detail', args=[str(self.id)])

    
    def __str__(self):
        """String for representing the Model object."""
        return f'{self.first_name} {self.last_name}'

class Comment(models.Model):
    """Model representing a blog post."""
    comment = models.CharField(max_length=200, help_text='Enter a comment here')
    post_date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-post_date']

    def __str__(self):
        """String for representing the Model object."""
        return self.comment, self.post_date