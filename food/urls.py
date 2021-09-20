from django.urls import path
from .views import base, home

app_name = 'blog'

urlpatterns = [
	path('', home, name= 'home'),
	path('articles/<slug:catID>/', base, name='catID')

]