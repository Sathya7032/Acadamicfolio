from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from .models import *

class MySocialAccountAdapter(DefaultSocialAccountAdapter):
    def save_user(self, request, sociallogin, form=None):
        user = super().save_user(request, sociallogin, form)
        Profile.objects.get_or_create(user=user)
        return user
