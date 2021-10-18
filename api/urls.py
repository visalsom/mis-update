from rest_framework.routers import DefaultRouter

from api import views

router = DefaultRouter()
router.register('soldiers', views.SoldierViewSet)
router.register('documents', views.DocumentViewSet, basename='documents')
router.register('announcements', views.AnnouncementViewSet)

urlpatterns = router.urls