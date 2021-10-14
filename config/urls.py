from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from main_app import views

router = routers.DefaultRouter()
router.register('person', views.PersonViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),

    # django-rest
    path('api-auth/', include('rest_framework.urls', namespace="rest_framework")),
    path('', include(router.urls)),

    # for complex query
    path('main_app/', include('main_app.urls')),
]
