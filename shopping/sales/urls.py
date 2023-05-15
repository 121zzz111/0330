from django.urls import path

from . import views
from sales.views import *
from .views import SearchAPIView

urlpatterns = [
   # path('goods/', views.listgoods),
    # path(r'search/', views.search)   # http://127.0.0.1/api/sales/search/
    path('search/', SearchAPIView.as_view()),
]

