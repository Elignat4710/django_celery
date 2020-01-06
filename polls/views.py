from .models import (
    Company, Work, Worker, WorkTime, Manager,
    WorkPlace
    )
import logging
from rest_framework import viewsets
from .serializers import (
    CompanySerializer, ManagerSerializer, WorkSerializer,
    WorkerSerializer, WorkPlaceSerializer, CompanyDetailSerializer,
    WorkPlaceDetailSerializer, WorkTimeSerializer
    )
from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status


logger = logging.getLogger('sentry_logger')


class WorkTimeViewSet(viewsets.ModelViewSet):
    queryset = WorkTime.objects.all()
    serializer_class = WorkTimeSerializer


class WorkPlaceViewSet(viewsets.ModelViewSet):
    queryset = WorkPlace.objects.all()
    permissions_classes = (permissions.IsAuthenticated,)

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return WorkPlaceDetailSerializer
        if self.action == 'create_worktime':
            return WorkTimeSerializer
        return WorkPlaceSerializer

    @action(methods=['post'], detail=True)
    def create_worktime(self, request, pk=None):
        wp = self.get_object()
        serializer = WorkTimeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(workplace=wp, work=wp.work_name,
                            worker=wp.worker_name)
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)

class WorkerViewSet(viewsets.ModelViewSet):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer
    permissions_classes = (permissions.IsAuthenticatedOrReadOnly,)


class WorkViewSet(viewsets.ModelViewSet):
    queryset = Work.objects.all()
    serializer_class = WorkSerializer
    permissions_classes = (permissions.IsAuthenticatedOrReadOnly,)


class ManagerViewSet(viewsets.ModelViewSet):
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer
    permissions_classes = (permissions.IsAuthenticatedOrReadOnly,)


class CompanyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Company.objects.all()

    def get_serializer_class(self):
        if self.action == 'create_manager':
            return ManagerSerializer
        elif self.action == 'create_work':
            return WorkSerializer
        elif self.action == 'retrieve':
            return CompanyDetailSerializer
        return CompanySerializer

    @action(methods=['post'], detail=True)
    def create_manager(self, request, pk=None):
        company = self.get_object()
        serializer = ManagerSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save(company=company)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['post'], detail=True)
    def create_work(self, request, pk=None):
        company = self.get_object()
        serializer = WorkSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save(com_name=company)
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)
