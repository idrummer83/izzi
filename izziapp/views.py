from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics

import datetime, csv, io

from .util import date_format

from .models import Customer

from izziapp.serializers import AllUsersSerializer, FileUploadSerializer


class UsersListView(generics.ListAPIView):
    queryset = Customer.objects.all()
    serializer_class = AllUsersSerializer


class UserRegisterView(generics.RetrieveAPIView):
    lookup_field = 'date_register'
    queryset = Customer.objects.all()
    serializer_class = AllUsersSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(datetime.datetime.strptime(date_format(kwargs['date_register']), "%Y-%m-%d").date())


class MyUploadView(generics.CreateAPIView):
    serializer_class = FileUploadSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        file = serializer.validated_data['file']
        decoded_file = file.read().decode()
        io_string = io.StringIO(decoded_file)
        reader = csv.reader(io_string)
        next(reader)
        for row in reader:
            Customer.objects.get_or_create(
                first_name=row[0], last_name=row[1],
                date_birthday=datetime.datetime.strptime(date_format(row[2]), '%Y-%m-%d').date(),
                date_register=datetime.datetime.strptime(date_format(row[3]), "%Y-%m-%d").date()
            )
        return Response(status=status.HTTP_201_CREATED)

