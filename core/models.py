from django.db import models
from custom_users.models import CustomUser

ATTRS = (
    ('FACEBOOK', 'Facebook'),
    ('PHONE', 'Phone number'),
    ('INSTAGRAM', 'Instagram'),
)


COLORS = (
    ('RED', 'Red'),
    ('BLUE', 'Blue'),
    ('GREEN', 'Green'),
    ('WHITE', 'White'),
    ('BLACK', 'Black'),
)


class Attribute(models.Model):
    name = models.CharField(max_length=20, choices=ATTRS)
    value = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return u'{0} - {1}'.format(self.name, self.value)

class Profile(models.Model):
    name = models.CharField(max_length=20)
    user = models.ForeignKey(CustomUser)
    color = models.CharField(max_length=20, choices=COLORS)
    connections = models.ManyToManyField('Profile', blank=True)
    attributes = models.ManyToManyField(Attribute, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return u'{0} - {1}'.format(self.user, self.name)

# class ProfileAttribute(models.Model):
#     profile = models.ForeignKey(Profile)
#     attribute = models.ForeignKey(Attribute)
#     value = models.CharField(max_length=100)
#
#     def __unicode__(self):
#         return u'{0} - {1}'.format(self.profile.user, self.name)
