from django.urls import path

from . import views
app_name = 'lostAndFound'
urlpatterns = [
    path('submitLost', views.submitLost, name='submitLost'),
    path('submitLost', views.submitLost, name='submitLost'),
    path('list', views.list, name='list'),
    path('detail', views.detail, name='detail'),
    path('userList', views.userList, name='userList'),
]