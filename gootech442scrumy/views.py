from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import (
    GoalStatus,
    ScrumyGoals,
    ScrumyHistory
)
import random
# Create your views here.

def index(request):
    goal_filter = ScrumyGoals.objects.filter(goal_name ="Learn Django")
    return HttpResponse(goal_filter)


def move_goal(request, goal_id):
    goal = get_object_or_404(ScrumyGoals, goal_id=goal_id)
    return HttpResponse(goal)


def add_goal(request):
    new_goal = ScrumyGoals.objects.create(
        goal_name = "Keep Learning Django",
        goal_id = random.randint(1000, 9999),
        created_by = "Louis",
        moved_by = "Louis",
        owner = "Louis",
        goal_status = GoalStatus.objects.get(status_name="Weekly Goal"),
        user = User.objects.get(username = "louis")
    )
    return HttpResponse(new_goal)

def home(request):
    goal_filter = ScrumyGoals.objects.filter(goal_name="Keep Learning Django")
    goal_output = ''.join([goal.goal_name for goal in ScrumyGoals.objects.all()])
    return HttpResponse(goal_filter)

