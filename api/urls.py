from django.urls import path, include
from rest_framework_nested import routers

from api import views

router =routers.DefaultRouter()
router.register('soldiers', views.SoldierViewSet, basename='soldiers')
router.register('documents', views.DocumentViewSet, basename='documents')
router.register('announcements', views.AnnouncementViewSet, basename='announcements')
router.register('send', views.SendDocument, basename='send')

# urlpatterns = [
#     path('', include(router.urls)),
#     path('send', views.SendDocument.as_view(), name='send')
# ]

urlpatterns = router.urls