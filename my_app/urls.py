from django.urls import path
from . import views

app_name = 'my_app'
urlpatterns = [
    path('export/', views.export, name='export'),
    path('show_list/', views.show_list, name='show_list'),

]
