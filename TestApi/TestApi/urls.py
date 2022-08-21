from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),

    # path('auth/',include('djoser.urls')),
    # path('auth-token/',include('djoser.urls.authtoken')),
    path('auth/',include('rest_framework.urls')),

    path('', include('API.urls'))
]