from django import forms
from notes.models import Materials

class updatenotesForm(forms.ModelForm):
	class Meta:
		model=Materials
		fields="__all__"