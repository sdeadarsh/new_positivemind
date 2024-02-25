from django.shortcuts import render
from rest_framework import viewsets, permissions, status
from .models import Doctor, Appointment, AppointmentMaster, Feedback, Precipitation
from .serializers import DoctorSerializer, AppointmentSerializer, AppointmentMasterSerializer, FeedbackSerializer, \
    PrecipitationSerializer
from positivemind.utils import successful_response, error_response
from django.core import paginator


# Create your views here.
class AppointmentViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    serializer_class = AppointmentSerializer
    queryset = Appointment.objects.all()
    http_method_names = ['get', 'post', 'patch', 'delete', 'put']

    def create(self, request, *args, **kwargs):
        try:
            response = super(AppointmentViewSet, self).create(request, *args, **kwargs)
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
            response = super(AppointmentViewSet, self).list(request, *args, **kwargs)
            return successful_response(response.data)
        except Exception as e:
            return error_response(str(e))

    def retrieve(self, request, *args, **kwargs):
        try:
            response = super(AppointmentViewSet, self).retrieve(request, *args, **kwargs)
            return successful_response(response.data)
        except Exception as e:
            return error_response(str(e))

    def update(self, request, *args, **kwargs):
        try:
            response = super(AppointmentViewSet, self).update(request, partial=True)
            return successful_response(response.data)
        except Exception as e:
            return error_response(str(e))

    def destroy(self, request, *args, **kwargs):
        try:
            Appointment.objects.filter(pk=kwargs['pk']).update(is_active=0)
            return successful_response({})
        except Exception as e:
            return error_response(str(e))


class AppointmentMasterViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    serializer_class = AppointmentMasterSerializer
    queryset = AppointmentMaster.objects.all()
    http_method_names = ['get', 'post', 'patch', 'delete', 'put']

    def create(self, request, *args, **kwargs):
        try:
            response = super(AppointmentMasterViewSet, self).create(request, *args, **kwargs)
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
            response = super(AppointmentMasterViewSet, self).list(request, *args, **kwargs)
            return successful_response(response.data)
        except Exception as e:
            return error_response(str(e))

    def retrieve(self, request, *args, **kwargs):
        try:
            response = super(AppointmentMasterViewSet, self).retrieve(request, *args, **kwargs)
            return successful_response(response.data)
        except Exception as e:
            return error_response(str(e))

    def update(self, request, *args, **kwargs):
        try:
            response = super(AppointmentMasterViewSet, self).update(request, partial=True)
            return successful_response(response.data)
        except Exception as e:
            return error_response(str(e))

    def destroy(self, request, *args, **kwargs):
        try:
            AppointmentMaster.objects.filter(pk=kwargs['pk']).update(is_active=0)
            return successful_response({})
        except Exception as e:
            return error_response(str(e))


class DoctorViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    serializer_class = DoctorSerializer
    queryset = Doctor.objects.all()
    http_method_names = ['get', 'post', 'patch', 'delete', 'put']

    def create(self, request, *args, **kwargs):
        try:
            response = super(DoctorViewSet, self).create(request, *args, **kwargs)
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
            response = super(DoctorViewSet, self).list(request, *args, **kwargs)
            return successful_response(response.data)
        except Exception as e:
            return error_response(str(e))

    def retrieve(self, request, *args, **kwargs):
        try:
            response = super(DoctorViewSet, self).retrieve(request, *args, **kwargs)
            return successful_response(response.data)
        except Exception as e:
            return error_response(str(e))

    def update(self, request, *args, **kwargs):
        try:
            response = super(DoctorViewSet, self).update(request, partial=True)
            return successful_response(response.data)
        except Exception as e:
            return error_response(str(e))

    def destroy(self, request, *args, **kwargs):
        try:
            Doctor.objects.filter(pk=kwargs['pk']).update(is_active=0)
            return successful_response({})
        except Exception as e:
            return error_response(str(e))


class FeedbackViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    serializer_class = FeedbackSerializer
    queryset = Feedback.objects.all()
    http_method_names = ['get', 'post', 'patch', 'delete', 'put']

    def create(self, request, *args, **kwargs):
        try:
            response = super(FeedbackViewSet, self).create(request, *args, **kwargs)
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
            response = super(FeedbackViewSet, self).list(request, *args, **kwargs)
            return successful_response(response.data)
        except Exception as e:
            return error_response(str(e))

    def retrieve(self, request, *args, **kwargs):
        try:
            response = super(FeedbackViewSet, self).retrieve(request, *args, **kwargs)
            return successful_response(response.data)
        except Exception as e:
            return error_response(str(e))

    def update(self, request, *args, **kwargs):
        try:
            response = super(FeedbackViewSet, self).update(request, partial=True)
            return successful_response(response.data)
        except Exception as e:
            return error_response(str(e))

    def destroy(self, request, *args, **kwargs):
        try:
            Feedback.objects.filter(pk=kwargs['pk']).update(is_active=0)
            return successful_response({})
        except Exception as e:
            return error_response(str(e))


class PrecipitationViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    serializer_class = PrecipitationSerializer
    queryset = Precipitation.objects.all()
    http_method_names = ['get', 'post', 'patch', 'delete', 'put']

    def create(self, request, *args, **kwargs):
        try:
            response = super(PrecipitationViewSet, self).create(request, *args, **kwargs)
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
            response = super(PrecipitationViewSet, self).list(request, *args, **kwargs)
            return successful_response(response.data)
        except Exception as e:
            return error_response(str(e))

    def retrieve(self, request, *args, **kwargs):
        try:
            response = super(PrecipitationViewSet, self).retrieve(request, *args, **kwargs)
            return successful_response(response.data)
        except Exception as e:
            return error_response(str(e))

    def update(self, request, *args, **kwargs):
        try:
            response = super(PrecipitationViewSet, self).update(request, partial=True)
            return successful_response(response.data)
        except Exception as e:
            return error_response(str(e))

    def destroy(self, request, *args, **kwargs):
        try:
            Precipitation.objects.filter(pk=kwargs['pk']).update(is_active=0)
            return successful_response({})
        except Exception as e:
            return error_response(str(e))
