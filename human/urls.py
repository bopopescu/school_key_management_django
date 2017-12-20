from django.urls import path
from human.views import HumanListView, HumanDetailView

app_name = 'human'

urlpatterns = [
    path('', HumanListView.as_view(), name='list'),
    path('<int:pk>', HumanDetailView.as_view(), name='detail' )
]