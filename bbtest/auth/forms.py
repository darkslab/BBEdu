from django.forms import ValidationError, Form, CharField, PasswordInput
from django.contrib.auth import get_user_model, authenticate


User = get_user_model()

class AuthenticationForm(Form):
    username = CharField(label="Email or Username", max_length=User.USERNAME_LENGTH_MAX)
    password = CharField(label="Password", widget=PasswordInput, strip=False)

    def __init__(self, request=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = request
        self._user = None

    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        if username and password:
            self._user = authenticate(self.request, username=username, password=password)
            if self._user is None:
                raise ValidationError("Please enter a correct email or username and password.")

        return self.cleaned_data

    def get_user(self):
        return self._user
