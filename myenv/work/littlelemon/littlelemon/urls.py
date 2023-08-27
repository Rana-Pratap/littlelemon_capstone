from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from rest_framework import routers
from restaurant import views

# Define router
router = routers.DefaultRouter()
router.register(r'tables', views.BookingViewSet)

# Define urlpatterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path('restaurant/', include('restaurant.urls')),
    path('', RedirectView.as_view(url='/restaurant/', permanent=True)),
    path('api/', include(router.urls)),
    path('restaurant/booking/', include(router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('auth/', include('rest_authtoken.urls')),
]
