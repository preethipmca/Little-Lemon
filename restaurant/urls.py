#define URL route for index() view
from django.urls import include, path
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from .views import UserViewSet


router = DefaultRouter()
router.register(r'users', UserViewSet)
urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.MenuItemView.as_view(),name ='menu'),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
    path('', include(router.urls)),
    path('api-token-auth/', obtain_auth_token)

]

