from django.forms import ModelForm
from .models import KontakModel

class KontakFormModel(ModelForm):
    class Meta:
        model = KontakModel
        fields = '__all__'