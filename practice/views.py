from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
# Create your views here.
class SeasonalTrainingPlan(TemplateView):
    template_name = 'SeasonalTrainingPlan.html'


# Create your views here.
class WeeklyTrainingPlan(TemplateView):
    template_name = 'WeeklyTrainingPlan.html'


class DailyTrainingPlan(TemplateView):
    template_name = 'DailyTrainingPlan.html'