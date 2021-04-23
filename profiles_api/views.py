from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers

class HelloApiView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerilizer

    def get(self, request, format=None):
        """Return a list of API features"""

        an_apiview = [
            'Uses Http method as function (get, post, delete)',
            'Is similar to tradiotional django view',
            'Gives you the mose control over your application logic',
            'Is mapped manually to URLs'
        ]

        return Response({'message': 'Hello', 'an_apiview': an_apiview})

    def post(self, request):
        """create a hello message with our name"""

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
        """Handling updating an object"""

        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """Handle a partical update of on object"""

        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """Delete an object"""

        return Response({'method': 'DELETE'})
