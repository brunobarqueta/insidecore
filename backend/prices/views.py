from django.shortcuts import render
from rest_framework.exceptions import MethodNotAllowed
from tools_rest.response_view import success, bad_request
from . import models, serializers
from prices.tools import constantes
from prices.tools.helpers import validate_if_id_exist
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
        if serializer.is_valid():
            serializer.save()
            return success(serializer.data)
        
        first_error = next(iter(serializer.errors.values()))[0]
        return bad_request(first_error)
    
class PriceGetPutDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Price.objects.all()
    serializer_class = serializers.PriceGetPutSerializer

    def get_serializer_class(self):
        if self.request.method == 'GET' or self.request.method == 'PUT':
            return serializers.PriceGetPutSerializer
        elif self.request.method == 'DELETE':
            return serializers.PriceDeleteSerializer
        return self.serializer_class
    
    def partial_update(self, request, *args, **kwargs):
        raise MethodNotAllowed("PATCH method is not allowed")
    
    def retrieve(self, request, *args, **kwargs):
        validate = validate_if_id_exist(self)
        if not validate.success:
            return bad_request(validate.errors)
        
        serializer = self.get_serializer(validate.result)
        return success(serializer.data)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', True)
        
        validate = validate_if_id_exist(self)
        if not validate.success:
            return bad_request(validate.errors)
        
        serializer = self.get_serializer(validate.result, data=request.data, partial=partial)
        if serializer.is_valid():
            self.perform_update(serializer)
            return success(serializer.data)
            
        first_error = next(iter(serializer.errors.values()))[0]
        return bad_request(first_error)

    def destroy(self, request, *args, **kwargs):
        validate = validate_if_id_exist(self)
        if not validate.success:
            return bad_request(validate.errors)
        
        self.perform_destroy(validate.result)
        return success(True)