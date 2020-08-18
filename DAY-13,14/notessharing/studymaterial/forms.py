from django.forms import ModelForm # from django import forms

from studymaterial.models import Notes


class AddNotesForm(ModelForm):
	class Meta:

		model=Notes

		fields='__all__' # ['branch','subject','description']



