from django.contrib import admin
from django.urls import include, path

from rest_framework import routers
from browser import views

router = routers.DefaultRouter()
router.register(r'interface', views.task_detail_view)

urlpatterns = [
    path('', include('browser.urls')),
    path('tasksbrowser/administrator/', admin.site.urls),
    path('', include('browser.urls')),
    path('', include(router.urls)),
]