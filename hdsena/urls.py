from django.contrib import admin
from django.urls import include, path


from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('sena/', include('sena.urls')),
    path('', include('helpdesk.urls')),
    path('admin/', admin.site.urls),
] + static(settings.STATIC_URL,documement_root = settings.STATIC_ROOT)
