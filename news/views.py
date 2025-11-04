"""
news/views.py

Views for the sports news app. Includes simple pages and
read-only API endpoints using DRF function views.
"""

from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone

from .models import Article, League, Team

# -------------------------
# Pages
# -------------------------

def home(request):
    """
    Show approved sports articles. Newest first.
    """
    articles = Article.objects.filter(approved=True).order_by("-approved_at", "-created_at")
    leagues = League.objects.all()
    context = {"articles": articles, "leagues": leagues}
    return render(request, "news/home.html", context)


def article_detail(request, article_id: int):
    """
    Show a single sports article. Allow authors/editors to view drafts.
    """
    article = get_object_or_404(Article, id=article_id)
    if not article.approved and request.user != article.author and getattr(request.user, "role", "") != "EDITOR":
        messages.error(request, "You are not allowed to view this draft.")
        return redirect("home")
    return render(request, "news/article_detail.html", {"article": article})


def review_articles(request):
    """
    List all unapproved articles for quick review.
    For demo simplicity, no login wall.
    """
    pending = Article.objects.filter(approved=False).order_by("-created_at")
    return render(request, "news/review_articles.html", {"articles": pending})

# -------------------------
# APIs (DRF)
# -------------------------
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["GET"])
def api_leagues(request):
    """Return all leagues as JSON."""
    data = [{"id": l.id, "name": l.name} for l in League.objects.all()]
    return Response(data)


@api_view(["GET"])
def api_teams_by_league(request, league_id: int):
    """Return teams for a given league ID."""
    teams = Team.objects.filter(league_id=league_id)
    data = [{"id": t.id, "name": t.name, "league": t.league.name} for t in teams]
    return Response(data)


@api_view(["GET"])
def api_articles(request):
    """Return approved sports articles."""
    qs = Article.objects.filter(approved=True).order_by("-approved_at", "-created_at")
    data = [
        {
            "id": a.id,
            "title": a.title,
            "author": a.author.username,
            "league": a.league.name if a.league else None,
            "team": a.team.name if a.team else None,
            "approved_at": a.approved_at,
        }
        for a in qs
    ]
    return Response(data)
