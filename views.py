# Create your views here.
from rest_framework import viewsets, status
from django.utils import timezone

from django.http import Http404
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


class LargeResultsSetPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'pageSize'
    max_page_size = 1000

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'pageSize'
    max_page_size = 100

class TemporalModelViewSet(viewsets.ModelViewSet):
    pagination_class = StandardResultsSetPagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    ordering_fields = '__all__'

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            self.model.objects.filter(pk=instance.pk, vflag=1).update(
                vt=timezone.now(), vflag=0, vu='dashboard')
        except Http404:
            pass
        return Response(status=status.HTTP_200_OK)