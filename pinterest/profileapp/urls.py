from django.urls import path

from .views import *

app_name = 'profileapp'

urlpatterns = [
    path('create/', ProfileCreateView.as_view(), name='create'),

]