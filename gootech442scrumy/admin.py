from django.contrib import admin
from .models import ScrumyGoals, ScrumyHistory, GoalStatus
# Register your models here.



class ScrumyGoalsAdmin(admin.ModelAdmin):
    list_display = ('goal_id','goal_name','created_by', 'moved_by', 'owner', 'goal_status', 'user')


admin.site.register(ScrumyGoals,ScrumyGoalsAdmin)
admin.site.register(ScrumyHistory)
admin.site.register(GoalStatus)
