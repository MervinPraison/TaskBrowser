from django.urls import path


from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:task_id>/', views.detail, name='detail'),
    path('api/', views.task_list),
    path('api/<int:pk>/', views.task_detail),
]