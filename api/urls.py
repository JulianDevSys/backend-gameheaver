""" from django.urls import path, include
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register(r'register', views.PersonaViewSet, basename='persona')

urlpatterns = [
    path('', include(router.urls)),
]
 """
from django.urls import path
from api import views
from rest_framework_simplejwt.views import TokenRefreshView
urlpatterns = [
    path('register/', views.register, name='register'),
    path('', views.login_view, name='login_view'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('datos/',views.datas,name='datas' )
]