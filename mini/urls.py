from django.urls import path

from mini import views
from mini.views import category

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('category', views.category, name='category'),
    path('portfolio', views.portfolio, name='portfolio'),
    path('blog', views.blog, name='blog'),
    path('contact', views.contact, name='contact'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
]