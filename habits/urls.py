from django.urls import path

from habits.views import (HabitListView, HabitCreateView, HabitDetailView, HabitUpdateView,
                          HabitDeleteView, PublicHabitListView)
from habits.apps import HabitsConfig

app_name = HabitsConfig.name

urlpatterns = [
    path('', HabitListView.as_view(), name='habit_list'),
    path('public/', PublicHabitListView.as_view(), name='public_habit_list'),
    path('create/', HabitCreateView.as_view(), name='habit_create'),
    path('<int:pk>/', HabitDetailView.as_view(), name='habit_detail'),
    path('<int:pk>/update/', HabitUpdateView.as_view(), name='habit_update'),
    path('<int:pk>/delete/', HabitDeleteView.as_view(), name='habit_delete'),
]
