from django.db import models

# Create your models here.
class Author(models.Model):
    First_Name = models.CharField(max_length=100, null=True, blank=True, help_text='Enter your first name')
    Last_Name = models.CharField(max_length=100, null=True, blank=True, help_text='Enter your last name')
    Email = models.EmailField(max_length=100, null=True, blank=True, help_text='Enter your email')
    Image = models.ImageField(upload_to='images/', null=True, blank=True, help_text='Enter your image')
    def __str__(self):
        return self.First_Name + ' ' + self.Last_Name
    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'
        ordering = ['First_Name', 'Last_Name']

class Category(models.Model):
    Category_Name = models.CharField(max_length=100, null=True, blank=True, help_text='Enter your category name')
    def __str__(self):
        return self.Category_Name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['Category_Name']
class Post(models.Model):
    Post_Title = models.CharField(max_length=100, null=True, blank=True, help_text='Enter your post title')
    Post_Content = models.TextField(null=True, blank=True, help_text='Enter your post content')
    Author = models.ForeignKey(Author, on_delete=models.CASCADE)
    Category = models.ForeignKey(Category, on_delete=models.CASCADE)
    def __str__(self):
        return self.Post_Title
    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ['Post_Title']

