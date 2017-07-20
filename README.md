# django-administrate
RU: Нормальная админка для django
EN: Just one ofter admin panel for django

#Установка/Install
1.
RU: Добавьте 'administrate' в INSTALLED_APPS (settings.py)
EN: Add 'administrate' to INSTALLED_APPS in settings.py file
2.
RU: Добавьте 'from django.conf.urls import url,include' в urls.py если еще нет подобного импорта
EN: Add 'from django.conf.urls import url,include' to urls.py , or add need to exists string
3.
RU: Добавьте 'url(r'^administrate/', include('administrate.urls')),' в массив urlpatterns который опять же в urls.py
помните про логику чтоб можно было попасть в эти правила
EN: Add 'url(r'^administrate/$', include('administrate.urls')),' to urlpatterns array in  urls.py file, and dont forget about logic

#Разработка/Develop
RU:
EN: