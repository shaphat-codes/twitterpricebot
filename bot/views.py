from django.shortcuts import render
from django_celery_results.models import TaskResult
from . serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response


from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Create your views here.
    

@api_view(['GET'])
def get_latest_result(request, task):
    latest_result = TaskResult.objects.filter(periodic_task_name=task).order_by('-id')[0]
    serializer = TaskResultSerializer(latest_result)
    return Response(serializer.data)

