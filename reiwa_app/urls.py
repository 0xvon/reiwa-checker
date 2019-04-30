from django.urls import path
from . import views


urlpatterns = [
    path('', views.model_form_upload, name='upload'),
    path('result', views.result, name='result'),
]