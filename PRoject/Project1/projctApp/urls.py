from django.urls import path
from . import views
urlpatterns = [
	path('',views.projct,name='projct'),
    path('contact/',views.contact,name='contact'),
    path('destinations/',views.destinations,name='destinations'),
    path('elements/',views.elements,name='elements'),
    path('news/',views.news,name='news')
]
