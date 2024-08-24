from django import forms
from velocity.models import Velocity

class VelocityForm(forms.ModelForm):
    class Meta:
        model=Velocity
        fields={"title","name","email","mobile","description"}

