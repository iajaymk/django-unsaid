from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('detail/<int:id>/',views.detail, name="detail"),
    path('submit/',views.submit, name='submit'),
    path('about/', views.about, name='about')
]