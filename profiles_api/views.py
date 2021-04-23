from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    """Test API View"""

    def get(self, request, format=None):
        """Return a list of API features"""

        an_apiview = [
            'Uses Http method as function (get, post, delete)',
            'Is similar to tradiotional django view',
            'Gives you the mose control over your application logic',
            'Is mapped manually to URLs'
        ]

        return Response({'message': 'Hello', 'an_apiview': an_apiview})
