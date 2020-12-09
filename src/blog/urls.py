from django.urls import include, path
from . import views


app_name = 'blog'

urlpatterns = [
    path('', views.GetsView.as_view(), name='home'),
]
