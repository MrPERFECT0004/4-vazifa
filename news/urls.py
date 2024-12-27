from django.urls import path
from .views import brand,car

urlpatterns = [
    path('', brand, name='brand_list'), 
    path('car/',car,name="car_list"),
]