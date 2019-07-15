from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse
from .models import (
    GoalStatus,
    ScrumyGoals,
    ScrumyHistory
)
# Create your views here.

def index(request):
    goal_filter = ScrumyGoals.objects.filter(goal_name ="Learn Django")
    return HttpResponse(goal_filter)


def move_goal(request, goal_id):
    goal = get_object_or_404(ScrumyGoals, goal_id=goal_id)
    return HttpResponse(goal)

