from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


"""
Sample models

class Sample(models.Model):
    chart_field = models.CharField(max_length=128)
    text_field = models.TextField()
    integer_field = models.IntegerField(default=0)
    positive_integer_field = models.PositiveIntegerField(default=0)
    float_field = models.FloatField(default=0)
    decimal_field = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    foreign_key = models.ForeignKey('Model', related_name='related_name', null=True, blank=True)
    slug_field = models.SlugField(null=True, blank=True)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(null=True, blank=True)
    date_field = models.DateField(null=True, blank=True)
    boolean_field = models.BooleanField(default=False)
    ip_address = models.GenericIPAddressField()
    url_field = models.URLField(max_length=200)
    
    def url(self):
        return "/sample/{}".format(self.id)

class Profile(models.Model):
    user = models.OneToOneField(User)


User.profile = property(lambda u: Profile.objects.get_or_create(user=u)[0])
"""