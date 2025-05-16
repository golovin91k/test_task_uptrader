from typing import Any
from django.shortcuts import render
from django.views import generic


class HomeView(generic.TemplateView):
    template_name = 'tree_menu/home.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        print(self.request.path)
        return super().get_context_data(**kwargs)
