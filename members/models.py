from django.db import models


class Member(models.Model):
    ACCESSIBILITY_CHOICES = (
        (False, 'PRIVATE'),
        (True, 'PUBLIC')
    )

    member_accessibility = models.BooleanField('Member Accessibility', choices=ACCESSIBILITY_CHOICES)
    first_name = models.CharField('First name', max_length=255)
    last_name = models.CharField('Last name', max_length=255)
    biography = models.CharField('Bio', max_length=1024, blank=True)
    email = models.CharField('Email', max_length=255, blank=True)
    contact_accessibility = models.BooleanField('Contact Accessibility', choices=ACCESSIBILITY_CHOICES)
    phone = models.CharField('Phone', max_length=255, blank=True)
    join_date = models.DateTimeField('Date joined')

    def __str__(self):
        return self.first_name + " " + self.last_name
