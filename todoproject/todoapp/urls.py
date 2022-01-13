from . import views
from django.urls import path

urlpatterns = [

    path('', views.add, name='add'),
    path('delete/<int:taskid>/', views.delete, name='delete'),
    path('update/<int:id>/', views.update, name='update'),
    path('cbvhome/', views.ListView.as_view(), name='cbvhome'),
    path('cvbdetails/<int:pk>/', views.TaskDetailview.as_view(), name='cvbdetails'),
    path('cvbupdate/<int:pk>/', views.TaskUpdateView.as_view(), name='cvbupdate'),
    path('cvbdelete/<int:pk>/', views.TaskDeleteview.as_view(), name='cvbdelete'),

]
