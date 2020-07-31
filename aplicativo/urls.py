# from django.urls import path

from aplicativo.views import PessoaViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', PessoaViewSet)
urlpatterns = router.urls


# urlpatterns = [

#     path('pessoa/list', view = views.PessoaList.as_view(), name = 'pessoa-list'),
#     path('pessoa/rud/<int:pk>', view= views.PessoaRetrieveUpdateDestroy.as_view(), name = 'pessoa-rud'),

# ]