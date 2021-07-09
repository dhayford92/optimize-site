from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('optimize.urls')),
    path('blog/', include('blog.urls')),
]
admin.site.site_header = 'Optimize Admin'
admin.site.site_title = 'Optimize Admin Portal'
admin.site.index_title = 'Welcome to Optimize Main Page Portal'
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)