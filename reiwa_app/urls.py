from django.urls import path
from . import views


urlpatterns = [
    path('', views.model_form_upload, name='upload'),
    path('calc', views.calc, name='calc'),
    path('result', views.result, name='result'),
]