from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from users.views import UserViewSet, UserActivityViewSet, UserGoalViewSet
from food.views import FoodViewSet
from logs.views import UserFoodLogViewSet, CalorieRequirementViewSet, UserFoodRecommendationViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'user-activities', UserActivityViewSet)
router.register(r'user-goals', UserGoalViewSet)
router.register(r'foods', FoodViewSet)
router.register(r'user-food-logs', UserFoodLogViewSet)
router.register(r'calorie-requirements', CalorieRequirementViewSet)
router.register(r'user-food-recommendations', UserFoodRecommendationViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
