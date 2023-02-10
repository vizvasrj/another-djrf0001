from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django import http
from django.urls import reverse
from .forms import CsvFileUpload
from  rest_framework.decorators import parser_classes
from  rest_framework.parsers import FileUploadParser, MultiPartParser
import pandas as pd
import io
from .tasks import someting
import uuid
from .serializers import (
    ItemSerializer, TaskSerializer, DemoModelSerializer
)
from .models import Item, Task, DemoModel
from django.shortcuts import get_object_or_404
import django_filters
from rest_framework.pagination import PageNumberPagination

@api_view(['GET'])
def get_data(request):
    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def add_data(request):
    serializer = ItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['GET', 'POST'])
def tasks(request):
    if request.method == "POST":
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    items = Task.objects.all()
    serializer = TaskSerializer(items, many=True)
    return Response(serializer.data)


@api_view(['GET', 'DELETE'])
def tasks_detail(request, pk):
    if request.method == "DELETE":
        try:
            Task.objects.filter(id=pk).delete()
            return http.HttpResponse("404")
        except Task.DoesNotExist:
            raise http.Http404
    try:
        items = Task.objects.get(id=pk)
    except Task.DoesNotExist:
        raise http.Http404

    serializer = TaskSerializer(items)
    return Response(serializer.data)


import csv

class FileUploadView(APIView):
    parser_classes = [MultiPartParser]

    def put(self, request, filename, format=None):
        file_obj = request.data['image']
        # eader = csv.reader(file_obj)
        # for row in eader:
        #     print(row)

        # with open("aaa.csv", "wb") as hh:
        #     hh.write(file_obj.read())
        # for chunk in file_obj.chunks():
        #     # destination.write(chunk)
        # someting.delay("aaa")
        # for chunk in file_obj:
        #     print(chunk)

        
        # import time
        filename = str(uuid.uuid4()) + '.csv'
        destination = open('./' + filename, 'wb')
        for chunk in file_obj.chunks():
            destination.write(chunk)
            
        destination.close() 

        someting.delay(filename)

        # df = pd.read_csv(io.StringIO(file_obj.read().decode('utf-8')), delimiter=',')
        
        # print(df.columns)
        # destination.close()
        # ...
        # do some stuff with uploaded file
        # ...
        return Response(status=204)


from rest_framework import generics

class SmallPagesPagination(PageNumberPagination):  
    page_size = 50

class UserListView(generics.ListAPIView):
    queryset = DemoModel.objects.all()
    serializer_class = DemoModelSerializer
    # filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    ordering_filter = ('year', 'name', )
    pagination_class = SmallPagesPagination



# file_list = []
# for root, _, filenames in os.walk("./"):
#     for filename in filenames:
#         file_list.append(os.path.join(root, filename))

# for x in file_list:
#     print(x)