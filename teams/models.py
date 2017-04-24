from django.db import models

from members.models import Member


class Team(models.Model):
    ACCESSIBILITY_CHOICES = (
        (False, 'PRIVATE'),
        (True, 'PUBLIC')
    )

    name = models.CharField('Name', max_length=255)
    website = models.CharField('Website', max_length=255, blank=True)
    admission = models.BooleanField('Admission', choices=ACCESSIBILITY_CHOICES)
    team_members = models.ManyToManyField('Team members', Member)
