from typing import Any
from django.views import generic

from .models import MenuItem


class HomeView(generic.TemplateView):
    template_name = 'tree_menu/home.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        return super().get_context_data(**kwargs)


class MenuItemDetailView(generic.DetailView):
    template_name = 'tree_menu/home.html'
    slug_url_kwarg = 'item_name'
    slug_field = 'name'
    model = MenuItem

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        current_item = self.object
        menu_title = current_item.menu.title
        context['active_menu_items'] = {
            menu_title: current_item.name}
        return context
