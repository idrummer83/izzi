from rest_framework import serializers

from .models import Customer


class AllUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = (
            'id', 'first_name', 'last_name', 'date_birthday', 'date_register'
        )


class FileUploadSerializer(serializers.Serializer):
    file = serializers.FileField()

    class Meta:
        fields = ('file',)
