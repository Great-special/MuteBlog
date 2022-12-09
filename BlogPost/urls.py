from django.urls import path
from BlogPost import  views


urlpatterns = [
    path('', views.home, name='home'),
    path('category/<str:cats>/', views.categories, name='category'),

    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('login/', views.login_user, name='login'),
    path('register/', views.register, name='register'),
    path('add-blog/', views.add_blog, name="add-blog"),
    path('blog-detail/<str:slug>/', views.blog_detail, name="blog-detail"),
    path('see-blog/', views.see_blog, name="see-blog"),
    path('blog-delete/<str:slug>/', views.blog_delete, name="blog-delete"),
    path('blog-update/<str:slug>/', views.blog_update, name="blog-update"),
    path('logout-view/', views.logout_user, name="logout"),

]


