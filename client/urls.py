from django.urls import path
from . import views

app_name = 'client'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:poll_id>/', views.detail, name='detail'),
    path('<int:poll_id>/vote/', views.vote, name='vote'),
    path('<int:poll_id>/results/', views.results, name='results'),
    path('all_results/', views.all_results, name='all_results'),
]