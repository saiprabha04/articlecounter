from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic.base import RedirectView,TemplateView



from questionT.models import ArticleT


# Create your views here.
class ArticleDetail(TemplateView):

    template_name = "home.html"

    def get_context_data(self, *args,**kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_article'] = ArticleT.objects.get(pk=self.kwargs.get('pk',None))
        return context


class ArticleCounterRedirectView(RedirectView):

    permanent = False
    query_string = True
    pattern_name = 'article-detail'

    def get_redirect_url(self, *args, **kwargs):
        article = get_object_or_404(ArticleT, pk=kwargs['pk'])
        article.counter +=1
        article.save()
        return super().get_redirect_url(*args, **kwargs)

def first(request):
    return render(request,"first.html")