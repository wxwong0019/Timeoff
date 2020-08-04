from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import (
		CreateView,
		DetailView,
		ListView,
		UpdateView,
		DeleteView
	)

from .models import Article
from .forms import ArticleModelForm
# Create your views here.

class ArticleListView(ListView):
	template_name = 'articles/article_list.html'
	queryset = Article.objects.all()	#<blog>/<modelname>_list.htmln

class ArticleDetailView(DetailView):
	template_name = 'articles/article_detail.html'
	queryset = Article.objects.all()

	def get_object(self):
		id_ = self.kwargs.get('id')
		return get_object_or_404(Article, id = id_)

class ArticleCreateView(CreateView):
	template_name = 'articles/article_create.html'
	form_class = ArticleModelForm
	queryset = Article.objects.all()
	success_url = '/blog/create'

	def form_valid(self, fors):
		print(fors.cleaned_data)
		return super().form_valid(fors)


class ArticleUpdateView(UpdateView):
	template_name = 'articles/article_create.html'
	form_class = ArticleModelForm
	queryset = Article.objects.all()
	
	def form_valid(self, fors):
		print(fors.cleaned_data)
		return super().form_valid(fors)

	def get_object(self):
		id_ = self.kwargs.get('id')
		return get_object_or_404(Article, id = id_)	

class ArticleDeleteView(DeleteView):
	template_name = 'articles/article_delete.html'

	def get_object(self):
		id_ = self.kwargs.get('id')
		return get_object_or_404(Article, id = id_)

	def get_success_url(self):
		return reverse("articles:article-list")