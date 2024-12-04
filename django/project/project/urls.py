
from django.contrib import admin
from django.urls import path, include
from blogapp import views
 
from django.urls import re_path # new
from rest_framework import permissions # new
from drf_yasg.views import get_schema_view # new
from drf_yasg import openapi # new

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blogapi/', views.BlogApi.as_view()),
    # path('blogmodify/', views.BlogModify.as_view()),
    path('blogapi/<int:pk>', views.BlogModify.as_view()),
    path('api-auth/', include('rest_framework.urls')),
    
    path('', include('dj_rest_auth.urls')), #for login.logout, and reset password

    path('api/dj-rest-auth-registration/', include('dj_rest_auth.registration.urls')),# for registration

    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
