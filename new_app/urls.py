from django.urls import path

from .views import index

app_name = 'new_app'

urlpatterns=[
    path('index/',index,name='index')
]