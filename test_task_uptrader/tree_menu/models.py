from django.db import models
from django.urls import reverse

from .constans import MENU_TITLE_MAX_LENGTH, MENU_ITEM_NAME_MAX_LENGTH


class Menu(models.Model):
    title = models.CharField(max_length=MENU_TITLE_MAX_LENGTH)


class MenuItem(models.Model):
    menu = models.ForeignKey(
        Menu, on_delete=models.CASCADE, related_name='items')
    name = models.CharField(max_length=MENU_ITEM_NAME_MAX_LENGTH)
    parent = models.ForeignKey(
        'self', on_delete=models.CASCADE, null=True, blank=True)

    def get_absolute_url(self):
        return reverse('model_detail', kwargs={'pk': self.pk})
