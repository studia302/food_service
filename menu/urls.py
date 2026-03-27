from django.urls import path
from .views import FoodListView

app_name = 'menu'

urlpatterns = [
    path('foods/', FoodListView.as_view(), name='food-list'),
]
