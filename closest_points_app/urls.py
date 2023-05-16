from django.urls import path
from .views import PointSetAPIView

urlpatterns = [
    path('closest_points/', PointSetAPIView.as_view()),
]
