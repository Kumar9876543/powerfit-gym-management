from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('trainers/', views.trainers, name='trainers'),
    path('add-member/', views.add_member, name='add_member'),
    path('members/', views.member_list, name='member_list'),
    path('update-member/<int:id>/', views.update_member, name='update_member'),
    path('delete-member/<int:id>/', views.delete_member, name='delete_member'),
    path('dashboard/', views.customer_dashboard, name='customer_dashboard'),
    path('contact/', views.contact, name='contact'),
    
]
