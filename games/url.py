# games/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Homepage view
    path('profile/<str:username>/', views.profile, name='profile'),  # User profile view
    path('game/<int:game_id>/', views.game_detail, name='game_detail'),  # Game detail view
    path('add-review/<int:game_id>/', views.add_review, name='add_review'),  # Add review view
    path('add-friend/<int:user_id>/', views.add_friend, name='add_friend'),  # Add friend view
    path('recommendations/', views.recommendations, name='recommendations'),  # Recommendations view
]
