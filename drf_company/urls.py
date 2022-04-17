from django.contrib import admin
from django.urls import path, include
from emp import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('employee', views.EmployeeGenericViewSet, basename='employee')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create/', views.PositionCreateAPIView.as_view()),
    path('position/', views.PositionListAPIView.as_view()),
    path('update/<int:pk>/', views.PositionUpdateAPIView.as_view()),
    path('destroy/<int:pk>/', views.PositionDestroyAPIView.as_view()),
    path('retrieve/<int:pk>/', views.PositionRetrieveAPIView.as_view()),
    #path('emp/', views.EmployeeGenericViewSet.as_view({
        #'get': 'list',
        #'post': 'create'
    #})),
    #path('emp/<int:pk>/', views.EmployeeGenericViewSet.as_view({
        #'get': 'retrieve',
        #'post': 'update',
        #'delete':'destroy'
    #})),
    path('', include(router.urls)),



]
