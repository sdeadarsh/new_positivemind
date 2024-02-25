from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()

router.register(r'brand', views.BrandViewSet, basename='brand')
router.register(r'bulk_file_upload', views.AgriInputBulkFileUploadViewSet, basename='bulk_file_upload')
router.register(r'bulk_file_upload_product', views.BulkFileUploadProductViewSet, basename='bulk_file_upload_product')
router.register(r'farmer_lead', views.FarmerLeadViewSet, basename='farmer_lead')
# router.register(r'farmer_cart', views.FarmerCartViewSet, basename='farmer_cart')

urlpatterns = [
    path('', include(router.urls)),
]