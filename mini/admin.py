from django.contrib import admin

from mini.models import Category, Author, Post


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['Category_Name']
    list_filter = ['Category_Name']
    search_fields = ['Category_Name']

admin.site.register(Category, CategoryAdmin)

class AuthorAdmin(admin.ModelAdmin):
    list_display = ['First_Name', 'Last_Name', 'Email',]
    search_fields = ['First_Name', 'Last_Name', 'Email']
    list_filter = ['First_Name', 'Last_Name', 'Email']

admin.site.register(Author, AuthorAdmin)

class PostAdmin(admin.ModelAdmin):
    list_display = ['Post_Title', 'Post_Content', 'Author', 'Category']
    search_fields = ['Post_Title', 'Post_Content', 'Author', 'Category']
    list_filter = ['Post_Title', 'Author', 'Category']

admin.site.register(Post, PostAdmin)
