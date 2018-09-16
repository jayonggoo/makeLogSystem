from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
	path('', views.index, name='index'),
    #path('<int:pk>/', views.DetailView.as_view(), name='detail'),
	path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
	path('<int:question_id>/vote/', views.vote, name='vote'),
	path('test', views.test_celery),
	path('register', views.register, name='register'),
	path('<int:data_id>/', views.detailRegister, name='registerDetail')
]
