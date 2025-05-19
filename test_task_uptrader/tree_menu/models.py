from django.db import models

from .constans import MENU_TITLE_MAX_LENGTH, MENU_ITEM_NAME_MAX_LENGTH


class Menu(models.Model):
    title = models.CharField(max_length=MENU_TITLE_MAX_LENGTH)

    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.title = self.title.lower()
        self.full_clean()
        super().save(*args, **kwargs)


class MenuItem(models.Model):
    name = models.CharField(max_length=MENU_ITEM_NAME_MAX_LENGTH, unique=True)
    menu = models.ForeignKey(
        Menu, on_delete=models.CASCADE, related_name='items', blank=True)
    parent = models.ForeignKey(
        'self', on_delete=models.CASCADE, null=True, blank=True,
        related_name='childrens')

    class Meta:
        verbose_name = 'Объект меню'
        verbose_name_plural = 'Объекты меню'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.parent:
            self.menu = self.parent.menu
        self.full_clean()
        super().save(*args, **kwargs)
