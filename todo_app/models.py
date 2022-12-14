from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Tasks(models.Model):

    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000, blank=True, null=True)
    complete_status = models.BooleanField(default=False)
    create_time = models.DateTimeField(auto_now_add=True)