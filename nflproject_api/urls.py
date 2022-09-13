from django.urls import path
from . import views

urlpatterns = [
    path('api/team', views.TeamList.as_view(), name='team_list'), # api/team will be routed to the teamList view for handling
    path('api/team/<int:pk>', views.TeamDetail.as_view(), name='team_detail'), # api/team will be routed to the teamDetail view for handling
]
