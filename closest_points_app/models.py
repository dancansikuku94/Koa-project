from django.db import models
# Register models here.
class PointSet(models.Model):
    points = models.CharField(max_length=200)
    closest_points = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
