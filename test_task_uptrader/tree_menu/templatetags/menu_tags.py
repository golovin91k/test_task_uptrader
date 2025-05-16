from django import template

from tree_menu.models import Menu


register = template.Library()


@register.inclusion_tag('tree_menu/menu.html', takes_context=True)
def draw_menu(context, menu_name):
    request = context['request']
    return {'menu_tree': [1, 2, 3, 4, 5]}

