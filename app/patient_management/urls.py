from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()

router.register(r'patient', views.PatientViewSet, basename='patient')
router.register(r'document', views.DocumentViewSet, basename='document')

urlpatterns = [
    path('', include(router.urls)),
]
