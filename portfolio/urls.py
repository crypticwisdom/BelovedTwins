from portfolio.views import home
from django.urls import path

app_name = 'portfolio'

urlpatterns = [
    path('', home, name="home"),
]