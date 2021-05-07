from django.urls import  path
from . import views
from .views import register

urlpatterns = [
    path('', views.index, name='index'), 
    path('partner/', views.partner, name='partner'),
    path('registernow',register,name="registernow"),
    path('schedule/', views.schedule, name='schedule'),
    path('committee/', views.committee, name='committee'),
    path('about/', views.about, name='about'),
    path('contact_Us/', views.contact, name='contact_Us'),

]