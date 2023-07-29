# pages/views.py

# Импортируем класс TemplateView, чтобы унаследоваться от него.
from django.views.generic import TemplateView


class HomePage(TemplateView):
    # В атрибуте template_name обязательно указывается имя шаблона,
    # на основе которого будет создана возвращаемая страница.
    template_name = 'pages/index.html'