from uuid import uuid4
from PIL import Image
from django.contrib.auth.models import AbstractUser
from django.db import models as m
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.core.cache import cache
from django.conf import settings as s

from core.lists import CIVIL_LIST, GENDER_LIST
from timezone_field import TimeZoneField



def get_media_dir(instance, filename, section):
    split = filename.split('.')
    ext = split.pop()
    name = f'{uuid4()}'
    subfolder = f'user-{instance.pk}'
    return f'{subfolder}/{section}/{name}.{ext}'

def avatar_dir(instance, filename):
    return get_media_dir(instance, filename, 'avatar')


class User(AbstractUser):
    """Default user for {{cookiecutter.project_name}}."""

    #: First and last name do not cover name patterns around the globe
    middle_name = m.CharField(max_length=191, blank=True)
    civil = m.PositiveSmallIntegerField(choices=CIVIL_LIST, blank=True, default=1)
    gender = m.CharField(max_length=1, choices=GENDER_LIST, blank=True, default='')
    avatar = m.ImageField(upload_to=avatar_dir, blank=True, null=True)
    bday = m.DateField(null=True, blank=True)
    address1 = m.CharField(max_length=191, blank=True)
    address2 = m.CharField(max_length=191, blank=True)
    city = m.CharField(max_length=191, blank=True)
    zipcode = m.CharField(max_length=50, blank=True)
    country = m.CharField(max_length=2, blank=True)
    mobile = m.CharField(max_length=100, blank=True)
    telephone = m.CharField(max_length=100, blank=True)
    timezone = TimeZoneField(display_GMT_offset=True, max_length=100, blank=True)
    website = m.URLField(max_length=191, blank=True)
    notes = m.TextField(blank=True)
    updated_at = m.DateTimeField(auto_now=True)

    def __str__(self):
        return self.displayname

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.avatar:
            with Image.open(self.avatar.path) as img:
                img.thumbnail((400, 200), Image.ANTIALIAS)
                img.save(self.avatar.path)
        # img.resize((400, 200), Image.ANTIALIAS)
        # path = f'{s.MEDIA_ROOT}{name}.{ext}'
    
        # img.save(filename)
    
        # user = super().save(*args, **kwargs)
        # if self.avatar:
        #     av = Image.open(self.avatar)
        #     av = av.resize((400, 400), Image.ANTIALIAS)
        #     av.save(self.avatar.path)
        #     # with Image.open(user.avatar) as av:
        #     #     user.avatar = av.thumbnail((100, 100))
        # return user

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})

    @property
    def fullname(self):
        return f'{self.first_name} {self.last_name}'

    @property
    def flipname(self):
        return f'{self.last_name.upper()}, {self.first_name}'

    @property
    def displayname(self):
        name = self.email
        if self.username:
            name = self.username
        elif self.fullname:
            name = self.fullname
        return name