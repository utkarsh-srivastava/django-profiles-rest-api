from rest_framework import serializers

class HelloSerilizer(serializers.Serializer):
    """Serializes a name fields for testing out APIVIEW"""

    name = serializers.CharField(max_length=10)
