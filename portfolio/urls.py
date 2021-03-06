from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('', views.home, name='home'),
    path('portfolio', views.portfolio, name='portfolio'),
    path('about', views.about, name='about'),
    path('portfolio/<int:project_id>/', views.detailProject, name='detailProject'),

]
