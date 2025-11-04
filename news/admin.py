"""
news/admin.py

Admin registration for sports models.
"""

from django.contrib import admin
from .models import League, Team, Article, Newsletter


@admin.register(League)
class LeagueAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ("name", "league")
    list_filter = ("league",)
    search_fields = ("name",)


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "league", "team", "approved", "approved_by", "approved_at")
    list_filter = ("approved", "league")
    search_fields = ("title", "body")
    autocomplete_fields = ("author", "league", "team", "approved_by")

    def save_model(self, request, obj, form, change):
        """Auto-assign approving editor if approved in admin."""
        if obj.approved and not obj.approved_by:
            obj.approved_by = request.user
        super().save_model(request, obj, form, change)


@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "league", "created_at")
    list_filter = ("league",)
    search_fields = ("title", "body")
    autocomplete_fields = ("author", "league")
