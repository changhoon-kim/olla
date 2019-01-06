from django.urls import path

from . import views

app_name = 'home'
urlpatterns = [
    # ex: /home/
    #path('', views.index, name='index'),
    path('', views.IndexView.as_view(), name='index'),
    # ex: /home/5/
    #path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # ex: /home/5/results
    #path('<int:pk>/results', views.results, name='results'),
    path('<int:pk>/results', views.ResultsView.as_view(), name='results'),
    # ex: /home/5/vote
    path('<int:question_id>/vote', views.vote, name='vote'),
]
