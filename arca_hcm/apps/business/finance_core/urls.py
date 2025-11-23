from django.urls import path, include

urlpatterns = [
    path('api/', include('apps.business.finance_core.api.urls')),
]
