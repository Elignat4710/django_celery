from rest_framework import serializers
from .models import (
    Company, Manager, Worker, Work, WorkPlace,
    WorkTime
)


class WorkTimeSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = WorkTime
        fields = ('id', 'date_start', 'date_end', 'hours_worked')


class WorkPlaceSerializer(serializers.HyperlinkedModelSerializer):
    work_name = serializers.ReadOnlyField(source='work_name.name')
    worker_name = serializers.ReadOnlyField(source='worker_name.name')

    class Meta:
        model = WorkPlace
        fields = ('url', 'name', 'work_name', 'worker_name', 'status',)


class WorkerSerializer(serializers.HyperlinkedModelSerializer):
    workplace = serializers.SerializerMethodField('work_place')

    def work_place(self, worker):
        if WorkPlace.objects.filter(worker_name=worker).exists():
            wp = WorkPlace.objects.get(worker_name=worker)
            return f'{wp.name}'
        return 'Not working now'

    class Meta:
        model = Worker
        fields = ('url', 'id', 'name', 'workplace')


class WorkSerializer(serializers.HyperlinkedModelSerializer):
    company = serializers.ReadOnlyField(source='com_name.name')

    class Meta:
        model = Work
        fields = ('url', 'id', 'name', 'company', 'com_name')


class ManagerSerializer(serializers.HyperlinkedModelSerializer):
    company_name = serializers.ReadOnlyField(source='company.name')

    class Meta:
        model = Manager
        fields = ('url', 'id', 'name', 'email', 'company_name', 'company')


class CompanyDetailSerializer(serializers.HyperlinkedModelSerializer):
    managers = ManagerSerializer(many=True)
    works = WorkSerializer(many=True)

    class Meta:
        model = Company
        fields = ('url', 'id', 'name', 'managers', 'works')


class CompanySerializer(serializers.HyperlinkedModelSerializer):
    managers = serializers.StringRelatedField(many=True)
    works = serializers.StringRelatedField(many=True)

    class Meta:
        model = Company
        fields = ('url', 'id', 'name', 'managers', 'works')


class WorkPlaceDetailSerializer(serializers.HyperlinkedModelSerializer):
    work_name = WorkSerializer()
    worker_name = WorkerSerializer()
    worktimes = WorkTimeSerializer(read_only=True, many=True)

    class Meta:
        model = WorkPlace
        fields = ('id', 'name', 'work_name', 'worker_name', 'status', 'worktimes')
