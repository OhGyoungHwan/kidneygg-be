from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from food import views


urlpatterns = [
    path('food/', views.FoodList.as_view()),
    path('food/<int:pk>/', views.FoodDetail.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('diet/', views.DietList.as_view()),
    path('diet/<int:pk>/', views.DietDetail.as_view()),
    path('dish/', views.DishList.as_view()),
    path('dish/<int:pk>/', views.DishDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]
