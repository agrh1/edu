from django.urls import path
from .views import ServerAddView, ServerViewSet, ServerDetailView, ServerShortViewSet


urlpatterns = [
    path('servers', ServerViewSet.as_view()),
    path('servers/status', ServerShortViewSet.as_view()),
    path('servers/<int:pk>', ServerDetailView.as_view()),
    path('servers/add', ServerAddView.as_view()),
]