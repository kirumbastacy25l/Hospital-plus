
from django.contrib import admin
from django.urls import path
from hospitalapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index,name = 'home'),
    path('service/', views.service,name='services'),
    path('starter/', views.starter,name = 'starter'),
    path('about/', views.about,name = 'about'),
    path('services/', views.services,name = 'services'),
    path('department/', views.department,name = 'department'),
    path('doctors/', views.doctors,name = 'doctors'),
    path('appointment/', views.appoint,name = 'appointment'),

]
