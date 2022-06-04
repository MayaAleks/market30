from django.urls import path
from .views import main_page, category_sort

app_name='main'
urlpatterns = [
    path('',main_page, name='main_page'),
    path('<int:id>/', category_sort, name="category_sort"),
]
