from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
# Create your models here.


class GoalStatus(models.Model):
    status_name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'GoalStatus'

    def __str__(self):
        return self.status_name

class ScrumyGoals(models.Model):
    goal_id = models.AutoField(primary_key=True)
    goal_name = models.CharField(max_length=255)
    created_by = models.CharField(max_length=30)
    moved_by = models.CharField(max_length=30)
    owner = models.CharField(max_length=30)
    goal_status = models.ForeignKey(GoalStatus, on_delete=models.CASCADE)
    user = models.ForeignKey(User, models.CASCADE, related_name='users')

    class Meta:
        verbose_name_plural = 'SrumyGoals'


    def __str__(self):
        return self.goal_name

class ScrumyHistory(models.Model):
    goal = models.ForeignKey(ScrumyGoals, on_delete=models.CASCADE)
    moved_by = models.CharField(max_length=30)
    created_by = models.CharField(max_length=30)
    moved_from = models.CharField(max_length=30)
    moved_to = models.CharField(max_length=30)
    time_of_action = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name_plural = 'ScrumyHistories'





# goal_name, goal_id, created_by, moved_by, owner