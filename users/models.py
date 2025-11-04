"""
users/models.py

Defines a simple custom User model that supports roles and
subscriptions for a sports news platform.
"""

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    Custom user supporting roles for access control.

    Roles:
        - READER: can browse approved sports articles.
        - JOURNALIST: can write articles and newsletters.
        - EDITOR: can review and approve articles.
    """

    class Role(models.TextChoices):
        READER = "READER", "Reader"
        JOURNALIST = "JOURNALIST", "Journalist"
        EDITOR = "EDITOR", "Editor"

    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.READER,
        help_text="Determines permissions and UI visibility.",
    )

    # Subscriptions: readers can follow journalists or teams/leagues (via news models later)
    subscriptions_journalists = models.ManyToManyField(
        "self",
        symmetrical=False,
        related_name="followers",
        blank=True,
        help_text="Readers following specific journalists.",
        limit_choices_to={"role": Role.JOURNALIST},
    )

    def __str__(self) -> str:
        """Return the username for admin display."""
        return self.username
