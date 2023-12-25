from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('books', views.books, name='index'),
    path('delete', views.delete, name='index'),
    path('update', views.update, name='index'),

]
