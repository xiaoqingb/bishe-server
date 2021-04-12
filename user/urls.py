from django.urls import path

from . import views
app_name = 'user'
urlpatterns = [
    # ex: /user/
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('userList', views.userList, name='userList'),
    path('importUser', views.importUser, name='importUser'),
    path('delete', views.delete, name='delete'),
    path('edit', views.edit, name='edit'),
    path('loginByCard', views.loginByCard, name='loginByCard'),
    path('favoriteTotal', views.favoriteTotal, name='favoriteTotal'),
    path('thumbTotal', views.thumbTotal, name='thumbTotal'),
    path('commentTotal', views.commentTotal, name='commentTotal'),
]