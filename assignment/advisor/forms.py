from django import forms
from .models import Advisor

class AdvisorForm(forms.ModelForm):
	class Meta:
		model = Advisor
		fields = [
			'name',
			'photo_url'
		]