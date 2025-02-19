from re import template
from typing import Any
from webbrowser import get
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

from goods.models import Categories



class IndexView(TemplateView):
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Home - Главная' 
        context['content'] = 'Магазин мебели Home'
        return context
    
class AboutView(TemplateView):
    template_name = 'main/about.html'
    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["title"] = 'Home - О нас' 
        context["content"] = 'О нас'
        context['text_on_page'] = "Cooll magazin"
        return context
    


# def index(request):

#     context: dict = {
#         'title': 'Home - Главная',
#         'content': "Магазин мебели HOME",     
#     }
#     return render(request, 'main/index.html', context)

# def about(request):
#     context: dict = {
#         'title': 'Home - О нас',
#         'content': "О нас", 
#         'text_on_page': 'Wise mans say would it be a sin if cant'
        
#     }
#     return render(request, 'main/about.html', context)