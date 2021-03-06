from django.forms import ModelForm
from . import models

class UserForm(ModelForm):
    class Meta:
        model = models.Profile
        fields = ('rank',)

class ChallengerForm(ModelForm):
    class Meta:
        model = models.Profile
        fields = ('challenger',)
        
class OutcomeForm(ModelForm):
    class Meta:
        model = models.Profile
        fields = ('rank',)
        