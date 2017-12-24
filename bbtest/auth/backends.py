from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q


User = get_user_model()


class Backend(ModelBackend):
    def authenticate(self, request, username=None, password=None):
        try:
            # DARK_TODO  There is no need to LIMIT 1 as we're filtering the columns that have a UNIQUE contraint
            user = User.objects.filter(Q(is_active=True) & (Q(username=username) | Q(email=username)))[0]
            if user.check_password(password):
                return user
        except IndexError:
            pass
        return None
