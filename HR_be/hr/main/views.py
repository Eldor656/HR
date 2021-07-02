from django.shortcuts import render
from .models import Enterprise, Worker, PostWorker, PostEnterprise
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import EnterpriseSerializer, WorkerSerializer, PostWorkerSerializer, PostEnterpriseSerializer


class WorkerView(APIView):
    def get(self, request):
        return Response({
            'ok': True,
            'data': WorkerSerializer(Worker.objects.all(), many=True).data
        })

    def post(self, request):
        return Response({
            'data': request.data
        })


class PostWorkerView(APIView):
    def get(self, request):
        return Response({
            'ok': True,
            'data': PostWorkerSerializer(PostWorker.objects.all(), many=True).data
        })

    def post(self, request):
        return Response({
            'data': request.data
        })


class EnterpriseView(APIView):
    def get(self, request):
        return Response({
            'ok': True,
            'data': EnterpriseSerializer(Enterprise.objects.all(), many=True).data
        })

    def post(self, request):
        return Response({
            'data': request.data
        })


class PostEnterpriseView(APIView):
    def get(self, request):
        return Response({
            'ok': True,
            'data': PostEnterpriseSerializer(PostEnterprise.objects.all(), many=True).data
        })

    def post(self, request):
        return Response({
            'data': request.data
        })

