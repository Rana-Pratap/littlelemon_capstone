from django.urls import path
from rest_framework import routers
from .views import MenuItemsView, SingleMenuItemView, BookingViewSet, index

router = routers.DefaultRouter()
router.register(r'tables', BookingViewSet)

urlpatterns = [
    path('', index, name='index'),
    path('menu/', MenuItemsView.as_view(), name='menu-list'),
    path('menu/<int:pk>/', SingleMenuItemView.as_view(), name='menu-detail'),
]

urlpatterns += router.urls
