from django.urls import path
from .views import ServerAddView, ServerViewSet, ServerDetailView, ServerShortViewSet, ServerDataAddView


urlpatterns = [
    path('servers', ServerViewSet.as_view()),
    path('servers/status', ServerShortViewSet.as_view()),
    path('servers/<int:pk>', ServerDetailView.as_view()),
    path('servers/add', ServerAddView.as_view()),
    path('serverdata/add', ServerDataAddView.as_view()),

]