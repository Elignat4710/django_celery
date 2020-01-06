from rest_framework import routers
from . import views


router = routers.DefaultRouter()

router.register(r'companies', views.CompanyViewSet)
router.register(r'managers', views.ManagerViewSet)
router.register(r'work', views.WorkViewSet)
router.register(r'worker', views.WorkerViewSet)
router.register(r'work_place', views.WorkPlaceViewSet)
