from django.urls import path

from . import views
app_name = 'favorite'
urlpatterns = [
    path('add', views.add, name='add'),
    path('cancel', views.cancel, name='remove'),
]