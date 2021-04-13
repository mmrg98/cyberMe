from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from check import views
from rest_framework_simplejwt.views import TokenObtainPairView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', TokenObtainPairView.as_view() , name='login'),
    path('signup/', views.SignUpAPIView.as_view(), name='register'),
    path('check-card/<str:card>/', views.CheckCard.as_view(), name='check-card'),

]

if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
