from rest_framework import routers

from core.user.viewsets import UserViewSet
from core.auth.viewsets import RegisterViewSet,LoginViewSet
router = routers.SimpleRouter()

router.register(r'<int:pk>/',UserViewSet,basename='user')
router.register(r'',UserViewSet,basename='user')
router.register(r'auth/register', RegisterViewSet,
    basename='auth-register')
router.register(r'auth/login', LoginViewSet,
    basename='auth-login')
urlpatterns = [*router.urls,] 
