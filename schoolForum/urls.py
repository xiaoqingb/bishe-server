from django.urls import path

from . import views
app_name = 'schoolForum'
urlpatterns = [
    path('list', views.list, name='list'),
    path('publish', views.publish, name='publish'),
    path('delete', views.delete, name='delete'),
    path('edit', views.edit, name='edit'),
    path('detail', views.detail, name='detail'),
    path('thumbUp', views.thumbUp, name='thumbUp'),
    path('comment', views.comment, name='comment'),
    path('deleteComment', views.deleteComment, name='deleteComment'),
]