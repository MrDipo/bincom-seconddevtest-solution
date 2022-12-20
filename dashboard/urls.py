from django.urls import path
from . import views

urlpatterns = [
    path('pu-single', views.pu_single),
    path('lga-single', views.lga_single),
    path('add-results', views.add_results),
]
