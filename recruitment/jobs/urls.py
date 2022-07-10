from jobs.views import JobViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'jobs',JobViewSet,basename='jobs')

urlpatterns = router.urls