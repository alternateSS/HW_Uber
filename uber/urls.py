from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from account import views as acc_view
from service import views as ser_view

acc_router = DefaultRouter()
acc_router.register('register', acc_view.ProfileRegisterAPIView)

ser_router = DefaultRouter()
ser_router.register('taxi', ser_view.TaxiViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/auth/', include('rest_framework.urls')),
    path('api/account/', include(acc_router.urls)),
    path('api/service/', include(ser_router.urls)),
    path('api/service/taxi/<int:pk>/order/', ser_view.OrderViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('api/service/taxi/<int:pk>/order/<int:id>', ser_view.OrderViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy'
    }))
]
