from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ChartOfAccountsViewSet, JournalViewSet, AccountsPayableViewSet, AccountsReceivableViewSet, BankAccountViewSet

router = DefaultRouter()
router.register(r'chart-of-accounts', ChartOfAccountsViewSet)
router.register(r'journals', JournalViewSet)
router.register(r'ap', AccountsPayableViewSet)
router.register(r'ar', AccountsReceivableViewSet)
router.register(r'bank-accounts', BankAccountViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
