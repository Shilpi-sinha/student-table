from django import forms
from data.models import*
class studentform(forms.ModelForm):
	class Meta:
		model=student
		fields='__all__'
