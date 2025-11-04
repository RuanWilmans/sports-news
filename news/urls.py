"""
news/urls.py

App routes for web pages and simple JSON APIs.
"""

from django.urls import path
from . import views

urlpatterns = [
    # Pages
    path("", views.home, name="home"),
    path("article/<int:article_id>/", views.article_detail, name="article_detail"),
    path("review/", views.review_articles, name="review_articles"),

    # Basic APIs
    path("api/leagues/", views.api_leagues, name="api_leagues"),
    path("api/teams/<int:league_id>/", views.api_teams_by_league, name="api_teams_by_league"),
    path("api/articles/", views.api_articles, name="api_articles"),
]
