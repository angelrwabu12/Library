from django.urls import path
from .views import home,about,contact,registration,authordetail

urlpatterns = [
    path('',home,name='home'),
    path('about/',about,name='about'),
    path('contact/',contact,name='contact'),
    path('registration/',registration,name='registration'),
    path('authordetail/',authordetail,name='authordetail')
  ]
