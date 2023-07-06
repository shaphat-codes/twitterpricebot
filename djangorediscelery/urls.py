
from django.contrib import admin
from django.urls import path
from bot.views import get_latest_result

urlpatterns = [
    path('admin/', admin.site.urls),
    path('results/<str:task>', get_latest_result, name= "latest-result"),


]
