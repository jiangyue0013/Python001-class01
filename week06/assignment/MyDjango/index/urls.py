from django.urls import path, re_path, register_converter

from . import views, converters

# 注册自定义过滤器
register_converter(converters.IntConverter, 'myint')
register_converter(converters.FourDigitYearConverter, 'yyyy')


urlpatterns = [
    path('', views.index),
    path('<int:year>/<str:name>', views.name),
    re_path('(?P<year>[0-9]{4}$).html', views.myyear, name='urlyear'),
    path('<yyyy:year>', views.years),
]