from django import forms
from .models import Article

class ArticleModelForm(forms.ModelForm):
	title		=	forms.CharField()
	content		=	forms.CharField()
	duration	=	forms.DurationField()

	class Meta:
		model = Article
		fields = [
			'title',
			'content',
			"duration",
		]