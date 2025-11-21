
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.http import JsonResponse

schema_view = get_schema_view(
   openapi.Info(
      title="ARCA ERP API",
      default_version='v1',
      description="API documentation for ARCA ERP",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

def health_check(request):
    return JsonResponse({"status": "ok"})

urlpatterns = [
    path("admin/", admin.site.urls),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('health/', health_check, name='health_check'),

    # Auth module
    path('api/auth/', include('apps.core.auth_core.urls')),

    # Core Business Layer
    path('api/finance_core/', include('apps.business.finance_core.urls')),
    path('api/cost_mgmt/', include('apps.business.cost_mgmt.urls')),
    path('api/material_core/', include('apps.business.material_core.urls')),
    path('api/order_mgmt/', include('apps.business.order_mgmt.urls')),
    path('api/warehouse_x/', include('apps.business.warehouse_x.urls')),
    path('api/asset_care/', include('apps.business.asset_care.urls')),
    path('api/prod_core/', include('apps.business.prod_core.urls')),
    path('api/quality_core/', include('apps.business.quality_core.urls')),

    # Human & Organizational
    path('api/people_core/', include('apps.hr.people_core.urls')),
    path('api/data_change/', include('apps.hr.data_change.urls')),
    path('api/talent_hub/', include('apps.hr.talent_hub.urls')),

    # Customer & Retail
    path('api/customer_360/', include('apps.retail.customer_360.urls')),
    path('api/lead_ops/', include('apps.retail.lead_ops.urls')),
    path('api/service_desk/', include('apps.retail.service_desk.urls')),
    path('api/loyalty_plus/', include('apps.retail.loyalty_plus.urls')),
    path('api/promo_core/', include('apps.retail.promo_core.urls')),
    path('api/retail_pos/', include('apps.retail.retail_pos.urls')),
    path('api/checkout/', include('apps.retail.checkout.urls')),
    path('api/sync_hub/', include('apps.retail.sync_hub.urls')),
    path('api/retail_hub/', include('apps.retail.retail_hub.urls')),
    path('api/price_core/', include('apps.retail.price_core.urls')),

    # Supply Chain & Procurement
    path('api/supply_core/', include('apps.scm.supply_core.urls')),
    path('api/fleet_ops/', include('apps.scm.fleet_ops.urls')),
    path('api/purchase_hub/', include('apps.scm.purchase_hub.urls')),

    # Finance Extensions
    path('api/pay_link/', include('apps.business.pay_link.urls')),
    path('api/tax_core/', include('apps.business.tax_core.urls')),

    # Integration & Infrastructure
    path('api/event_core/', include('apps.core.event_core.urls')),
    path('api/service_bridge/', include('apps.core.service_bridge.urls')),
    path('api/data_hub/', include('apps.core.data_hub.urls')),
    path('api/admin_core/', include('apps.core.admin_core.urls')),

    # Analytics & Governance
    path('api/data_insights/', include('apps.analytics.data_insights.urls')),
    path('api/compliance_core/', include('apps.analytics.compliance_core.urls')),
    path('api/trace_core/', include('apps.analytics.trace_core.urls')),
    path('api/forecast_x/', include('apps.analytics.forecast_x.urls')),
]
