from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('v1/', include('reports.urls', namespace="reports")),
]