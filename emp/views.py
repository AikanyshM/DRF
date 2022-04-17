from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, DestroyAPIView, RetrieveAPIView
from .models import Position, Employee
from .serializers import PositionSerializer, EmployeeSerializer
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework.mixins import CreateModelMixin, ListModelMixin, UpdateModelMixin, DestroyModelMixin, RetrieveModelMixin


class PositionCreateAPIView(CreateAPIView):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer

class PositionListAPIView(ListAPIView):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer

class PositionDestroyAPIView(DestroyAPIView):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer

class PositionUpdateAPIView(UpdateAPIView):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer

class PositionRetrieveAPIView(RetrieveAPIView):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer

class EmployeeGenericViewSet(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def get_queryset(self):
        queryset = Employee.objects.all()
        if self.request.method == "GET":
            query = self.request.GET.get('query')
            if query and query != '':
                queryset = queryset.filter(name__icontains=query)
        return queryset