"""
news/models.py

Core sports news models:
- League: e.g., Premier League, NBA.
- Team: belongs to a league.
- Article: sports article with optional league/team association.
- Newsletter: optional long-form updates by journalists.
"""

from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone

User = settings.AUTH_USER_MODEL


class League(models.Model):
    """Represents a sports league (e.g., NBA, EPL)."""
    name = models.CharField(max_length=120, unique=True)

    def __str__(self) -> str:
        return self.name


class Team(models.Model):
    """Represents a sports team within a league."""
    name = models.CharField(max_length=120)
    league = models.ForeignKey(League, on_delete=models.CASCADE, related_name="teams")

    class Meta:
        unique_together = ("name", "league")

    def __str__(self) -> str:
        return f"{self.name} ({self.league.name})"


class Article(models.Model):
    """
    Sports article written by a journalist and optionally linked
    to a league or a team. Editors approve articles before they are public.
    """
    title = models.CharField(max_length=200)
    body = models.TextField()
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="sports_articles",
        limit_choices_to={"role": "JOURNALIST"},
    )

    league = models.ForeignKey(
        League,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="articles",
        help_text="Optional league context.",
    )
    team = models.ForeignKey(
        Team,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="articles",
        help_text="Optional team context.",
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    approved = models.BooleanField(default=False)
    approved_by = models.ForeignKey(
        User,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="approved_sports_articles",
        limit_choices_to={"role": "EDITOR"},
    )
    approved_at = models.DateTimeField(null=True, blank=True)

    def clean(self) -> None:
        """
        Enforce that approved articles must have an approving editor.
        """
        if self.approved and not self.approved_by:
            raise ValidationError("Approved articles must include an approving editor.")

    def save(self, *args, **kwargs) -> None:
        """
        Automatically set approval timestamp when approved.
        """
        if self.approved and not self.approved_at:
            self.approved_at = timezone.now()
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        ctx = self.team.name if self.team else (self.league.name if self.league else "General")
        return f"{self.title} [{ctx}]"


class Newsletter(models.Model):
    """
    Optional long-form newsletter for sports readers.
    """
    title = models.CharField(max_length=200)
    body = models.TextField()
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="sports_newsletters",
        limit_choices_to={"role": "JOURNALIST"},
    )
    league = models.ForeignKey(
        League,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="newsletters",
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"Newsletter: {self.title}"
