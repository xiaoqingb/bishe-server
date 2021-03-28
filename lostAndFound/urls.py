from django.urls import path

from . import views
app_name = 'lostAndFound'
urlpatterns = [
    path('submitLost', views.submitLost, name='submitLost'),
    path('list', views.list, name='list'),
    path('detail', views.detail, name='detail'),
    path('userList', views.userList, name='userList'),
    path('approve', views.approve, name='approve'),
    path('delete', views.delete, name='delete'),
    path('reject', views.reject, name='reject'),
    path('adminEdit', views.adminEdit, name='adminEdit'),
    path('adminList', views.adminList, name='adminList'),
]