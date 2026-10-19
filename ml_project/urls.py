from django.contrib import admin
from django.urls import path
from predictor.views import PredictAPI

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/predict/', PredictAPI.as_view(), name='predict'),
]