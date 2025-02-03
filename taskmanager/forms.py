from django.contrib.auth.forms import UserCreationForm
from django import forms

from taskmanager.models import Worker, Task, PRIORITY_CHOICES

TEAM_CHOICES = (
    ("","All"),
    ("Development Team","Development Team"),
    ("Marketing Team","Marketing Team"),
    ("Design Team","Design Team"),
    ("QA Team","QA Team"),
    ("Support Team","Support Team"),
)

STATUS_CHOICES = (
    ("", "All"),
    ("False","In progress"),
    ("True","Done"),
)


class UserCreateForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Worker
        fields =  UserCreationForm.Meta.fields


class TaskSearchForm(forms.Form):
    team = forms.ChoiceField(choices=TEAM_CHOICES,
                                      required=False,
                                      label="Select Team",)

    status = forms.ChoiceField(choices=STATUS_CHOICES,
                               required=False,
                               label="Status",)

    priority = forms.ChoiceField(choices=PRIORITY_CHOICES,
                                 required=False,
                                 label="Priority",)

class TaskCreateForm(forms.ModelForm):
    deadline = forms.DateTimeField(
        required=False,
        widget=forms.DateTimeInput(
            attrs={"type": "datetime-local"}, format="%Y-%m-%dT%H:%M"
        )
    )

    assignees = forms.ModelMultipleChoiceField(
        queryset=Worker.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )


    class Meta:
        model = Task
        fields = "__all__"
