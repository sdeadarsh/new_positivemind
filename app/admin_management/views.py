from django.shortcuts import render
from rest_framework import viewsets, permissions, status
from .models import Admin, UserType
from .serializers import UserTypeSerializer, AdminSerializer
from positivemind.utils import successful_response, error_response
from django.core import paginator


# Create your views here.

class AdminViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    serializer_class = AdminSerializer
    queryset = Admin.objects.all()
    http_method_names = ['get', 'post', 'patch', 'delete', 'put']

    def create(self, request, *args, **kwargs):
        try:
            response = super(AdminViewSet, self).create(request, *args, **kwargs)
            return successful_response(response.data)
        except Exception as e:
            return error_response(str(e))

    def add_pagination(self, dict_data, page, count):
        if page and count:
            p = paginator.Paginator(dict_data, count)
            return p.page(page).object_list
        return dict_data

    def list(self, request, *args, **kwargs):
        try:
            response = super(AdminViewSet, self).list(request, *args, **kwargs)
            return successful_response(response.data)
        except Exception as e:
            return error_response(str(e))

    def retrieve(self, request, *args, **kwargs):
        try:
            response = super(AdminViewSet, self).retrieve(request, *args, **kwargs)
            return successful_response(response.data)
        except Exception as e:
            return error_response(str(e))

    def update(self, request, *args, **kwargs):
        try:
            response = super(AdminViewSet, self).update(request, partial=True)
            return successful_response(response.data)
        except Exception as e:
            return error_response(str(e))

    def destroy(self, request, *args, **kwargs):
        try:
            Admin.objects.filter(pk=kwargs['pk']).update(is_active=0)
            return successful_response({})
        except Exception as e:
            return error_response(str(e))


class UserTypeViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    serializer_class = UserTypeSerializer
    queryset = UserType.objects.all()
    http_method_names = ['get', 'post', 'patch', 'delete', 'put']

    def create(self, request, *args, **kwargs):
        try:
            response = super(UserTypeViewSet, self).create(request, *args, **kwargs)
            return successful_response(response.data)
        except Exception as e:
            return error_response(str(e))

    def add_pagination(self, dict_data, page, count):
        if page and count:
            p = paginator.Paginator(dict_data, count)
            return p.page(page).object_list
        return dict_data

    def list(self, request, *args, **kwargs):
        try:
            response = super(UserTypeViewSet, self).list(request, *args, **kwargs)
            return successful_response(response.data)
        except Exception as e:
            return error_response(str(e))

    def retrieve(self, request, *args, **kwargs):
        try:
            response = super(UserTypeViewSet, self).retrieve(request, *args, **kwargs)
            return successful_response(response.data)
        except Exception as e:
            return error_response(str(e))

    def update(self, request, *args, **kwargs):
        try:
            response = super(UserTypeViewSet, self).update(request, partial=True)
            return successful_response(response.data)
        except Exception as e:
            return error_response(str(e))

    def destroy(self, request, *args, **kwargs):
        try:
            UserType.objects.filter(pk=kwargs['pk']).update(is_active=0)
            return successful_response({})
        except Exception as e:
            return error_response(str(e))
