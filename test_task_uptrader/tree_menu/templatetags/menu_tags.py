from django import template

from tree_menu.models import MenuItem


register = template.Library()


def get_parents(obj):
    result = []
    seen = set()
    while obj.parent:
        if obj.parent.id in seen:
            break
        seen.add(obj.parent.id)
        result.append(obj.parent)
        obj.parent = obj.parent.parent
    return list(reversed(result))


def get_childrens(objs, current_item_obj=None):
    result = []
    for _ in objs:
        if _.parent == current_item_obj:
            result.append(_)
    return result


@register.inclusion_tag('tree_menu/menu.html', takes_context=True)
def draw_menu(context, menu_name, item_name=None):
    all_menu_items = MenuItem.objects.select_related(
        'menu').filter(menu__title=menu_name)

    current_item_name = item_name

    current_item_obj = None

    for _ in all_menu_items:
        if _.name == current_item_name:
            current_item_obj = _
            break

    if not current_item_obj:
        childrens = get_childrens(all_menu_items)
        return {'childrens': childrens, 'menu_title': menu_name}

    parents = get_parents(current_item_obj)
    childrens = get_childrens(all_menu_items, current_item_obj)
    return {
        'parents': parents,
        'childrens': childrens,
        'current_obj': current_item_obj,
        'menu_title': current_item_obj.menu.title}
