from django.urls import path
from . import views




urlpatterns = [
    # 登入登出
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),

    # 功能模块
    path('index/', views.index, name='index'),
    path('ui-elements/', views.us_ui_elements, name='ui-elements'),
    path('chart/', views.us_chart, name='chart'),
    path('tab-panel/', views.us_tab_panel, name='tab-panel'),
    path('table/', views.us_table, name='table'),
    path('form/', views.us_form, name='form'),
    path('empty/', views.empty, name='empty'),

]
