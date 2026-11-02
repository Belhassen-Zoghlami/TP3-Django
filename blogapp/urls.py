from .views import *
from django.urls import path
app_name="Posts"
urlpatterns = [
    path('list',BlogView.as_view(),name='listhtml'),
    path('create',BlogCreateWithFields.as_view(),name='createField'),
    path('create/form',BlogCreateWithForm.as_view(),name='createForm'),
]