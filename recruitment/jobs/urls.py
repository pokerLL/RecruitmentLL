from django.urls import path

from jobs.views import JobViewSet,CityViewSet,ResumeViewSet,upload
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'job',JobViewSet,basename='job')
router.register(r'city',CityViewSet,basename='city')
router.register(r'resume',ResumeViewSet,basename='resume')


urlpatterns = router.urls

urlpatterns +=[
    path('upload',upload),
]