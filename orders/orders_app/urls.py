from django.conf.urls import url
from rest_framework import routers
from orders.orders_app.views import StudentViewSet, UniversityViewSet

router = routers.DefaultRouter()
router.register(r'students', StudentViewSet)
router.register(r'universities', UniversityViewSet)

urlpatterns = router.urls