from django import http
from django.http import response
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

from profiles_api import serializers


class HelloApiView(APIView):
    """Test APIView"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Restun a list of ApiView features"""
        an_apiview = [
            'Uses HTTP Method as function (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most contorl over you application logic',
            'Is mapped manually to URLs',
        ]


        return Response({'message': 'Hello', 'an_apiview': an_apiview})


    def post(self, request):
        """Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})

        else:
            return Response(
                serializer.errors, 
                status=status.HTTP_400_BAD_REQUEST
                )

    def put(self, request, pk=None):
        """Handle updating an object"""    
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """Handle partial update of object"""
        return Response({'method': 'PATCH'})
        
    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({'method': 'DELETE'})

class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Return a hello messgae"""


        a_viewset = [
            'Uses Actions (list, create,retrive, update, partial_update)',
            'Automatically  maps to URL using Router',
            'Provides more functianality with less code',
        ]

        return Response({'message': 'Hello!',  'a_viewset': a_viewset})

    def create(self, request):
        """Create a new hellow msg"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message': message})

        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
    
    def retrive(self, request, pk=None):
        """Handle getting on object by its ID"""
        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """Handle updating an object"""
        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """Handle update part an object """
        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """Handle remove an object"""
        return Response({'http_method': 'DELETE'})