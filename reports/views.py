from rest_framework.response import Response
from rest_framework.views import APIView
from .models import ReportNumber, ReportNumberByUser
from django.http import Http404
from rest_framework import status
from .serializers import ReportNumberSerializer, ReportNumberByUserSerializer   


class ReportNumberView(APIView):

    def get(self, request, format=None, *args, **kwargs):
        queryset = ReportNumber.objects.all()
        serializer = ReportNumberSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ReportNumberSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class ReportNumberByUserView(APIView):

    def post(self, request, format=None):
        serializer = ReportNumberByUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)     


class ReportNumberByUserDetailView(APIView):

    def get_object(self, pk):
        try:
            return ReportNumberByUser.objects.get(pk=pk)
        except ReportNumberByUser.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        queryset = self.get_object(pk)
        serializer = ReportNumberByUserSerializer(queryset)  
        return Response(serializer.data)
        
    def put(self, request, pk, format=None):
        queryset = self.get_object(pk)
        serializer = ReportNumberByUserSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        queryset = self.get_object(pk)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
