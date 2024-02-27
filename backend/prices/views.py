from django.shortcuts import render
from rest_framework.exceptions import MethodNotAllowed
from tools_rest.response_view import success
from . import models, serializers
from rest_framework import generics

class PriceListCreateView(generics.ListCreateAPIView):
    queryset = models.Price.objects.all()
    serializer_class = serializers.PriceListCreateSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return success(serializer.data)
        
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return success(serializer.data)
    
class PriceGetPutDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Price.objects.all()
    serializer_class = serializers.PriceGetPutSerializer

    def get_serializer_class(self):
        if self.request.method == 'GET' or self.request.method == 'PUT':
            return serializers.PriceGetPutSerializer
        elif self.request.method == 'DELETE':
            return serializers.PriceDeleteSerializer
        return serializers.PriceGetPutSerializer
    
    def partial_update(self, request, *args, **kwargs):
        raise MethodNotAllowed(request.method)
    
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return success(serializer.data)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', True)
        
        instance = self.get_object()
        data = request.data.copy()
        serializer_instance = self.serializer_class()
        for name in serializer_instance.fields:
            if data.get(name, None) is None:
                data[name] = getattr(instance, name)
            
        serializer = self.get_serializer(instance, data=data, partial=partial)
        if serializer.is_valid(raise_exception=True):
            self.perform_update(serializer)
            return success(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return success(True)