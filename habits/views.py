from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated

from habits.models import Habit
from habits.paginators import HabitPaginator
from users.permissions import IsOwner
from habits.serializers import HabitSerializer


class HabitListView(ListAPIView):
    """Отображение списка привычек текущего пользователя"""
    serializer_class = HabitSerializer
    pagination_class = HabitPaginator
    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user)


class PublicHabitListView(ListAPIView):
    """Отображение списка публичных привычек"""
    serializer_class = HabitSerializer

    def get_queryset(self):
        return Habit.objects.filter(is_public=True)


class HabitCreateView(CreateAPIView):
    """Создание привычки"""
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        new_habit = serializer.save()
        new_habit.user = self.request.user
        new_habit.save()


class HabitDetailView(RetrieveAPIView):
    """Отображение одной привычки"""
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated, IsOwner]


class HabitUpdateView(UpdateAPIView):
    """Изменение привычки"""
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated, IsOwner]


class HabitDeleteView(DestroyAPIView):
    """Удаление привычки"""
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated, IsOwner]
