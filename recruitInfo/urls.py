from django.urls import path

from . import views
app_name = 'recruitInfo'
urlpatterns = [
    path('list', views.list, name='list'),
    path('publish', views.publish, name='publish'),
    path('delete', views.delete, name='delete'),
    path('edit', views.edit, name='edit'),
    path('detail', views.detail, name='detail'),
    path('favoriteEdit', views.favoriteEdit, name='favoriteEdit'),
    path('userFavoriteList', views.userFavoriteList, name='userFavoriteList'),
    path('thumbUp', views.thumbUp, name='thumbUp'),
]