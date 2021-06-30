from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.conf.urls import url
from filebrowser.sites import site

# =============================================
from django.conf import settings
from django.conf.urls.static import static 
# =============================================


from wiki.views import VisitorCreateView, VisitorUpdateView, VisitorListView 


urlpatterns = [
    path('admin/filebrowser/', site.urls),
    path('grappelli/', include('grappelli.urls')),
    path('admin/', admin.site.urls),
    path('', include("wiki.urls")),
    path('', VisitorListView.as_view(), name='person_list'),
    path('add/', VisitorCreateView.as_view(), name='person_add'),
    path('<int:pk>/edit/', VisitorUpdateView.as_view(), name='person_edit'),

] 
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


