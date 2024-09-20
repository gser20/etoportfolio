from django.contrib import admin
from django.urls import path
from portfolio2 import views
from .views import contact_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('second_page/', views.second_page, name='second_page'),
    path('contact/', contact_view, name='contact'),  # Make sure this line is included
]
