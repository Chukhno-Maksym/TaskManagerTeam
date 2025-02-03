from django.contrib.auth.forms import UserCreationForm

from taskmanager.models import Worker


class UserCreateForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Worker
        fields =  UserCreationForm.Meta.fields