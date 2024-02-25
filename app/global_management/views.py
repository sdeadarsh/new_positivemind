from django.shortcuts import render
from rest_framework import viewsets, permissions, status
from .models import Address, ThinkingMaster, Thinking, QuestionerMaster, Questioner
from .serializers import QuestionerSerializer, QuestionerMasterSerializer, AddressSerializer, ThinkingSerializer, \
    ThinkingMasterSerializer
from positivemind.utils import successful_response, error_response
from django.core import paginator


# Create your views here.


class AddressViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    serializer_class = AddressSerializer
    queryset = Address.objects.all()
    http_method_names = ['get', 'post', 'patch', 'delete', 'put']

    def create(self, request, *args, **kwargs):
        try:
            response = super(AddressViewSet, self).create(request, *args, **kwargs)
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
            response = super(AddressViewSet, self).list(request, *args, **kwargs)
            return successful_response(response.data)
        except Exception as e:
            return error_response(str(e))

    def retrieve(self, request, *args, **kwargs):
        try:
            response = super(AddressViewSet, self).retrieve(request, *args, **kwargs)
            return successful_response(response.data)
        except Exception as e:
            return error_response(str(e))

    def update(self, request, *args, **kwargs):
        try:
            response = super(AddressViewSet, self).update(request, partial=True)
            return successful_response(response.data)
        except Exception as e:
            return error_response(str(e))

    def destroy(self, request, *args, **kwargs):
        try:
            Address.objects.filter(pk=kwargs['pk']).update(is_active=0)
            return successful_response({})
        except Exception as e:
            return error_response(str(e))


class ThinkingMasterViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    serializer_class = ThinkingMasterSerializer
    queryset = ThinkingMaster.objects.all()
    http_method_names = ['get', 'post', 'patch', 'delete', 'put']

    def create(self, request, *args, **kwargs):
        try:
            response = super(ThinkingMasterViewSet, self).create(request, *args, **kwargs)
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
            response = super(ThinkingMasterViewSet, self).list(request, *args, **kwargs)
            return successful_response(response.data)
        except Exception as e:
            return error_response(str(e))

    def retrieve(self, request, *args, **kwargs):
        try:
            response = super(ThinkingMasterViewSet, self).retrieve(request, *args, **kwargs)
            return successful_response(response.data)
        except Exception as e:
            return error_response(str(e))

    def update(self, request, *args, **kwargs):
        try:
            response = super(ThinkingMasterViewSet, self).update(request, partial=True)
            return successful_response(response.data)
        except Exception as e:
            return error_response(str(e))

    def destroy(self, request, *args, **kwargs):
        try:
            ThinkingMaster.objects.filter(pk=kwargs['pk']).update(is_active=0)
            return successful_response({})
        except Exception as e:
            return error_response(str(e))


class ThinkingViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    serializer_class = ThinkingSerializer
    queryset = Thinking.objects.all()
    http_method_names = ['get', 'post', 'patch', 'delete', 'put']

    def create(self, request, *args, **kwargs):
        try:
            response = super(ThinkingViewSet, self).create(request, *args, **kwargs)
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
            response = super(ThinkingViewSet, self).list(request, *args, **kwargs)
            return successful_response(response.data)
        except Exception as e:
            return error_response(str(e))

    def retrieve(self, request, *args, **kwargs):
        try:
            response = super(ThinkingViewSet, self).retrieve(request, *args, **kwargs)
            return successful_response(response.data)
        except Exception as e:
            return error_response(str(e))

    def update(self, request, *args, **kwargs):
        try:
            response = super(ThinkingViewSet, self).update(request, partial=True)
            return successful_response(response.data)
        except Exception as e:
            return error_response(str(e))

    def destroy(self, request, *args, **kwargs):
        try:
            Thinking.objects.filter(pk=kwargs['pk']).update(is_active=0)
            return successful_response({})
        except Exception as e:
            return error_response(str(e))


class QuestionerMasterViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    serializer_class = QuestionerMasterSerializer
    queryset = QuestionerMaster.objects.all()
    http_method_names = ['get', 'post', 'patch', 'delete', 'put']

    def create(self, request, *args, **kwargs):
        try:
            response = super(QuestionerMasterViewSet, self).create(request, *args, **kwargs)
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
            response = super(QuestionerMasterViewSet, self).list(request, *args, **kwargs)
            return successful_response(response.data)
        except Exception as e:
            return error_response(str(e))

    def retrieve(self, request, *args, **kwargs):
        try:
            response = super(QuestionerMasterViewSet, self).retrieve(request, *args, **kwargs)
            return successful_response(response.data)
        except Exception as e:
            return error_response(str(e))

    def update(self, request, *args, **kwargs):
        try:
            response = super(QuestionerMasterViewSet, self).update(request, partial=True)
            return successful_response(response.data)
        except Exception as e:
            return error_response(str(e))

    def destroy(self, request, *args, **kwargs):
        try:
            QuestionerMaster.objects.filter(pk=kwargs['pk']).update(is_active=0)
            return successful_response({})
        except Exception as e:
            return error_response(str(e))


class QuestionerViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    serializer_class = QuestionerSerializer
    queryset = Questioner.objects.all()
    http_method_names = ['get', 'post', 'patch', 'delete', 'put']

    def create(self, request, *args, **kwargs):
        try:
            response = super(QuestionerViewSet, self).create(request, *args, **kwargs)
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
            response = super(QuestionerViewSet, self).list(request, *args, **kwargs)
            return successful_response(response.data)
        except Exception as e:
            return error_response(str(e))

    def retrieve(self, request, *args, **kwargs):
        try:
            response = super(QuestionerViewSet, self).retrieve(request, *args, **kwargs)
            return successful_response(response.data)
        except Exception as e:
            return error_response(str(e))

    def update(self, request, *args, **kwargs):
        try:
            response = super(QuestionerViewSet, self).update(request, partial=True)
            return successful_response(response.data)
        except Exception as e:
            return error_response(str(e))

    def destroy(self, request, *args, **kwargs):
        try:
            Questioner.objects.filter(pk=kwargs['pk']).update(is_active=0)
            return successful_response({})
        except Exception as e:
            return error_response(str(e))
