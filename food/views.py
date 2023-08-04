from rest_framework import generics
from food.models import Food, Diet, Dish
from food.serializers import FoodSerializer, UserSerializer, DietSerializer, DishSerializer
from rest_framework import permissions
from food.permissions import IsUserOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from accounts.models import User


class FoodList(generics.ListAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['no', 'energy', "moisture",
                       "protein", "phosphorus", "potassium", "natrium"]


class FoodDetail(generics.RetrieveAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer


class DietList(generics.ListCreateAPIView):
    queryset = Diet.objects.all()
    serializer_class = DietSerializer

    def perform_create(self, serializer):
        serializer.save(userid=self.request.user)


class DietDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Diet.objects.all()
    serializer_class = DietSerializer


class DishList(generics.ListCreateAPIView):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer

    def perform_create(self, serializer):
        serializer.save(userid=self.request.user)


class DishDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
