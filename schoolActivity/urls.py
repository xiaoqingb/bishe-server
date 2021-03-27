from django.urls import path

from . import views
app_name = 'schoolActivity'
urlpatterns = [
    path('list', views.list, name='list'),
    path('publish', views.publish, name='publish'),
    path('delete', views.delete, name='delete'),
    path('edit', views.edit, name='edit'),
    path('detail', views.detail, name='detail'),
    path('apply', views.apply, name='apply'),
    path('enterList', views.enterList, name='enterList'),
]