from django import urls
from django.urls import path, include
from wiki.views import scrape
# , news_list

from rest_framework import routers
from . import views 

router = routers.DefaultRouter()
router.register(r'users', views.VisitorViewset)


urlpatterns = [
    path('api/', include(router.urls)),
	path('scrape/', scrape, name="scrape"),
	# path('', news_list, name="home"),
]