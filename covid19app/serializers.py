from rest_framework import serializers
from .models import Covid19C

class covid19Serializer(serializers.ModelSerializer):
    class Meta:
        model = Covid19C
        fields = "__all__"
