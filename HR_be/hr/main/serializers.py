from rest_framework import serializers
from .models import Worker, PostWorker, Enterprise, PostEnterprise


class WorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worker
        fields = '__all__'


class PostWorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostWorker
        fields = '__all__'


class EnterpriseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enterprise
        fields = '__all__'


class PostEnterpriseSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostEnterprise
        fields = '__all__'

