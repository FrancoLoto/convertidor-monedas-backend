from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    # Admin URL
    path('admin/', admin.site.urls),

    # Auth urls
    path('api/auth/', include('djoser.urls')),
    path('api/auth/', include('djoser.urls.jwt')),
    path('api/auth/', include('users.urls')),

    # Converter urls
    path('api/', include('converter.urls')),

    # News urls
    path('api/news/', include('news.urls')),

]
