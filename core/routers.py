from rest_framework import routers

from core.user.viewsets import UserViewSet

router = routers.SimpleRouter()

router.register(r'<int:pk>/',UserViewSet,basename='user')
router.register(r'',UserViewSet,basename='user')
urlpatterns = [*router.urls,] 
