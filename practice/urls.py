from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^SeasonalTrainingPlan/', views.SeasonalTrainingPlan.as_view(), name='SeasonalTrainingPlan'),
    url(r'^WeeklyTrainingPlan/', views.WeeklyTrainingPlan.as_view(), name='WeeklyTrainingPlan'),
    url(r'^DailyTrainingPlan/', views.DailyTrainingPlan.as_view(), name='DailyTrainingPlan')
]
